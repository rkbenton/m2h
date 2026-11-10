#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#   "markdown",
#   "pyobjc-framework-Cocoa",
# ]
# ///

"""
Function: 
    Takes Markdown text from the macOS pasteboard, converts it to 
    HTML (GitHub-Flavored style), and copies the result back to 
    the pasteboard as an HTML flavor.

How to run:
    uv run m2h.py
"""

import markdown
from AppKit import NSPasteboard, NSPasteboardTypeHTML, NSPasteboardTypeString
import sys

def convert():
    pb = NSPasteboard.generalPasteboard()
    
    # 1. Audit available flavors
    flavors = pb.types()
    print("📋 Pasteboard Flavor Audit:")
    if not flavors:
        print("  [Empty Pasteboard]")
    else:
        for flavor in flavors:
            print(f"  - {flavor}")
    print("-" * 35)

    # 2. Get Markdown text
    md_text = pb.stringForType_(NSPasteboardTypeString)
    
    if not md_text:
        print("❌ Error: No text found in the pasteboard.", file=sys.stderr)
        return

    # 3. Convert to HTML
    # 'extra' includes tables, fencend code blocks, etc.
    # 'sane_lists' makes it behave more like GFM
    try:
        html_output = markdown.markdown(
            md_text, 
            extensions=['extra', 'sane_lists', 'nl2br']
        )

        if not html_output:
            print("⚠️  Conversion resulted in empty output.")
            return

        # 4. Write back to pasteboard
        # We clear first, then set BOTH HTML and String types.
        # This allows you to paste "Rich Text" into mail apps 
        # or raw HTML into code editors.
        pb.clearContents()
        pb.setString_forType_(html_output, NSPasteboardTypeHTML)
        pb.setString_forType_(html_output, NSPasteboardTypeString)
        
        print("✅ Success!")
        print(f"   Input:  {len(md_text)} characters (Markdown)")
        print(f"   Output: {len(html_output)} characters (HTML)")
        print("🚀 Your pasteboard now contains the Rich Text/HTML version.")

    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    convert()