import re
path = r"c:\Users\USER\geinei_clean\solutions.html"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()
    heading_re = re.compile(r'<(h[1-6])[^>]*>(.*?)</h\1>', re.IGNORECASE | re.DOTALL)
    matches = heading_re.findall(content)
    print(f"Total headings found: {len(matches)}")
    for tag, inner in matches[:10]:
        print(f"[{tag}]: {inner.strip()}")
        if '&' in inner:
            print("  -> Contains ampersand!")
