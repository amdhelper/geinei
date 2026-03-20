import os
import re

base_dir = r"c:\Users\USER\geinei_clean"
langs = ['', 'zh', 'zh-cn', 'jp', 'de']

# Localized metadata for the News Page
locales = {
    '': {
        'title': '【Industry News】Additive Manufacturing & Powder Metallurgy Trends',
        'desc_meta': 'Stay updated with the latest industry news, additive manufacturing (AM) breakthroughs, Directed Energy Deposition (DED), and metal powder innovations.',
        'h2': 'Industry News <span style="font-family: \'Inter\', \'Arial\', sans-serif;">&amp;</span> Innovations',
        'desc_text': 'Stay updated with the latest trends, additive manufacturing (AM) breakthroughs, and metal powder innovations.',
        'nav_text': '📰 Industry News',
        'art_tag': 'Additive Manufacturing (AM)',
        'art_date': 'March 19, 2026',
        'art_title': 'Aconity3D introduces multi-material welding head for DED',
        'art_desc': 'Aconity3D has launched a new multi-material welding head designed for Directed Energy Deposition (DED) processes. This innovative head allows for the simultaneous use of two different metal powders or wire materials, paving the way for advanced additive manufacturing solutions and multi-metal components.',
        'read_more': 'Read Full Article'
    },
    'zh': {
        'title': '【產業新聞】積層製造與粉末冶金最新趨勢',
        'desc_meta': '掌握最新產業動態、積層製造 (AM) 突破、雷射金屬沉積 (DED) 以及金屬粉末創新技術。',
        'h2': '產業新聞 <span style="font-family: \'Inter\', \'Arial\', sans-serif;">&amp;</span> 創新技術',
        'desc_text': '掌握最新趨勢、積層製造 (AM) 突破與金屬粉末創新技術。',
        'nav_text': '📰 產業新聞',
        'art_tag': '積層製造 (AM)',
        'art_date': 'March 19, 2026',
        'art_title': 'Aconity3D 發表應用於 DED (雷射金屬沉積) 的多材質焊接頭',
        'art_desc': 'Aconity3D 推出了一款專為直接能量沉積 (DED) 製程設計的新型多材質焊接頭。這項創新的技術允許同時使用兩種不同的金屬粉末或線材，為先進積層製造解決方案與多金屬複合零件的生產鋪平了道路。',
        'read_more': '閱讀全文'
    },
    'zh-cn': {
        'title': '【产业新闻】增材制造与粉末冶金最新趋势',
        'desc_meta': '掌握最新产业动态、增材制造 (AM) 突破、激光金属沉积 (DED) 以及金属粉末创新技术。',
        'h2': '产业新闻 <span style="font-family: \'Inter\', \'Arial\', sans-serif;">&amp;</span> 创新技术',
        'desc_text': '掌握最新趋势、增材制造 (AM) 突破与金属粉末创新技术。',
        'nav_text': '📰 产业新闻',
        'art_tag': '增材制造 (AM)',
        'art_date': 'March 19, 2026',
        'art_title': 'Aconity3D 发布应用于 DED (激光金属沉积) 的多材质焊接头',
        'art_desc': 'Aconity3D 推出了一款专为直接能量沉积 (DED) 工艺设计的新型多材质焊接头。这项创新的技术允许同时使用两种不同的金属粉末或线材，为先进增材制造解决方案与多金属复合零件的生产铺平了道路。',
        'read_more': '阅读全文'
    },
    'jp': {
        'title': '【業界ニュース】積層造形と粉末冶金の最新トレンド',
        'desc_meta': '最新の業界ニュース、積層造形（AM）のブレークスルー、指向性エネルギー堆積（DED）、および金属粉末のイノベーションをご紹介します。',
        'h2': '業界ニュース <span style="font-family: \'Inter\', \'Arial\', sans-serif;">&amp;</span> イノベーション',
        'desc_text': '最新のトレンド、積層造形（AM）のブレークスルー、金属粉末のイノベーションをご紹介します。',
        'nav_text': '📰 業界ニュース',
        'art_tag': '積層造形 (AM)',
        'art_date': 'March 19, 2026',
        'art_title': 'Aconity3D、DED向けマルチマテリアル溶接ヘッドを発表',
        'art_desc': 'Aconity3Dは、指向性エネルギー堆積（DED）プロセス用に設計された新しいマルチマテリアル溶接ヘッドを発表しました。この革新的なヘッドにより、2種類の異なる金属粉末またはワイヤ材料を同時に使用できるようになり、高度な積層造形ソリューションとマルチメタル部品への道が開かれます。',
        'read_more': '原文を読む'
    },
    'de': {
        'title': '【Branchennachrichten】Trends in Additiver Fertigung & Pulvermetallurgie',
        'desc_meta': 'Bleiben Sie informiert auf dem Laufenden mit den neuesten Branchennachrichten, Durchbrüchen in der additiven Fertigung (AM) und Innovationen bei Metallpulvern.',
        'h2': 'Branchennachrichten <span style="font-family: \'Inter\', \'Arial\', sans-serif;">&amp;</span> Innovationen',
        'desc_text': 'Bleiben Sie informiert über die neuesten Trends, Durchbrüche in der additiven Fertigung (AM) und Innovationen bei Metallpulvern.',
        'nav_text': '📰 Branchennachrichten',
        'art_tag': 'Additive Fertigung (AM)',
        'art_date': '19. März 2026',
        'art_title': 'Aconity3D stellt Multimaterial-Schweißkopf für DED vor',
        'art_desc': 'Aconity3D hat einen neuen Multimaterial-Schweißkopf für das Directed Energy Deposition (DED) Verfahren auf den Markt gebracht. Dieser innovative Kopf ermöglicht die gleichzeitige Verwendung von zwei verschiedenen Metallpulvern oder Drahtmaterialien und ebnet so den Weg für fortschrittliche additive Fertigungslösungen und Multimetallkomponenten.',
        'read_more': 'Vollständigen Artikel lesen'
    }
}

for lang in langs:
    faq_path = os.path.join(base_dir, lang, "resource-faq.html") if lang else os.path.join(base_dir, "resource-faq.html")
    news_path = os.path.join(base_dir, lang, "resource-news.html") if lang else os.path.join(base_dir, "resource-news.html")
    
    if not os.path.exists(faq_path):
        print(f"File not found: {faq_path}")
        continue
    
    with open(faq_path, 'r', encoding='utf-8') as f:
        content = f.read()

    loc = locales[lang]

    # 1. Replace Title & Meta Description
    content = re.sub(r'<title>.*?</title>', f'<title>{loc["title"]}</title>', content)
    content = re.sub(r'<meta content=".*?" name="description"/>', f'<meta content="{loc["desc_meta"]}" name="description"/>', content)
    
    # 2. Replace Links resource-faq.html -> resource-news.html in hreflang and canonical
    content = content.replace('resource-faq.html', 'resource-news.html')

    # 3. Modify Page Header
    content = re.sub(r'<h2.*?>.*?</h2>', f'<h2 style="font-family: \'Playfair Display\', serif; font-size: 32px; font-weight: 700; color: #555; margin-bottom: 20px;">\n                    {loc["h2"]}</h2>', content, count=1)
    
    # Replace description paragraph in header
    content = re.sub(r'<p style="font-size: 18px; color: #555; max-width: 800px; margin: 0 auto; line-height: 1.6;">.*?</p>', f'<p style="font-size: 18px; color: #555; max-width: 800px; margin: 0 auto; line-height: 1.6;">\n                    {loc["desc_text"]}\n                </p>', content, flags=re.DOTALL)

    # 4. Add to Sidebar Navigation
    # Find the end of sidebar-nav ul
    if '</ul>' in content:
        # Add new li before </ul> in sidebar
        new_li = f'<li><a href="resource-news.html" class="active">{loc["nav_text"]}</a></li>\n</ul>'
        content = content.replace('</ul>', new_li, 1)

    # 5. Extract <div class="resource-content"> to </div> and replace content
    # Look for <!-- FAQ Section --> and replace from there to the next sibling closing tags
    
    news_content = f"""<!-- News Section -->
<div class="news-list" style="display: flex; flex-direction: column; gap: 30px;">
    <!-- Article 1 -->
    <a href="https://www.metal-am.com/aconity3d-introduces-multi-material-welding-head-for-ded/" target="_blank" rel="noopener noreferrer" style="display: block; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); transition: transform 0.3s ease, box-shadow 0.3s ease; text-decoration: none; color: inherit; border: 1px solid #eee;">
        <div style="padding: 30px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                <span style="display: inline-block; background: #f0f4f8; color: #002FA7; padding: 4px 10px; border-radius: 4px; font-size: 11px; font-weight: 600; text-transform: uppercase;">{loc['art_tag']}</span>
                <span style="color: #888; font-size: 13px;">{loc['art_date']}</span>
            </div>
            <h3 style="font-family: 'Playfair Display', serif; font-size: 24px; font-weight: 700; color: #111; margin-bottom: 15px; line-height: 1.3;">{loc['art_title']}</h3>
            <p style="font-size: 15px; color: #666; line-height: 1.6; margin-bottom: 20px;">
                {loc['art_desc']}
            </p>
            <span style="color: #002FA7; font-weight: 600; font-size: 14px; display: flex; align-items: center; gap: 5px;">{loc['read_more']} <span style="font-size: 18px;">&rarr;</span></span>
        </div>
    </a>
</div>
<style>
    .news-list a:hover {{
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        border-color: #C5A059;
    }}
</style>
</div> <!-- Close resource-content -->"""

    # We need to replace everything starting from <!-- FAQ Section --> up to the closing </div> of resource-content
    # The resource content has structure: <div class="resource-content"><!-- FAQ Section ... </div>
    # Using regex to replace the content correctly
    content_pattern = re.compile(r'(<div class="resource-content">)<!-- FAQ Section -->.*?(</div>\s*</div>\s*<!-- Footer -->|<footer)', re.DOTALL)
    
    # Actually wait, resource-faq.html might not have <!-- Footer --> immediately, let's just find <div class="resource-content"> and replace the rest until <footer or <section if there's another section.
    # A safer method is strictly breaking out everything inside Resource Content
    # resource-faq.html has <div class="resource-content">, then `<div class="accordion-card"...`, and then `</div></section>`.
    
    resource_content_pattern = re.compile(r'(<div class="resource-content">)(.*?)(</div>\s*<!-- Layout with Sidebar -->\s*</div>\s*</section>|</div>\s*</div>\s*</section>|<footer)', re.DOTALL)
    
    match = resource_content_pattern.search(content)
    if match:
        content = content[:match.start(2)] + news_content + "\n" + content[match.start(3):]
    else:
        # Fallback Replacement
        print("Fallback replacement used.")
        faq_start = content.find('<!-- FAQ Section -->')
        if faq_start != -1:
            end_tag = '</section>'
            faq_end = content.find(end_tag, faq_start)
            content = content[:faq_start] + news_content + "\n" + content[faq_end:]

    with open(news_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Created {news_path}")
