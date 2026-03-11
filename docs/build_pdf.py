#!/usr/bin/env python3
"""
将 docs/课题进展报告.md 编译为 PDF
用法: python3 docs/build_pdf.py
"""
import sys
import os
from pathlib import Path

DOCS_DIR = Path(__file__).parent
MD_FILE = DOCS_DIR / "课题进展报告.md"
PDF_FILE = DOCS_DIR / "课题进展报告.pdf"

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC&display=swap');

body {
    font-family: "Noto Serif SC", "WenQuanYi Micro Hei", "Source Han Sans CN",
                 "PingFang SC", "Microsoft YaHei", sans-serif;
    font-size: 13px;
    line-height: 1.8;
    color: #1a1a1a;
    margin: 0;
    padding: 0;
}
@page {
    size: A4;
    margin: 2.5cm 2.8cm 2.5cm 2.8cm;
    @bottom-center {
        content: counter(page) " / " counter(pages);
        font-size: 10px;
        color: #888;
    }
}
h1 {
    font-size: 22px;
    text-align: center;
    border-bottom: 2px solid #2c3e50;
    padding-bottom: 10px;
    margin-bottom: 24px;
    color: #1a1a2e;
}
h2 {
    font-size: 16px;
    color: #1a3a5c;
    border-left: 4px solid #2980b9;
    padding-left: 10px;
    margin-top: 28px;
    margin-bottom: 12px;
}
h3 {
    font-size: 14px;
    color: #2c3e50;
    margin-top: 18px;
    margin-bottom: 8px;
}
h4 {
    font-size: 13px;
    color: #34495e;
    margin-top: 12px;
    margin-bottom: 6px;
}
p {
    margin: 6px 0 10px 0;
    text-indent: 2em;
}
li {
    margin: 4px 0;
}
ul, ol {
    padding-left: 2em;
    margin: 6px 0;
}
strong {
    color: #2c3e50;
}
code {
    background: #f4f4f4;
    border-radius: 3px;
    padding: 1px 4px;
    font-family: monospace;
    font-size: 12px;
}
pre {
    background: #f8f8f8;
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 10px;
    font-size: 11px;
    white-space: pre-wrap;
    word-break: break-all;
}
blockquote {
    border-left: 3px solid #bbb;
    margin: 10px 0;
    padding: 4px 12px;
    color: #555;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin: 10px 0;
}
th, td {
    border: 1px solid #ccc;
    padding: 6px 10px;
    text-align: left;
}
th {
    background: #eaf2fb;
}
img {
    max-width: 100%;
    display: block;
    margin: 10px auto;
}
hr {
    border: none;
    border-top: 1px solid #ccc;
    margin: 20px 0;
}
"""


def build():
    try:
        import markdown
        from weasyprint import HTML, CSS as WeasyprintCSS
    except ImportError as e:
        print(f"缺少依赖，请执行: pip install markdown weasyprint\n{e}")
        sys.exit(1)

    print(f"读取: {MD_FILE}")
    md_text = MD_FILE.read_text(encoding="utf-8")

    # 图片路径转为绝对路径（weasyprint 需要）
    base_url = DOCS_DIR.as_uri() + "/"

    html_body = markdown.markdown(
        md_text,
        extensions=["extra", "toc", "tables", "fenced_code"],
    )
    html_full = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="utf-8"/></head>
<body>{html_body}</body>
</html>"""

    print(f"编译 PDF: {PDF_FILE}")
    HTML(string=html_full, base_url=base_url).write_pdf(
        str(PDF_FILE),
        stylesheets=[WeasyprintCSS(string=CSS)],
    )
    print(f"完成: {PDF_FILE}")


if __name__ == "__main__":
    build()
