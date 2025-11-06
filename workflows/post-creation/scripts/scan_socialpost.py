#!/usr/bin/env python3
"""
Logseq [[socialpost]] Entry Scanner

Scans Logseq pages and journals for blocks tagged with [[socialpost]].
Extracts full block context including multi-paragraph highlights.

Usage:
    cd /Users/timmetz/Library/CloudStorage/Dropbox/Logseq
    python3 <path-to-this-script>

Output:
    /tmp/logseq_socialpost_entries.json - JSON file with all found entries

Based on: Pattern used successfully in logseq-dot5-review workflow
"""

import os
import re
import json
import sys
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s',
    stream=sys.stderr
)


def extract_block_context(lines, target_idx):
    """
    Extract the FULL Logseq block including multi-paragraph highlights.

    This handles Readwise/Logseq highlights that span multiple paragraphs,
    ensuring all content is captured in the context.

    Args:
        lines: List of lines from the markdown file
        target_idx: Index of the line containing [[socialpost]]

    Returns:
        tuple: (context_string, first_content_line)
            - context_string: Full block content as newline-joined string
            - first_content_line: The first line of actual content
    """
    # Get the indentation level of the target line
    target_line = lines[target_idx]
    target_indent = len(target_line) - len(target_line.lstrip())

    # Find the parent block (line with less indentation above)
    parent_line = None
    parent_idx = target_idx - 1
    parent_indent = None

    while parent_idx >= 0:
        line = lines[parent_idx]
        if line.strip():  # Skip empty lines
            line_indent = len(line) - len(line.lstrip())
            if line_indent < target_indent:
                parent_line = line.strip()
                parent_indent = line_indent
                break
        parent_idx -= 1

    # Extract the FULL block including all continuation paragraphs
    block_lines = []

    if parent_line and parent_idx >= 0:
        # Find the START of the highlight block (the bullet point)
        block_start_idx = parent_idx
        check_idx = parent_idx - 1

        while check_idx >= 0:
            line = lines[check_idx]
            if line.strip():
                line_indent = len(line) - len(line.lstrip())
                if line_indent < parent_indent:
                    break
                elif line_indent == parent_indent:
                    if line.strip().startswith('-'):
                        break
                block_start_idx = check_idx
            check_idx -= 1

        # Capture from block_start_idx forward until we reach target line
        for idx in range(block_start_idx, target_idx):
            line = lines[idx]
            if line.strip():
                line_indent = len(line) - len(line.lstrip())
                if line_indent >= parent_indent:
                    block_lines.append(line.strip())

    # Add target line (the Tags line)
    block_lines.append(target_line.strip())

    # Add immediate children of target (Notes, etc.)
    child_idx = target_idx + 1
    while child_idx < len(lines):
        line = lines[child_idx]
        if line.strip():
            line_indent = len(line) - len(line.lstrip())
            if line_indent > target_indent:
                block_lines.append(line.strip())
            else:
                break
        child_idx += 1

    context = '\n'.join(block_lines)

    # For parent_line return value, use the actual first line of the highlight
    if block_lines:
        first_content_line = block_lines[0] if block_lines else parent_line
    else:
        first_content_line = parent_line

    return context, first_content_line


def scan_logseq_for_socialpost_entries(logseq_root):
    """
    Scan Logseq pages and journals for [[socialpost]] entries.

    Args:
        logseq_root: Path to Logseq root directory

    Returns:
        tuple: (entries_found, errors)
            - entries_found: List of entry dicts
            - errors: List of (file, error_msg) tuples for skipped files
    """
    entries_found = []
    errors = []

    for subdir in ['pages', 'journals']:
        subdir_path = logseq_root / subdir
        if not subdir_path.exists():
            logging.warning(f"Subdirectory not found: {subdir_path}")
            continue

        for md_file in subdir_path.glob('*.md'):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    lines = content.split('\n')

                for i, line in enumerate(lines):
                    try:
                        # Find [[socialpost]] entries
                        if '[[socialpost]]' not in line:
                            continue

                        # Extract smart context based on indentation
                        context, parent_line = extract_block_context(lines, i)

                        # Extract tags from the line
                        tags = re.findall(r'\[\[([^\]]+)\]\]', line)

                        # Get file birth time (creation time)
                        file_stat = md_file.stat()
                        birth_time = file_stat.st_birthtime

                        entries_found.append({
                            'file': str(md_file.relative_to(logseq_root)),
                            'line_num': i + 1,
                            'line': line.strip(),
                            'context': context,
                            'tags': tags,
                            'filename': md_file.name,
                            'parent_line': parent_line,
                            'birth_time': birth_time,
                            'absolute_path': str(md_file)
                        })
                    except Exception as e:
                        error_msg = f"Line {i+1}: {str(e)}"
                        logging.warning(f"Error processing line in {md_file.name}: {error_msg}")

            except UnicodeDecodeError as e:
                error_msg = f"Encoding error: {str(e)}"
                logging.error(f"Cannot read {md_file.name}: {error_msg}")
                errors.append((str(md_file.name), error_msg))
            except IOError as e:
                error_msg = f"I/O error: {str(e)}"
                logging.error(f"Cannot access {md_file.name}: {error_msg}")
                errors.append((str(md_file.name), error_msg))
            except Exception as e:
                error_msg = f"Unexpected error: {str(e)}"
                logging.error(f"Error processing {md_file.name}: {error_msg}")
                errors.append((str(md_file.name), error_msg))

    return entries_found, errors


def main():
    """Main execution function"""
    try:
        # Expected to be run from Logseq root directory
        logseq_root = Path.cwd()

        # Validate we're in the right directory
        if not (logseq_root / 'pages').exists() or not (logseq_root / 'journals').exists():
            logging.error("Must be run from Logseq root directory")
            logging.error(f"Current directory: {logseq_root}")
            logging.error("Expected: /Users/timmetz/Library/CloudStorage/Dropbox/Logseq")
            print("\nERROR: Not in Logseq directory")
            print("Solution: cd /Users/timmetz/Library/CloudStorage/Dropbox/Logseq")
            return 1

        logging.info("Scanning Logseq for [[socialpost]] entries...")
        print("Scanning Logseq for [[socialpost]] entries...")

        # Scan for entries
        entries_found, errors = scan_logseq_for_socialpost_entries(logseq_root)

        # Save to temp file
        output_file = Path('/tmp/logseq_socialpost_entries.json')
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(entries_found, f, indent=2, ensure_ascii=False)
        except IOError as e:
            logging.error(f"Cannot write output file: {e}")
            print(f"\nERROR: Cannot write to {output_file}")
            return 1

        # Report results
        print(f"\nFound {len(entries_found)} [[socialpost]] entries")
        print(f"Saved to {output_file}")

        # Report errors if any
        if errors:
            print(f"\n⚠️  Skipped {len(errors)} file(s) due to errors:")
            for filename, error_msg in errors[:5]:
                print(f"  - {filename}: {error_msg}")
            if len(errors) > 5:
                print(f"  ... and {len(errors) - 5} more")
            print("\nCheck stderr for full error log")
            return 1 if len(entries_found) == 0 else 0

        return 0

    except KeyboardInterrupt:
        print("\n\nScan interrupted by user")
        return 130
    except Exception as e:
        logging.error(f"Unexpected error in main(): {e}", exc_info=True)
        print(f"\nERROR: {e}")
        return 1


if __name__ == '__main__':
    exit(main())
