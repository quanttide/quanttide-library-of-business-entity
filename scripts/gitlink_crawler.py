#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GitLink 帮助文档爬虫 - 抓取帮助文档并保存为Markdown格式"""

import os
import re
import sys
import urllib.request
import urllib.parse
from html import unescape
from typing import Dict, List, Tuple

if sys.version_info[0] >= 3:
    import io

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

BASE_URL = "https://help.gitlink.org.cn"
OUTPUT_DIR = "docs/library/assets/gitlink"

NAVIGATION = {
    "快速开始": [
        ("/快速开始/注册GitLink账号", "注册GitLink账号"),
        ("/快速开始/配置SSH密钥", "配置SSH密钥"),
        ("/快速开始/创建代码仓库", "创建代码仓库"),
        ("/快速开始/克隆仓库", "克隆仓库"),
        ("/快速开始/推送代码", "推送代码"),
    ],
    "代码库管理": [
        ("/代码库管理/仓库创建", "仓库创建"),
        ("/代码库管理/仓库设置", "仓库设置"),
        ("/代码库管理/仓库协作", "仓库协作"),
        ("/代码库管理/代码浏览", "代码浏览"),
        ("/代码库管理/分支管理", "分支管理"),
        ("/代码库管理/标签管理", "标签管理"),
        ("/代码库管理/代码统计", "代码统计"),
        ("/代码库管理/代码保护", "代码保护"),
    ],
    "组织管理": [
        ("/组织管理/组织简介", "组织简介"),
        ("/组织管理/创建组织", "创建组织"),
        ("/组织管理/组织成员", "组织成员"),
        ("/组织管理/组织设置", "组织设置"),
        ("/组织管理/组织权限", "组织权限"),
    ],
    "疑修": [
        ("/疑修/疑修简介", "疑修简介"),
        ("/疑修/创建疑修", "创建疑修"),
        ("/疑修/疑修管理", "疑修管理"),
        ("/疑修/疑修标签", "疑修标签"),
        ("/疑修/疑修评论", "疑修评论"),
        ("/疑修/疑修指派", "疑修指派"),
        ("/疑修/疑修关闭", "疑修关闭"),
    ],
    "合并请求": [
        ("/合并请求/合并请求简介", "合并请求简介"),
        ("/合并请求/创建合并请求", "创建合并请求"),
        ("/合并请求/合并请求审核", "合并请求审核"),
        ("/合并请求/合并请求合并", "合并请求合并"),
        ("/合并请求/合并请求冲突", "合并请求冲突"),
    ],
    "DevOps引擎": [
        ("/DevOps引擎/引擎简介", "引擎简介"),
        ("/DevOps引擎/创建流水线", "创建流水线"),
        ("/DevOps引擎/流水线配置", "流水线配置"),
        ("/DevOps引擎/流水线执行", "流水线执行"),
        ("/DevOps引擎/流水线日志", "流水线日志"),
        ("/DevOps引擎/流水线制品", "流水线制品"),
    ],
    "维基": [
        ("/维基/维基页面管理", "维基页面管理"),
        ("/维基/模板导入及导出", "模板导入及导出"),
    ],
    "Bot市场": [
        ("/Bot市场/bot安装", "bot安装"),
        ("/Bot市场/bot配置", "bot配置"),
        ("/Bot市场/bot使用", "bot使用"),
        ("/Bot市场/bot开发", "bot开发"),
    ],
    "第三方服务": [
        ("/第三方服务/跨平台代码同步", "跨平台代码同步"),
        ("/第三方服务/重睛鸟代码溯源", "重睛鸟代码溯源"),
        ("/第三方服务/代码质量分析", "代码质量分析"),
    ],
    "通知": [
        ("/通知/通知简介", "通知简介"),
        ("/通知/通知设置", "通知设置"),
    ],
    "个人主页建站": [
        ("/个人主页建站/站点创建流程", "站点创建流程"),
        ("/个人主页建站/站点配置", "站点配置"),
        ("/个人主页建站/站点发布", "站点发布"),
    ],
}


def fetch_page(url: str) -> str:
    """获取页面内容"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return response.read().decode("utf-8")
    except Exception as e:
        print(f"Error fetching {url}: {e}", file=sys.stderr)
        raise


def extract_content(html: str) -> str:
    """从HTML中提取主要内容并转换为Markdown"""
    content = html

    content = re.sub(r"<script[^>]*>.*?</script>", "", content, flags=re.DOTALL)
    content = re.sub(r"<style[^>]*>.*?</style>", "", content, flags=re.DOTALL)

    article_match = re.search(r"<article[^>]*>(.*?)</article>", content, re.DOTALL)
    if article_match:
        content = article_match.group(1)

    theme_doc_match = re.search(
        r'<div class="theme-doc-markdown markdown">(.*?)</div>\s*<footer',
        content,
        re.DOTALL,
    )
    if theme_doc_match:
        content = theme_doc_match.group(1)

    content = re.sub(r"<nav[^>]*>.*?</nav>", "", content, re.DOTALL)
    content = re.sub(r"<aside[^>]*>.*?</aside>", "", content, re.DOTALL)
    content = re.sub(r"<header[^>]*>.*?</header>", "", content, re.DOTALL)
    content = re.sub(r"<footer[^>]*>.*?</footer>", "", content, re.DOTALL)

    content = re.sub(
        r'<span class="theme-doc-version-badge[^>]*>[^<]*</span>', "", content
    )
    content = re.sub(
        r'<span class="breadcrumbs[^>]*>.*?</span>', "", content, re.DOTALL
    )

    content = re.sub(
        r'<a[^>]*class="[^"]*pagination-nav[^"]*"[^>]*>.*?</a>', "", content, re.DOTALL
    )
    content = re.sub(
        r'<a[^>]*class="[^"]*theme-edit-this-page[^"]*"[^>]*>.*?</a>',
        "",
        content,
        re.DOTALL,
    )
    content = re.sub(r'<a[^>]*class="[^"]*card[^"]*"[^>]*>', "", content, re.DOTALL)
    content = re.sub(r"</a>", "", content)

    content = re.sub(r'class="[^"]*"', "", content)
    content = re.sub(r'id="[^"]*"', "", content)
    content = re.sub(r'data-[^"]*="[^"]*"', "", content)

    content = re.sub(r"<h1[^>]*>(.*?)</h1>", r"\n# \1\n", content, flags=re.DOTALL)
    content = re.sub(r"<h2[^>]*>(.*?)</h2>", r"\n## \1\n", content, flags=re.DOTALL)
    content = re.sub(r"<h3[^>]*>(.*?)</h3>", r"\n### \1\n", content, flags=re.DOTALL)
    content = re.sub(r"<h4[^>]*>(.*?)</h4>", r"\n#### \1\n", content, flags=re.DOTALL)
    content = re.sub(r"<h5[^>]*>(.*?)</h5>", r"\n##### \1\n", content, flags=re.DOTALL)
    content = re.sub(r"<h6[^>]*>(.*?)</h6>", r"\n###### \1\n", content, flags=re.DOTALL)

    content = re.sub(r"<strong>(.*?)</strong>", r"**\1**", content, flags=re.DOTALL)
    content = re.sub(r"<b>(.*?)</b>", r"**\1**", content, flags=re.DOTALL)
    content = re.sub(r"<em>(.*?)</em>", r"*\1*", content, flags=re.DOTALL)
    content = re.sub(r"<i>(.*?)</i>", r"*\1*", content, flags=re.DOTALL)

    content = re.sub(r"<code>(.*?)</code>", r"`\1`", content, flags=re.DOTALL)
    content = re.sub(r"<code[^>]*>(.*?)</code>", r"`\1`", content, flags=re.DOTALL)
    content = re.sub(
        r"<pre[^>]*><code>(.*?)</code></pre>",
        r"\n```\n\1\n```\n",
        content,
        flags=re.DOTALL,
    )

    content = re.sub(
        r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r"[\2](\1)", content, flags=re.DOTALL
    )

    content = re.sub(
        r'<img[^>]*src="([^"]*)"[^>]*alt="([^"]*)"[^>]*>',
        r"![\2](\1)",
        content,
        flags=re.DOTALL,
    )
    content = re.sub(
        r'<img[^>]*src="([^"]*)"[^>]*>', r"![](https://help.gitlink.org.cn\1)", content
    )

    content = re.sub(r"<ul[^>]*>", r"\n", content, flags=re.DOTALL)
    content = re.sub(r"</ul>", r"\n", content)
    content = re.sub(r"<ol[^>]*>", r"\n", content, flags=re.DOTALL)
    content = re.sub(r"</ol>", r"\n", content)
    content = re.sub(r"<li[^>]*>(.*?)</li>", r"- \1\n", content, flags=re.DOTALL)

    content = re.sub(r"<p[^>]*>(.*?)</p>", r"\n\1\n\n", content, flags=re.DOTALL)
    content = re.sub(r"<br\s*/?>", r"\n", content, flags=re.IGNORECASE)

    content = re.sub(r"<div[^>]*>(.*?)</div>", r"\n\1\n", content, flags=re.DOTALL)
    content = re.sub(r"<span[^>]*>(.*?)</span>", r"\1", content, flags=re.DOTALL)
    content = re.sub(
        r"<section[^>]*>(.*?)</section>", r"\n\1\n", content, flags=re.DOTALL
    )

    content = re.sub(r"<[^>]+>", "", content)
    content = re.sub(r"/>", "", content)

    content = re.sub(
        r"\[([^\]]+)\]\((/[^)]+)\)", r"[\1](https://help.gitlink.org.cn\2)", content
    )

    content = unescape(content)

    content = re.sub(r"\n{3,}", r"\n\n", content)

    if (
        "关于GitLink" in content
        and "快速开始" in content
        and "帮助文档有助于您全面了解GitLink平台" in content
    ):
        return "[PAGE_REDIRECTED_TO_INTRO]"

    lines = content.split("\n")
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        if line:
            cleaned_lines.append(line)
    content = "\n".join(cleaned_lines)

    return content.strip()


def fetch_sitemap_urls() -> Dict[str, List[Tuple[str, str]]]:
    """从sitemap.xml获取有效的URL列表"""
    print("Fetching sitemap...")
    sitemap_url = BASE_URL + "/sitemap.xml"
    html = fetch_page(sitemap_url)

    urls = re.findall(r"<loc>([^<]+)</loc>", html)

    nav = {}
    for url in urls:
        if "/next/" in url:
            continue
        if url in [
            "https://help.gitlink.org.cn/",
            "https://help.gitlink.org.cn/search",
        ]:
            continue

        path = url.replace("https://help.gitlink.org.cn", "")

        if path.startswith("/Bot") and "/" in path:
            category = "Bot市场"
            title = urllib.parse.unquote(path.split("/")[-1])
        elif path.startswith("/DevOps") and "/" in path:
            category = "DevOps引擎"
            title = urllib.parse.unquote(path.split("/")[-1])
        elif path.startswith("/代码库管理") and "/" in path:
            category = "代码库管理"
            title = urllib.parse.unquote(path.split("/")[-1])
        elif path.startswith("/组织管理") and "/" in path:
            category = "组织管理"
            title = urllib.parse.unquote(path.split("/")[-1])
        elif path.startswith("/疑修") and "/" in path:
            category = "疑修"
            title = urllib.parse.unquote(path.split("/")[-1])
        elif path.startswith("/合并请求") and "/" in path:
            category = "合并请求"
            title = urllib.parse.unquote(path.split("/")[-1])
        elif path.startswith("/维基") and "/" in path:
            category = "维基"
            title = urllib.parse.unquote(path.split("/")[-1])
        elif path.startswith("/第三方服务") and "/" in path:
            category = "第三方服务"
            title = urllib.parse.unquote(path.split("/")[-1])
        elif path.startswith("/通知") and "/" in path:
            category = "通知"
            title = urllib.parse.unquote(path.split("/")[-1])
        elif path.startswith("/个人主页建站") and "/" in path:
            category = "个人主页建站"
            title = urllib.parse.unquote(path.split("/")[-1])
        elif path.startswith("/快速开始") and "/" in path:
            category = "快速开始"
            title = urllib.parse.unquote(path.split("/")[-1])
        else:
            continue

        if category not in nav:
            nav[category] = []
        nav[category].append((path, title))

    for category in nav:
        nav[category].sort(key=lambda x: x[1])

    print(
        "Found "
        + str(sum(len(v) for v in nav.values()))
        + " pages in "
        + str(len(nav))
        + " categories"
    )
    return nav


def get_category_page_urls() -> Dict[str, List[Tuple[str, str]]]:
    """获取所有分类页面的URL"""
    return fetch_sitemap_urls()


def save_markdown(category: str, title: str, content: str):
    """Save Markdown file"""
    category_dir = os.path.join(OUTPUT_DIR, category)
    os.makedirs(category_dir, exist_ok=True)

    filename = title + ".md"
    filepath = os.path.join(category_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print("Saved: " + filepath)


def create_index():
    """Create index file"""
    index_content = "# GitLink Help Docs\n\nOffline version of GitLink help documentation.\n\n## Table of Contents\n\n"

    for category, pages in NAVIGATION.items():
        index_content += "### " + category + "\n\n"
        for _, title in pages:
            index_content += "- [" + title + "](" + category + "/" + title + ".md)\n"
        index_content += "\n"

    index_path = os.path.join(OUTPUT_DIR, "README.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_content)

    print("Created index: " + index_path)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Starting to crawl GitLink help docs...")

    all_pages = []
    for category, pages in NAVIGATION.items():
        for path, title in pages:
            all_pages.append((category, path, title))

    total = len(all_pages)
    for idx, (category, path, title) in enumerate(all_pages, 1):
        encoded_path = urllib.parse.quote(path, safe="/")
        url = BASE_URL + encoded_path
        print("[" + str(idx) + "/" + str(total) + "] Fetching: " + title + "...")

        try:
            html = fetch_page(url)
            content = extract_content(html)

            if content == "[PAGE_REDIRECTED_TO_INTRO]":
                print("  WARNING: Page redirected to intro, skipping...")
                continue

            full_content = "# " + title + "\n\n" + content

            save_markdown(category, title, full_content)

        except Exception as e:
            err_msg = "  Error: " + str(e)
            print(err_msg)
            save_markdown(
                category, title, "# " + title + "\n\nUnable to fetch content: " + str(e)
            )

    create_index()

    print("\nDone! All docs saved to docs/library/assets/gitlink/")


if __name__ == "__main__":
    main()
