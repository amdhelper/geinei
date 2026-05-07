import os
import re

BASE_DIR = r"c:\Users\USER\geinei_clean"

STATIC_TAGS = """    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XS5ZTZGF2Y"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-XS5ZTZGF2Y');
    </script>
    <!-- Microsoft Clarity -->
    <script type="text/javascript">
        (function(c,l,a,r,i,t,y){
            c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
            t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
            y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
        })(window, document, "clarity", "script", "q46c2dab8f");
    </script>"""

# Match the entire <script> block that contains window.location.hostname and G-XS5ZTZGF2Y
pattern = re.compile(r'<script>\s*if\s*\(\s*window\.location\.hostname[^<]+G-XS5ZTZGF2Y[^<]+</script>', re.DOTALL)

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = pattern.sub(STATIC_TAGS, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

if __name__ == "__main__":
    count = 0
    for root, _, files in os.walk(BASE_DIR):
        if '.git' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                if process_file(os.path.join(root, file)):
                    print(f"Updated {file}")
                    count += 1
    print(f"Total updated: {count}")
