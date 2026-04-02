#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GitLink 帮助文档爬虫 - 从GitHub仓库获取文档"""

import os
import shutil
import subprocess
from pathlib import Path

REPO_URL = "https://gitlink.org.cn/Gitlink/gitlink_help_center.git"
OUTPUT_DIR = "docs/library/assets/gitlink"
TEMP_DIR = "/tmp/gitlink_docs"


def main():
    print("Cloning GitLink help docs...")

    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)

    subprocess.run(["git", "clone", "--depth", "1", REPO_URL, TEMP_DIR], check=True)

    source_docs = Path(TEMP_DIR) / "docs"

    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)

    shutil.copytree(source_docs, OUTPUT_DIR, dirs_exist_ok=True)

    shutil.rmtree(TEMP_DIR)

    print("\nDone! Docs saved to " + OUTPUT_DIR)


if __name__ == "__main__":
    main()
