"""News-image entry: copy the bundled infographic to /output/entry.png.

Runs with the Python standard library only, no network, and writes
the same bytes on every run: entry.png is shipped in this repository.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    src = HERE / "entry.png"
    if not src.is_file():
        raise FileNotFoundError("entry.png missing beside main.py")
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, OUT / "entry.png")


if __name__ == "__main__":
    main()
