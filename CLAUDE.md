# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`m2h` is a single-file macOS utility (`m2h.py`) that reads Markdown text from the system clipboard, converts it to HTML (GitHub-Flavored Markdown style), and writes the result back to the clipboard in both `NSPasteboardTypeHTML` and `NSPasteboardTypeString` flavors.

## Running

```bash
uv run m2h.py
```

Dependencies are declared inline using PEP 723 format and managed automatically by `uv` — no separate install step needed.

## Dependencies

- `markdown` — Markdown-to-HTML conversion with extensions: `extra`, `sane_lists`, `nl2br`
- `pyobjc-framework-Cocoa` — macOS pasteboard access via `NSPasteboard`

## Architecture

The entire logic lives in a single `convert()` function in `m2h.py`:

1. Audits pasteboard flavors (prints for debugging)
2. Reads `NSPasteboardTypeString` from the pasteboard
3. Converts with `markdown.markdown()` using the three extensions above
4. Clears the pasteboard and writes back both `NSPasteboardTypeHTML` and `NSPasteboardTypeString`

The dual-flavor write is intentional: HTML flavor for rich-text paste targets (mail clients, etc.) and String flavor for plain-text targets (code editors, etc.).

**macOS only** — depends on the Cocoa framework.
