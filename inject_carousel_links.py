import os
import re

base_dir = r"c:\Users\USER\geinei_clean"

files_to_update = {
    "index.html": {"text": "Learn More ➔"},
    "zh/index.html": {"text": "了解更多 ➔"},
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

    # We need to find the three slides. They are marked by 
    # <!-- Slide 1 -->
    # <div class="text-carousel-slide active"> ... </p> ... </div>
    # Let's split by <!-- Slide and inject the link right before the closing </div> of that slide
    
    # regex to find Slide 1, 2, 3 block
    for i in range(1, 4):
        slide_marker = f"<!-- Slide {i} -->"
        if slide_marker not in content:
            print(f"Could not find {slide_marker} in {filepath}")
            continue
            
        link = slide_links[i-1]
        text = config["text"]
        
        # We find the next </p> after the slide marker, and insert the <a> tag after it.
        # This is safer than replacing the closing </div> because there might be multiple nested </div>s.
        
        pattern = re.compile(rf"({slide_marker}.*?</p>\s*)", re.DOTALL)
        match = pattern.search(content)
        
        if match:
            # check if our link is already injected
            if f'href="{link}"' not in match.group(0) and "margin-top" not in match.group(0):
                replacement = match.group(1) + f'<a href="{link}" style="display: inline-block; margin-top: 15px; color: #C5A059; font-weight: 600; font-size: 16px; text-decoration: none; transition: opacity 0.3s;" onmouseover="this.style.opacity=0.8" onmouseout="this.style.opacity=1">{text}</a>\n'
                content = content[:match.start()] + replacement + content[match.end():]
                print(f"Updated Slide {i} in {filepath}")
            else:
                print(f"Slide {i} in {filepath} might already have a link.")
        else:
            print(f"Could not find </p> after {slide_marker} in {filepath}")
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
