import os, re

base_dir = r"c:\Users\USER\geinei_clean"

files_to_update = {
    "zh-cn/index.html": {"text": "了解更多 ➔"},
    "jp/index.html": {"text": "詳しくはこちら ➔"},
    "de/index.html": {"text": "Mehr erfahren ➔"}
}

slide_links = [
    "capabilities.html",
    "solutions.html",
    "case-studies.html"
]

for rel_path, config in files_to_update.items():
    filepath = os.path.join(base_dir, rel_path.replace('/', os.sep))
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = re.compile(r'(<div class="text-carousel-slide.*?)(</p>)', re.DOTALL | re.IGNORECASE)
    
    def repl(match):
        # Only inject in the first 3 match groups
        idx = getattr(repl, 'counter', 0)
        
        # In case there are more than 3, just return original to be safe
        if idx >= 3:
            return match.group(0)
            
        link = slide_links[idx]
        text = config["text"]
        
        # Check if already injected
        if "了解更多" in match.group(0) or "link" in match.group(0) or 'href="' in match.group(0):
            # Already has a link somewhere inside this block maybe
            pass
            
        anchor = f'\n                            <a href="{link}" style="display: inline-block; margin-top: 15px; color: #C5A059; font-weight: 600; font-size: 16px; text-decoration: none; transition: opacity 0.3s;" onmouseover="this.style.opacity=0.8" onmouseout="this.style.opacity=1">{text}</a>'
        
        repl.counter += 1
        return match.group(1) + match.group(2) + anchor
    
    repl.counter = 0
    new_content = pattern.sub(repl, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated {filepath} with {repl.counter} slides.")
