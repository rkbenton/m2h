# m2h — Markdown to HTML (via clipboard)

A macOS utility that converts Markdown text to HTML using the system clipboard. Copy some Markdown, run `m2h`, and your clipboard is replaced with the rendered HTML — in both rich-text and plain-text flavors, so you can paste into mail clients or code editors alike.

## Requirements

- macOS
- [uv](https://docs.astral.sh/uv/) — dependencies are managed automatically via the inline PEP 723 declaration

## Usage

1. Copy some Markdown text to your clipboard
2. Run:
   ```bash
   uv run m2h.py
   ```
3. Paste the resulting HTML wherever you need it

## Run from anywhere (symlink setup)

To call `m2h` from any directory, first add a shebang line to the script so the OS knows how to execute it directly, then create a symlink on your `PATH`.

**1. Add a shebang as the very first line of `m2h.py`:**

```python
#!/usr/bin/env -S uv run --script
```

**2. Make the script executable:**

```bash
chmod +x /path/to/m2h/m2h.py
```

**3. Symlink it onto your PATH:**

```bash
ln -s /path/to/m2h/m2h.py /usr/local/bin/m2h
```

Use the full absolute path (e.g. `/Users/yourname/...`). After this, running `m2h` from any terminal session will work.

## Markdown extensions enabled

| Extension    | Effect |
|--------------|--------|
| `extra`      | Tables, fenced code blocks, footnotes, and more |
| `sane_lists` | List handling consistent with GitHub-Flavored Markdown |
| `nl2br`      | Single newlines converted to `<br>` tags |
