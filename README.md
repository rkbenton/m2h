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

The script already has a shebang (`#!/usr/bin/env -S uv run --script`). To call `m2h` from any directory:

**1. Make the script executable:**

```bash
chmod +x /path/to/m2h/m2h.py
```

**2. Symlink it onto your PATH:**

```bash
ln -s /path/to/m2h/m2h.py ~/.local/bin/m2h
```

Use the full absolute path (e.g. `/Users/yourname/...`). After this, running `m2h` from any terminal session will work.

`~/.local/bin` is preferred over `/usr/local/bin`: it needs no `sudo`, and it matches
where the companion [h2m](https://github.com/rkbenton/h2m) utility installs.

> `~/.local/bin` must be on your PATH. If it isn't, add this to your `~/.zshrc`:
> ```bash
> export PATH="$HOME/.local/bin:$PATH"
> ```

### If the project lives in Dropbox

**Dropbox uses one of two locations depending on how it was installed** — check which
one exists on your machine before copying a command:

```bash
ls -d ~/Dropbox ~/Library/CloudStorage/Dropbox 2>/dev/null
```

Older installs (and machines upgraded from them) use `~/Dropbox`; newer installs use
the File Provider path under `~/Library/CloudStorage`. Or let the shell pick whichever
is present:

```bash
for d in ~/Dropbox ~/Library/CloudStorage/Dropbox; do
  [ -f "$d/PythonStuff/m2h/m2h.py" ] || continue
  chmod +x "$d/PythonStuff/m2h/m2h.py"
  ln -sf "$d/PythonStuff/m2h/m2h.py" ~/.local/bin/m2h
  break
done
```

> **Use a symlink (`ln -s`), not a hard link.** A hard link points at the file's inode
> rather than its path, so if Dropbox ever replaces `m2h.py` instead of editing it in
> place, `m2h` will keep silently running a stale copy of the script. Check what you
> have with `ls -l ~/.local/bin/m2h` — a symlink shows an `->` arrow. If it doesn't,
> replace it: `rm ~/.local/bin/m2h` and re-run the `ln -s` above.

## Markdown extensions enabled

| Extension    | Effect |
|--------------|--------|
| `extra`      | Tables, fenced code blocks, footnotes, and more |
| `sane_lists` | List handling consistent with GitHub-Flavored Markdown |
| `nl2br`      | Single newlines converted to `<br>` tags |
