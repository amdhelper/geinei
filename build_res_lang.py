import os
import re

languages = {
    'zh': {
        'title': '技術資源',
        'subtitle': '知識庫與常見問題。探索粉末冶金的製程選擇、材料規格與設計指南。',
        'c1_tag': '比較與選擇', 'c1_title': '製程選擇指南', 'c1_desc': 'PM 與 CNC 加工及鑄造之比較。了解各種成型方式（如壓製燒結、MIM、鍛造等）。',
        'c2_tag': '工程設計', 'c2_title': '設計與齒輪指南', 'c2_desc': '完整的齒輪類型指南、粉末冶金設計建議及自潤軸承應用。',
        'c3_tag': '規格與處理', 'c3_title': '材料規格', 'c3_desc': '鐵、鋼、銅及不鏽鋼規格。包含密度、孔隙率、表面處理與粉末生產細節。',
        'c4_tag': '檢驗', 'c4_title': '品質控制', 'c4_desc': '我們確保精密度的系統化方法，包含CMM、光學檢驗與材料測試。',
        'c5_tag': '知識庫', 'c5_title': '常見問題與詞彙表', 'c5_desc': '解答關於PM強度與成本的常見疑問，並提供詳盡的產業專有名詞解釋。',
        'explore': '探索 →'
    },
    'zh-cn': {
        'title': '技术资源',
        'subtitle': '知识库与常见问题。探索粉末冶金的制程选择、材料规格与设计指南。',
        'c1_tag': '比较与选择', 'c1_title': '制程选择指南', 'c1_desc': 'PM 与 CNC 加工及铸造之比较。了解各种成型方式（如压制烧结、MIM、锻造等）。',
        'c2_tag': '工程设计', 'c2_title': '设计与齿轮指南', 'c2_desc': '完整的齿轮类型指南、粉末冶金设计建议及自润轴承应用。',
        'c3_tag': '规格与处理', 'c3_title': '材料规格', 'c3_desc': '铁、钢、铜及不锈钢规格。包含密度、孔隙率、表面处理与粉末生产细节。',
        'c4_tag': '检验', 'c4_title': '品质控制', 'c4_desc': '我们确保精密度的系统化方法，包含CMM、光学检验与材料测试。',
        'c5_tag': '知识库', 'c5_title': '常见问题与词汇表', 'c5_desc': '解答关于PM强度与成本的常见疑问，并提供详尽的产业专有名词解释。',
        'explore': '探索 →'
    },
    'de': {
        'title': 'Technische Ressourcen',
        'subtitle': 'Wissensdatenbank & FAQ. Entdecken Sie häufige Fragen, Materialspezifikationen und Konstruktionsrichtlinien für die Pulvermetallurgie.',
        'c1_tag': 'Vergleich & Auswahl', 'c1_title': 'Leitfaden zur Verfahrensauswahl', 'c1_desc': 'PM vs. CNC vs. Guss. Erfahren Sie mehr über verschiedene Umformmethoden.',
        'c2_tag': 'Technik', 'c2_title': 'Konstruktion & Zahnrad-Guides', 'c2_desc': 'Umfassender Leitfaden zu Zahnradarten, PM-gerechter Konstruktion und Sinterlagern.',
        'c3_tag': 'Spezifikationen', 'c3_title': 'Materialspezifikationen', 'c3_desc': 'Eisen, Stahl, Messing und Edelstahl. Details zu Dichte, Porosität und Oberflächenbehandlung.',
        'c4_tag': 'Inspektion', 'c4_title': 'Qualitätskontrolle', 'c4_desc': 'Unser systematischer Ansatz zur Gewährleistung von Präzision.',
        'c5_tag': 'Wissensdatenbank', 'c5_title': 'FAQ & Glossar', 'c5_desc': 'Antworten auf häufige Fragen zu PM-Festigkeit und -Kosten.',
        'explore': 'Entdecken →'
    },
    'jp': {
        'title': '技術リソース',
        'subtitle': 'ナレッジベース＆FAQ。粉末冶金のプロセス選択、材料仕様、設計ガイドをご覧ください。',
        'c1_tag': '比較と選択', 'c1_title': 'プロセス選択ガイド', 'c1_desc': 'PMとCNC加工、鋳造の比較。プレス＆焼結、MIMなどの成形方法について。',
        'c2_tag': 'エンジニアリング', 'c2_title': '設計＆歯車ガイド', 'c2_desc': '歯車の種類、PM用の設計、含油軸受の用途に関する完全ガイド。',
        'c3_tag': '仕様と処理', 'c3_title': '材料仕様', 'c3_desc': '鉄、鋼、真鍮、ステンレス。密度、気孔率、表面処理に関する詳細。',
        'c4_tag': '検査', 'c4_title': '品質管理', 'c4_desc': '精度を確保するためのCMMや材料試験などの体系的なアプローチ。',
        'c5_tag': 'ナレッジベース', 'c5_title': 'FAQ & 用語集', 'c5_desc': 'PMの強度やコストに関するよくある質問と、専門用語の包括的な用語集。',
        'explore': '見る →'
    }
}

top_level_ids = [
    'process-guide', 'gear-types', 'forming-methods', 'pm-vs-cnc',
    'surface-treatment', 'design-guide', 'bearings-guide', 'sintering-guide',
    'powder-production', 'quality-control', 'density-porosity', 'faq',
    'glossary', 'materials'
]

file_map = {
    'process-guide': 'resource-process.html',
    'forming-methods': 'resource-process.html',
    'pm-vs-cnc': 'resource-process.html',
    'gear-types': 'resource-design.html',
    'design-guide': 'resource-design.html',
    'bearings-guide': 'resource-design.html',
    'materials': 'resource-materials.html',
    'surface-treatment': 'resource-materials.html',
    'density-porosity': 'resource-materials.html',
    'sintering-guide': 'resource-materials.html',
    'powder-production': 'resource-materials.html',
    'quality-control': 'resource-quality.html',
    'faq': 'resource-faq.html',
    'glossary': 'resource-faq.html'
}

sub_item_map = {
    'spur-helical': 'resource-design.html',
    'bevel-worm': 'resource-design.html',
    'planetary': 'resource-design.html',
    'press-sinter': 'resource-process.html',
    'mim': 'resource-process.html',
    'hip-forging': 'resource-process.html',
    'iron-steel': 'resource-materials.html',
    'stainless': 'resource-materials.html',
    'magnetic': 'resource-materials.html',
    'bronze-brass': 'resource-materials.html'
}

def extract_block(full_html, block_id):
    start_str = f'<div id=\"{block_id}\"'
    start_idx = full_html.find(start_str)
    if start_idx == -1:
        return ""
        
    comment_search = full_html.rfind('<!--', 0, start_idx)
    if comment_search != -1 and full_html[comment_search:start_idx].strip().startswith('<!--'):
        actual_start = comment_search
    else:
        actual_start = start_idx

    end_idx = start_idx
    div_count = 0
    in_block = False
    
    i = start_idx
    while i < len(full_html):
        if full_html[i:i+4] == '<div':
            div_count += 1
            in_block = True
            i += 4
            continue
        if full_html[i:i+5] == '</div':
            div_count -= 1
            i += 5
            if in_block and div_count == 0:
                end_idx = i + 1
                while end_idx < len(full_html) and full_html[end_idx-1] != '>':
                    end_idx += 1
                break
            continue
        i += 1
        
    return full_html[actual_start:end_idx]


for lang, texts in languages.items():
    html_path = os.path.join(lang, 'resources.html')
    if not os.path.exists(html_path):
        continue
        
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    file_content = {k: '' for k in set(file_map.values())}
    
    layout_start_match = re.search(r'(.*?<div class=\"resource-layout\">)', html, re.IGNORECASE | re.DOTALL)
    top_part = layout_start_match.group(1) if layout_start_match else ''

    aside_match = re.search(r'(<aside class=\"resource-sidebar\">.*?<\/aside>.*?<div class=\"resource-content\">)', html, re.IGNORECASE | re.DOTALL)
    aside_part = aside_match.group(1) if aside_match else ''

    # Robust footer matching
    end_pattern = re.compile(r'(<\/div>\s*(<!--\s*End resource-content\s*-->)?\s*<\/div>\s*(<!--\s*End resource-layout\s*-->)?\s*(<\/div>\s*)?<\/section>.*?<\/html>)', re.IGNORECASE | re.DOTALL)
    m = end_pattern.search(html)
    if m:
        footer_part = m.group(1)
    else:
        print(f"[{lang}] Could not find footer part!")
        footer_part = ''

    content_start = html.find('<div class=\"resource-content\">') + len('<div class=\"resource-content\">')
    content_end = html.find('</div>\n            </div>\n        </section>\n\n        <!-- Footer -->')
    if content_end == -1:
        content_end = html.find('<!-- Smooth Scroll JavaScript -->')
    if content_end == -1:
        content_end = html.find('<!-- Footer -->')
    if content_end == -1:
        content_end = html.find('</section>')
        
    content_area = html[content_start:content_end]

    for tid in top_level_ids:
        block_html = extract_block(content_area, tid)
        if block_html:
            file_content[file_map[tid]] += '\n' + block_html + '\n'
        else:
            print(f"[{lang}] Failed to find {tid}")

    # Update sidebar links
    new_aside = aside_part
    for tid, filename in file_map.items():
        new_aside = re.sub(f'href=\"#({tid})\"', f'href=\"{filename}#\\1\"', new_aside)

    for div_id, filename in sub_item_map.items():
        new_aside = re.sub(f'href=\"#({div_id})\"', f'href=\"{filename}#\\1\"', new_aside)

    # Need to update paths to root images in detail pages and index page
    # In translated root, images are in `../images/`
    for filename, content in file_content.items():
        out_html = top_part + new_aside + content + footer_part
        out_path = os.path.join(lang, filename)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(out_html)

    print(f"[{lang}] Generated 5 detail pages")

    nav_end_match = re.search(r'(.*?<\/nav>)', html, re.IGNORECASE | re.DOTALL)
    nav_part = nav_end_match.group(1) if nav_end_match else top_part

    cards_html = nav_part + f'''
    <!-- Hero Section -->
    <section style=\"background: linear-gradient(135deg, #002FA7 0%, #001a6e 100%); padding: 80px 0; text-align: center;\">
        <div class=\"container\">
            <h1 style=\"font-family: 'Playfair Display', serif; font-size: 48px; font-weight: 700; color: white; margin-bottom: 20px;\">
                {texts["title"]}
            </h1>
            <p style=\"font-size: 20px; color: #a0b0d0; max-width: 700px; margin: 0 auto; line-height: 1.6;\">
                {texts["subtitle"]}
            </p>
        </div>
    </section>

    <!-- Resources Grid -->
    <section style=\"padding: 80px 0; background: #f8f9fa;\">
        <div class=\"container\">
            <div style=\"display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 40px;\">

                <!-- Card 1: Process -->
                <a href=\"resource-process.html\" class=\"case-card-link\" style=\"display: block; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); transition: transform 0.3s ease; text-decoration: none; color: inherit;\">
                    <div style=\"height: 200px; background-image: url('../images/thumb_res_process.png'); background-size: cover; background-position: center; border-bottom: 3px solid #C5A059;\"></div>
                    <div style=\"padding: 30px;\">
                        <span style=\"display: inline-block; background: #f0f4f8; color: #002FA7; padding: 4px 10px; border-radius: 4px; font-size: 11px; font-weight: 600; text-transform: uppercase; margin-bottom: 15px;\">{texts["c1_tag"]}</span>
                        <h3 style=\"font-family: 'Playfair Display', serif; font-size: 22px; font-weight: 700; color: #111; margin-bottom: 15px; line-height: 1.3;\">{texts["c1_title"]}</h3>
                        <p style=\"font-size: 15px; color: #666; line-height: 1.6; margin-bottom: 20px;\">
                            {texts["c1_desc"]}
                        </p>
                        <span style=\"color: #002FA7; font-weight: 600; font-size: 14px;\">{texts["explore"]}</span>
                    </div>
                </a>

                <!-- Card 2: Design -->
                <a href=\"resource-design.html\" class=\"case-card-link\" style=\"display: block; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); transition: transform 0.3s ease; text-decoration: none; color: inherit;\">
                    <div style=\"height: 200px; background-image: url('../images/thumb_res_design.png'); background-size: cover; background-position: center; border-bottom: 3px solid #C5A059;\"></div>
                    <div style=\"padding: 30px;\">
                        <span style=\"display: inline-block; background: #f0f4f8; color: #002FA7; padding: 4px 10px; border-radius: 4px; font-size: 11px; font-weight: 600; text-transform: uppercase; margin-bottom: 15px;\">{texts["c2_tag"]}</span>
                        <h3 style=\"font-family: 'Playfair Display', serif; font-size: 22px; font-weight: 700; color: #111; margin-bottom: 15px; line-height: 1.3;\">{texts["c2_title"]}</h3>
                        <p style=\"font-size: 15px; color: #666; line-height: 1.6; margin-bottom: 20px;\">
                            {texts["c2_desc"]}
                        </p>
                        <span style=\"color: #002FA7; font-weight: 600; font-size: 14px;\">{texts["explore"]}</span>
                    </div>
                </a>

                <!-- Card 3: Materials -->
                <a href=\"resource-materials.html\" class=\"case-card-link\" style=\"display: block; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); transition: transform 0.3s ease; text-decoration: none; color: inherit;\">
                    <div style=\"height: 200px; background-image: url('../images/thumb_res_material.png'); background-size: cover; background-position: center; border-bottom: 3px solid #C5A059;\"></div>
                    <div style=\"padding: 30px;\">
                        <span style=\"display: inline-block; background: #f0f4f8; color: #002FA7; padding: 4px 10px; border-radius: 4px; font-size: 11px; font-weight: 600; text-transform: uppercase; margin-bottom: 15px;\">{texts["c3_tag"]}</span>
                        <h3 style=\"font-family: 'Playfair Display', serif; font-size: 22px; font-weight: 700; color: #111; margin-bottom: 15px; line-height: 1.3;\">{texts["c3_title"]}</h3>
                        <p style=\"font-size: 15px; color: #666; line-height: 1.6; margin-bottom: 20px;\">
                            {texts["c3_desc"]}
                        </p>
                        <span style=\"color: #002FA7; font-weight: 600; font-size: 14px;\">{texts["explore"]}</span>
                    </div>
                </a>

                <!-- Card 4: Quality -->
                <a href=\"resource-quality.html\" class=\"case-card-link\" style=\"display: block; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); transition: transform 0.3s ease; text-decoration: none; color: inherit;\">
                    <div style=\"height: 200px; background-image: url('../images/thumb_res_quality.png'); background-size: cover; background-position: center; border-bottom: 3px solid #C5A059;\"></div>
                    <div style=\"padding: 30px;\">
                        <span style=\"display: inline-block; background: #f0f4f8; color: #002FA7; padding: 4px 10px; border-radius: 4px; font-size: 11px; font-weight: 600; text-transform: uppercase; margin-bottom: 15px;\">{texts["c4_tag"]}</span>
                        <h3 style=\"font-family: 'Playfair Display', serif; font-size: 22px; font-weight: 700; color: #111; margin-bottom: 15px; line-height: 1.3;\">{texts["c4_title"]}</h3>
                        <p style=\"font-size: 15px; color: #666; line-height: 1.6; margin-bottom: 20px;\">
                            {texts["c4_desc"]}
                        </p>
                        <span style=\"color: #002FA7; font-weight: 600; font-size: 14px;\">{texts["explore"]}</span>
                    </div>
                </a>

                <!-- Card 5: FAQ & Glossary -->
                <a href=\"resource-faq.html\" class=\"case-card-link\" style=\"display: block; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); transition: transform 0.3s ease; text-decoration: none; color: inherit;\">
                    <div style=\"height: 200px; background-image: url('../images/thumb_res_faq.png'); background-size: cover; background-position: center; border-bottom: 3px solid #C5A059;\"></div>
                    <div style=\"padding: 30px;\">
                        <span style=\"display: inline-block; background: #f0f4f8; color: #002FA7; padding: 4px 10px; border-radius: 4px; font-size: 11px; font-weight: 600; text-transform: uppercase; margin-bottom: 15px;\">{texts["c5_tag"]}</span>
                        <h3 style=\"font-family: 'Playfair Display', serif; font-size: 22px; font-weight: 700; color: #111; margin-bottom: 15px; line-height: 1.3;\">{texts["c5_title"]}</h3>
                        <p style=\"font-size: 15px; color: #666; line-height: 1.6; margin-bottom: 20px;\">
                            {texts["c5_desc"]}
                        </p>
                        <span style=\"color: #002FA7; font-weight: 600; font-size: 14px;\">{texts["explore"]}</span>
                    </div>
                </a>
                
            </div>
            
            <style>
            .case-card-link:hover {{
                transform: translateY(-5px) !important;
                box-shadow: 0 10px 25px rgba(0,0,0,0.1) !important;
            }}
            </style>
        </div>
    </section>
'''

    footer_footer_match = re.search(r'(<!-- Smooth Scroll JavaScript -->.*)', html, re.IGNORECASE | re.DOTALL)
    if not footer_footer_match:
        footer_footer_match = re.search(r'(<footer.*)', html, re.IGNORECASE | re.DOTALL)
    final_footer = footer_footer_match.group(1) if footer_footer_match else ''

    with open(os.path.join(lang, 'resources.html'), 'w', encoding='utf-8') as f:
        f.write(cards_html + final_footer)

    print(f"[{lang}] Updated resources.html hub page")
