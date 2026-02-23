"""
Fix GA and Clarity tracking codes to only run on yehsheng.com
Handles ALL formatting variations using line-by-line replacement.
"""
import os
import re

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

NEW_TRACKING = '''    <!-- Google Analytics & Clarity (production only) -->
    <script>
        if (window.location.hostname === 'yehsheng.com') {
            var gaScript = document.createElement('script');
            gaScript.async = true;
            gaScript.src = 'https://www.googletagmanager.com/gtag/js?id=G-XS5ZTZGF2Y';
            document.head.appendChild(gaScript);
            window.dataLayer = window.dataLayer || [];
            function gtag() { dataLayer.push(arguments); }
            gtag('js', new Date());
            gtag('config', 'G-XS5ZTZGF2Y');
            (function (c, l, a, r, i, t, y) {
                c[a] = c[a] || function () { (c[a].q = c[a].q || []).push(arguments) };
                t = l.createElement(r); t.async = 1; t.src = "https://www.clarity.ms/tag/" + i;
                y = l.getElementsByTagName(r)[0]; y.parentNode.insertBefore(t, y);
            })(window, document, "clarity", "script", "q46c2dab8f");
        }
    </script>'''

count = 0
skipped = 0
warnings = []

for root, dirs, files in os.walk(ROOT_DIR):
    dirs[:] = [d for d in dirs if d not in ['.git', '.github', '.vscode', 'images', 'images_backup', 'assets']]
    for fname in files:
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(root, fname)
        rel = os.path.relpath(fpath, ROOT_DIR)
        
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already updated
        if "window.location.hostname === 'yehsheng.com'" in content:
            skipped += 1
            continue
        
        # Skip if no GA code at all
        if 'G-XS5ZTZGF2Y' not in content:
            continue
        
        lines = content.split('\n')
        
        # Find the start line (GA script tag or GA comment)
        start_idx = None
        end_idx = None
        
        for i, line in enumerate(lines):
            stripped = line.strip()
            # Find start: either the comment or the script tag
            if start_idx is None:
                if 'googletagmanager.com/gtag/js?id=G-XS5ZTZGF2Y' in stripped:
                    # Check if previous line is a comment
                    if i > 0 and ('Google Analytics' in lines[i-1] or 'Google tag' in lines[i-1]):
                        start_idx = i - 1
                    else:
                        start_idx = i
            
            # Find end: closing </script> after clarity code
            if start_idx is not None and end_idx is None:
                if 'q46c2dab8f' in stripped:
                    # Find the next </script> after this line
                    for j in range(i, min(i + 5, len(lines))):
                        if '</script>' in lines[j]:
                            end_idx = j
                            break
                    if end_idx is None:
                        # clarity and </script> on same line
                        end_idx = i
        
        if start_idx is not None and end_idx is not None:
            # Get the content before the GA block
            before = lines[:start_idx]
            after = lines[end_idx + 1:]
            
            new_lines = before + [NEW_TRACKING] + after
            new_content = '\n'.join(new_lines)
            
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  UPDATED: {rel} (lines {start_idx+1}-{end_idx+1})")
            count += 1
        else:
            warnings.append(f"{rel} (start={start_idx}, end={end_idx})")
            print(f"  WARNING: {rel} - start={start_idx}, end={end_idx}")

print(f"\n=== Summary ===")
print(f"Updated: {count}")
print(f"Skipped (already done): {skipped}")
if warnings:
    print(f"Warnings: {len(warnings)}")
    for w in warnings:
        print(f"  - {w}")
