#!/usr/bin/env python3
"""Agent Skills 文档爬虫 - 从 agentskills.io 获取文档"""

import os
import shutil
import requests
from pathlib import Path
from bs4 import BeautifulSoup

BASE_URL = "https://agentskills.io"
OUTPUT_DIR = "assets/library/assets/agentskills"

PAGES = [
    ("home", "/home"),
    ("what-are-skills", "/what-are-skills"),
    ("specification", "/specification"),
    ("clients", "/clients"),
    ("skill-creation-quickstart", "/skill-creation/quickstart"),
    ("skill-creation-best-practices", "/skill-creation/best-practices"),
    (
        "skill-creation-optimizing-descriptions",
        "/skill-creation/optimizing-descriptions",
    ),
    ("skill-creation-evaluating-skills", "/skill-creation/evaluating-skills"),
    ("skill-creation-using-scripts", "/skill-creation/using-scripts"),
    (
        "client-implementation-adding-skills-support",
        "/client-implementation/adding-skills-support",
    ),
]


def fetch_page(path: str) -> str:
    url = BASE_URL + path
    print(f"Fetching: {url}")
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.text


def extract_content(html: str, page_name: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    main_content = soup.find("main")
    if not main_content:
        return ""

    title = soup.find("title")
    title_text = (
        title.get_text(strip=True) if title else page_name.replace("-", " ").title()
    )

    article = main_content.find("article")
    if article:
        content = article
    else:
        content = main_content

    for tag in content.find_all(
        ["script", "style", "nav", "header", "footer", "aside"]
    ):
        tag.decompose()

    markdown = f"# {title_text}\n\n"

    for p in content.find_all(
        [
            "p",
            "h1",
            "h2",
            "h3",
            "h4",
            "h5",
            "h6",
            "ul",
            "ol",
            "pre",
            "code",
            "blockquote",
        ]
    ):
        if p.name == "p":
            text = p.get_text(strip=True)
            if text:
                markdown += text + "\n\n"
        elif p.name.startswith("h"):
            level = int(p.name[1])
            markdown += "#" * level + " " + p.get_text(strip=True) + "\n\n"
        elif p.name in ["ul", "ol"]:
            for li in p.find_all("li", recursive=False):
                markdown += "- " + li.get_text(strip=True).replace("\n", " ") + "\n"
            markdown += "\n"
        elif p.name == "pre":
            code = p.get_text(strip=True)
            markdown += f"```\n{code}\n```\n\n"
        elif p.name == "blockquote":
            markdown += "> " + p.get_text(strip=True) + "\n\n"

    return markdown


def main():
    print("Scraping Agent Skills documentation...")

    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)

    for filename, path in PAGES:
        try:
            html = fetch_page(path)
            content = extract_content(html, filename)

            output_file = Path(OUTPUT_DIR) / f"{filename}.md"
            output_file.write_text(content, encoding="utf-8")
            print(f"Saved: {output_file}")
        except Exception as e:
            print(f"Error fetching {path}: {e}")

    index_content = "# Agent Skills\n\n## 文档目录\n\n"
    for filename, path in PAGES:
        title = filename.replace("-", " ").title()
        index_content += f"- [{title}]({filename}.md)\n"

    (Path(OUTPUT_DIR) / "README.md").write_text(index_content, encoding="utf-8")
    print("\nDone! Docs saved to " + OUTPUT_DIR)


if __name__ == "__main__":
    main()
