#!/usr/bin/python3
"""
Markdown to HTML conversion script.
"""

import sys
import os

if __name__ == "__main__":
    # Check if the number of arguments is less than 2
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    # Check if the Markdown file exists
    markdown_file = sys.argv[1]
    if not os.path.isfile(markdown_file):
        sys.stderr.write(f"Missing {markdown_file}\n")
        sys.exit(1)

    # If everything is correct, print nothing and exit successfully
    sys.exit(0)

