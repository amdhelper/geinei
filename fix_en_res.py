import os

files = ['resource-process.html', 'resource-design.html', 'resource-materials.html', 'resource-quality.html', 'resource-faq.html']

en_sidebar = """<aside class="resource-sidebar">
    <div class="sidebar-title">📋 Quick Navigation</div>
    <ul class="sidebar-nav">
        <li><a href="case-studies.html">📋 Case Studies</a></li>
        <li><a href="resource-process.html#process-guide">🔄 Process Selection</a></li>
        <li><a href="resource-design.html#gear-types">⚙️ Gear Guide</a></li>
        <li class="sub-item"><a href="resource-design.html#spur-helical">• Spur/Helical</a></li>
        <li class="sub-item"><a href="resource-design.html#bevel-worm">• Bevel/Worm</a></li>
        <li class="sub-item"><a href="resource-design.html#planetary">• Planetary/Harmonic</a></li>
        <li><a href="resource-design.html#bearings-guide">🔩 Self-Lubricating Bearings</a></li>
        <li><a href="resource-materials.html#sintering-guide">🔥 Sintering Process</a></li>
        <li><a href="resource-materials.html#powder-production">🔬 Powder Production</a></li>
        <li><a href="resource-quality.html#quality-control">📊 Quality Control</a></li>
        <li><a href="resource-materials.html#density-porosity">⚡ Density/Porosity</a></li>
        <li><a href="resource-faq.html#faq">❓ FAQ</a></li>
        <li><a href="resource-faq.html#glossary">📖 Glossary</a></li>
        <li><a href="resource-materials.html#materials">🔧 Material Specs</a></li>
    </ul>
</aside>
<div class="resource-content">"""

for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 1. Fix literal \n
        content = content.replace('\\n', '')
        
        # 2. Add sidebar if missing
        if '<aside class="resource-sidebar">' not in content:
            if '<div class="resource-layout">' in content:
                content = content.replace('<div class="resource-layout">', f'<div class="resource-layout">\n{en_sidebar}')
                # Close the new <div class="resource-content"> before the closing section tag.
                content = content.replace('</section>', '</div>\n</div>\n</section>')
                
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Fixed {f}")
    except Exception as e:
        print(f"Error {f}: {e}")
