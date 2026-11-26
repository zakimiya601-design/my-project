"""index.html から claude.ai に公開する版 (doctype/head なし) を作る。
使い方: python3 tools/build-artifact.py <出力パス>"""
import re, sys
s = open("index.html", encoding="utf-8").read()
title = re.search(r"<title>.*?</title>", s).group(0)
style = re.search(r"<style>.*?</style>", s, re.S).group(0)
body = re.search(r"<body>\n(.*)</body>", s, re.S).group(1)
out = f'{title}\n<meta name="claude:viewport-fit-sides" content="cover">\n{style}\n{body}'
open(sys.argv[1], "w", encoding="utf-8").write(out)
