import os
import re

base_dir = r"c:\Users\USER\geinei_clean"
langs = ['', 'zh', 'zh-cn', 'jp', 'de']

# Localized texts for the 6th card
locales = {
    '': {
        'tag': 'Insights & Trends',
        'title': 'Industry News <span style="font-family: \'Inter\', \'Arial\', sans-serif;">&amp;</span> Innovations',
        'desc': 'Stay updated with the latest trends, additive manufacturing (AM) breakthroughs, and metal powder innovations.',
        'explore': 'Explore &rarr;'
    },
    'zh': {
        'tag': '最新動態與趨勢',
        'title': '產業新聞與創新技術',
        'desc': '掌握最新趨勢、積層製造 (AM) 突破與金屬粉末創新技術。',
        'explore': '了解更多 &rarr;'
    },
    'zh-cn': {
        'tag': '最新动态与趋势',
        'title': '产业新闻与创新技术',
        'desc': '掌握最新趋势、增材制造 (AM) 突破与金属粉末创新技术。',
        'explore': '了解更多 &rarr;'
    },
    'jp': {
        'tag': 'インサイトとトレンド',
        'title': '業界ニュースとイノベーション',
        'desc': '最新のトレンド、積層造形（AM）のブレークスルー、金属粉末のイノベーションをご紹介します。',
        'explore': '詳細を見る &rarr;'
    },
    'de': {
        'tag': 'Einblicke & Trends',
        'title': 'Branchennachrichten & Innovationen',
        'desc': 'Bleiben Sie informiert über die neuesten Trends, Durchbrüche in der additiven Fertigung (AM) und Innovationen bei Metallpulvern.',
        'explore': 'Erkunden &rarr;'
    }
}

for lang in langs:
    filepath = os.path.join(base_dir, lang, "resources.html") if lang else os.path.join(base_dir, "resources.html")
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    card_pattern = re.compile(r'(<!-- Card 5.*?</a>)', re.DOTALL)
    match = card_pattern.search(content)
    if not match:
        print(f"Card 5 not found in {filepath}")
        continue
        
    card5_html = match.group(1)
    
    if '<!-- Card 6: Industry News -->' in content:
        print(f"Card 6 already exists in {filepath}")
        continue

    loc = locales[lang]
    if '../images/' in card5_html:
        image_path = "../images/thumb_res_news.png"
    else:
        image_path = "images/thumb_res_news.png"

    card6_html = f"""
<!-- Card 6: Industry News -->
<a class="case-card-link" href="resource-news.html" style="display: block; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); transition: transform 0.3s ease; text-decoration: none; color: inherit;">
<div style="height: 200px; background-image: url('{image_path}'); background-size: cover; background-position: center; border-bottom: 3px solid #C5A059;">
</div>
<div style="padding: 30px;">
<span style="display: inline-block; background: #f0f4f8; color: #002FA7; padding: 4px 10px; border-radius: 4px; font-size: 11px; font-weight: 600; text-transform: uppercase; margin-bottom: 15px;">{loc['tag']}</span>
<h3 style="font-family: 'Playfair Display', serif; font-size: 22px; font-weight: 700; color: #111; margin-bottom: 15px; line-height: 1.3;">
                            {loc['title']}</h3>
<p style="font-size: 15px; color: #666; line-height: 1.6; margin-bottom: 20px;">
                            {loc['desc']}
                        </p>
<span style="color: #002FA7; font-weight: 600; font-size: 14px;">{loc['explore']}</span>
</div>
</a>"""

    new_content = content.replace(card5_html, card5_html + "\n" + card6_html)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Successfully added Card 6 to {filepath}")
