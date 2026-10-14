#!/usr/bin/env python3
"""Build a small, explicit public bundle for the GoodEats static site."""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PUBLIC = ROOT / "public"
ASSETS = (
    (ROOT / "images" / "group-order-editorial.jpg", PUBLIC / "images" / "group-order-editorial.jpg"),
    (ROOT / "fonts" / "BricolageGrotesque-latin.woff2", PUBLIC / "fonts" / "BricolageGrotesque-latin.woff2"),
    (ROOT / "fonts" / "OFL.txt", PUBLIC / "fonts" / "OFL.txt"),
)


def build() -> None:
    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
    (PUBLIC / "images").mkdir(parents=True)
    (PUBLIC / "fonts").mkdir(parents=True)
    shutil.copy2(ROOT / "index.html", PUBLIC / "index.html")
    for source, destination in ASSETS:
        if not source.is_file():
            raise FileNotFoundError(f"Required public asset is missing: {source.relative_to(ROOT)}")
        shutil.copy2(source, destination)
    print("Built the GoodEats public site into ./public (HTML, image, and licensed font only).")


if __name__ == "__main__":
    build()
