#!/usr/bin/env python3
"""Simple image inventory script for the project.

Run from the project root (PowerShell):
  & .\.venv\Scripts\Activate.ps1
  python .\scripts\inspect_images.py

This prints counts by extension, sizes in MB, and the top 20 largest images.
"""
from pathlib import Path

def format_mb(n: int) -> str:
    return f"{n/1024/1024:.2f} MB"

def main():
    root = Path("img")
    if not root.exists():
        print("Directory 'img' not found in project root. Run from project root.")
        return

    exts = ['.jpg', '.jpeg', '.png', '.webp', '.psd']
    images = [p for p in root.rglob('*') if p.suffix.lower() in exts]

    counts = {ext: 0 for ext in exts}
    sizes = {ext: 0 for ext in exts}

    for p in images:
        s = p.suffix.lower()
        counts[s] += 1
        try:
            sizes[s] += p.stat().st_size
        except OSError:
            print(f"Could not stat file: {p}")

    total = sum(sizes.values())

    print("Image inventory for 'img/' (run from project root)")
    print('-' * 60)
    print('Counts:')
    for k, v in counts.items():
        print(f"  {k}: {v}")
    print('\nSizes:')
    for k, v in sizes.items():
        print(f"  {k}: {format_mb(v)}")
    print('\nTotal size (img/):', format_mb(total))

    print('\nTop 20 largest images:')
    for p in sorted(images, key=lambda x: x.stat().st_size if x.exists() else 0, reverse=True)[:20]:
        try:
            print(f"  {p} — {format_mb(p.stat().st_size)}")
        except OSError:
            print(f"  {p} — (unable to read size)")

if __name__ == '__main__':
    main()
