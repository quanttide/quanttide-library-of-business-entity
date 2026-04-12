#!/usr/bin/env python3
"""Agent Skills 文档爬虫 - 从 GitHub 仓库获取 MDX 源文件"""

import shutil
from pathlib import Path
import re

REPO_DIR = "/tmp/agentskills/docs"
OUTPUT_DIR = "assets/library/assets/agentskills"

PAGES = [
    ("overview.md", "home.mdx", "Overview"),
    ("concept/what-are-skills.md", "what-are-skills.mdx", "What are skills?"),
    ("specification.md", "specification.mdx", "Specification"),
    ("clients.md", "clients.mdx", "Client Showcase"),
    ("skill-creation/quickstart.md", "skill-creation/quickstart.mdx", "Quickstart"),
    (
        "skill-creation/best-practices.md",
        "skill-creation/best-practices.mdx",
        "Best practices",
    ),
    (
        "skill-creation/optimizing-descriptions.md",
        "skill-creation/optimizing-descriptions.mdx",
        "Optimizing descriptions",
    ),
    (
        "skill-creation/evaluating-skills.md",
        "skill-creation/evaluating-skills.mdx",
        "Evaluating skills",
    ),
    (
        "skill-creation/using-scripts.md",
        "skill-creation/using-scripts.mdx",
        "Using scripts",
    ),
    (
        "client-implementation/adding-skills-support.md",
        "client-implementation/adding-skills-support.mdx",
        "Adding skills support",
    ),
]


def process_mdx(content: str, title: str) -> str:
    lines = content.split("\n")
    in_frontmatter = False
    md_lines = []
    skip_until_newline = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        if stripped == "---":
            if not in_frontmatter:
                in_frontmatter = True
                continue
            else:
                in_frontmatter = False
                continue

        if in_frontmatter:
            continue

        if stripped.startswith("import ") or stripped.startswith("export "):
            continue

        if stripped.startswith("<Card"):
            skip_until_newline = True
            continue
        if stripped == "</Card>" or stripped == "/>":
            skip_until_newline = False
            continue
        if skip_until_newline:
            continue

        if stripped.startswith("<CardGroup") or stripped.startswith("</CardGroup"):
            continue
        if stripped.startswith("<LogoCarousel") or stripped.startswith(
            "</LogoCarousel"
        ):
            continue
        if stripped.startswith(">"):
            continue

        md_lines.append(line)

    md = f"# {title}\n\n"
    md += "\n".join(md_lines)

    md = re.sub(r"\n{3,}", "\n\n", md)

    return md.strip()


def main():
    print("Processing Agent Skills documentation from GitHub...")

    if Path(OUTPUT_DIR).exists():
        shutil.rmtree(OUTPUT_DIR)
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

    for output_file, source_file, title in PAGES:
        source = Path(REPO_DIR) / source_file

        if not source.exists():
            print(f"Source not found: {source}")
            continue

        content = source.read_text(encoding="utf-8")
        md_content = process_mdx(content, title)

        output_path = Path(OUTPUT_DIR) / output_file
        output_path.parent.mkdir(parents=True, exist_ok=True)

        output_path.write_text(md_content, encoding="utf-8")
        print(f"Saved: {output_path}")

    index_content = """# Agent Skills

Agent Skills 是一个简单、开放的格式，用于为 AI 代理提供新能力和专业知识。

## 文档目录

### 概念
- [什么是技能？](concept/what-are-skills.md)

### 规范
- [规范说明](specification.md)

### 展示
- [客户端展示](clients.md)

### 技能创建（For skill creators）
- [快速开始](skill-creation/quickstart.md)
- [最佳实践](skill-creation/best-practices.md)
- [优化描述](skill-creation/optimizing-descriptions.md)
- [评估技能](skill-creation/evaluating-skills.md)
- [使用脚本](skill-creation/using-scripts.md)

### 客户端实现（For client implementors）
- [添加技能支持](client-implementation/adding-skills-support.md)

---

来源: https://github.com/agentskills/agentskills
"""

    (Path(OUTPUT_DIR) / "README.md").write_text(index_content, encoding="utf-8")
    print("\nDone! Docs saved to " + OUTPUT_DIR)


if __name__ == "__main__":
    main()
