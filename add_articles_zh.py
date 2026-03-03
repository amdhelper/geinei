"""Add Self-Lubricating Bearings and Sintering Process articles to zh/resources.html (Traditional Chinese)"""

BEARINGS_ZH = '''
                    <!-- 含油軸承指南 -->
                    <div id="bearings-guide" style="margin-bottom:80px">
                        <h3 style="font-family:'Playfair Display',serif;font-size:28px;font-weight:700;color:#333;margin-bottom:15px;border-bottom:2px solid #eee;padding-bottom:10px">
                            🔩 含油軸承（自潤滑軸承）指南
                        </h3>
                        <p style="font-size:16px;color:#555;line-height:1.7;margin-bottom:25px">
                            含油軸承是粉末冶金最成功的應用之一。其獨特的多孔結構能夠自動儲存和釋放潤滑油，使其成為免維護應用的理想選擇。
                        </p>

                        <h4 style="font-size:22px;font-weight:600;color:#002FA7;margin-bottom:15px;padding-left:15px;border-left:4px solid #C5A059">
                            含油軸承的工作原理
                        </h4>
                        <div style="background:linear-gradient(135deg,#f0f4ff 0%,#e8f4fd 100%);border:2px solid #C5A059;border-radius:12px;padding:25px;margin-bottom:25px">
                            <p style="font-size:15px;line-height:1.8;color:#333;margin:0 0 15px 0">
                                PM軸承以<strong>可控孔隙率（體積15-25%）</strong>製造。燒結後進行真空浸油處理。運轉過程中：
                            </p>
                            <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px">
                                <div style="background:white;padding:15px;border-radius:8px;text-align:center">
                                    <div style="font-size:32px;margin-bottom:8px">🔄</div>
                                    <strong style="font-size:14px;color:#002FA7">1. 熱膨脹</strong>
                                    <p style="font-size:13px;color:#666;margin:5px 0 0">摩擦產生熱量 → 油膨脹滲出至表面</p>
                                </div>
                                <div style="background:white;padding:15px;border-radius:8px;text-align:center">
                                    <div style="font-size:32px;margin-bottom:8px">💧</div>
                                    <strong style="font-size:14px;color:#002FA7">2. 潤滑</strong>
                                    <p style="font-size:13px;color:#666;margin:5px 0 0">油膜在軸承與軸之間形成 → 降低摩擦</p>
                                </div>
                                <div style="background:white;padding:15px;border-radius:8px;text-align:center">
                                    <div style="font-size:32px;margin-bottom:8px">🧲</div>
                                    <strong style="font-size:14px;color:#002FA7">3. 回吸</strong>
                                    <p style="font-size:13px;color:#666;margin:5px 0 0">停止時，毛細作用將油吸回孔隙中</p>
                                </div>
                            </div>
                        </div>

                        <h4 style="font-size:22px;font-weight:600;color:#002FA7;margin-bottom:15px;padding-left:15px;border-left:4px solid #C5A059">
                            軸承類型比較
                        </h4>
                        <table class="process-table">
                            <thead><tr><th>比較項目</th><th>PM含油軸承</th><th>滾珠軸承</th><th>滑動軸承</th></tr></thead>
                            <tbody>
                                <tr><td><strong>維護需求</strong></td><td class="highlight-pm">免維護</td><td>需定期潤滑</td><td>需潤滑</td></tr>
                                <tr><td><strong>噪音</strong></td><td class="highlight-pm">非常安靜</td><td>中等</td><td>安靜</td></tr>
                                <tr><td><strong>量產成本</strong></td><td class="highlight-pm">⭐ 最低</td><td>高</td><td>中等</td></tr>
                                <tr><td><strong>轉速範圍</strong></td><td>低-中速</td><td>高速</td><td>低速</td></tr>
                                <tr><td><strong>承載能力</strong></td><td>輕-中載</td><td>高載</td><td>中載</td></tr>
                                <tr><td><strong>使用壽命</strong></td><td class="highlight-pm">10,000+ 小時</td><td>20,000+ 小時</td><td>5,000+ 小時</td></tr>
                            </tbody>
                        </table>

                        <h4 style="font-size:22px;font-weight:600;color:#002FA7;margin-bottom:15px;margin-top:30px;padding-left:15px;border-left:4px solid #C5A059">
                            PM軸承常用材料
                        </h4>
                        <table class="term-table">
                            <thead><tr><th style="width:180px">材料</th><th>MPIF編碼</th><th>PV極限 (MPa·m/s)</th><th>適用場合</th></tr></thead>
                            <tbody>
                                <tr><td class="term-name">青銅 (90Cu-10Sn)</td><td>CT-1000</td><td>1.8</td><td>低速輕載。家電、風扇、玩具</td></tr>
                                <tr><td class="term-name">鐵銅合金</td><td>FC-0208</td><td>3.5</td><td>中等負載。汽車配件、電動工具</td></tr>
                                <tr><td class="term-name">鐵青銅複合</td><td>FC-0800</td><td>2.5</td><td>均衡性能。馬達、泵浦</td></tr>
                            </tbody>
                        </table>

                        <div class="decision-box" style="background:linear-gradient(135deg,#f0f4ff 0%,#e8f4fd 100%)">
                            <h4>🏭 常見應用領域</h4>
                            <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px">
                                <div style="background:white;padding:12px;border-radius:8px;text-align:center"><div style="font-size:28px">🖥️</div><strong style="font-size:13px">電腦散熱風扇</strong></div>
                                <div style="background:white;padding:12px;border-radius:8px;text-align:center"><div style="font-size:28px">🚗</div><strong style="font-size:13px">汽車馬達</strong></div>
                                <div style="background:white;padding:12px;border-radius:8px;text-align:center"><div style="font-size:28px">🏠</div><strong style="font-size:13px">家用電器</strong></div>
                                <div style="background:white;padding:12px;border-radius:8px;text-align:center"><div style="font-size:28px">🔧</div><strong style="font-size:13px">電動工具</strong></div>
                            </div>
                            <p style="margin-top:15px;font-size:14px;color:#666">
                                <strong>💡 設計建議：</strong>為獲最佳性能，軸與軸承間隙建議維持0.02-0.05mm。<a href="contact.html" style="color:#002FA7">聯絡我們</a>獲取軸承設計支援！
                            </p>
                        </div>
                    </div>
'''

SINTERING_ZH = '''
                    <!-- 燒結製程解析 -->
                    <div id="sintering-guide" style="margin-bottom:80px">
                        <h3 style="font-family:'Playfair Display',serif;font-size:28px;font-weight:700;color:#333;margin-bottom:15px;border-bottom:2px solid #eee;padding-bottom:10px">
                            🔥 燒結製程解析
                        </h3>
                        <p style="font-size:16px;color:#555;line-height:1.7;margin-bottom:25px">
                            燒結是將壓製成形的金屬粉末（「生坯」）轉變為高強度功能性零件的關鍵熱處理步驟。了解燒結製程有助於工程師優化零件性能與品質。
                        </p>

                        <h4 style="font-size:22px;font-weight:600;color:#002FA7;margin-bottom:15px;padding-left:15px;border-left:4px solid #C5A059">
                            PM製造流程
                        </h4>
                        <div style="display:flex;flex-wrap:wrap;gap:0;margin-bottom:30px;justify-content:center">
                            <div style="background:#002FA7;color:white;padding:20px 15px;text-align:center;min-width:140px;flex:1;border-radius:8px 0 0 8px">
                                <div style="font-size:28px;margin-bottom:8px">⚗️</div>
                                <strong style="font-size:14px">1. 粉末混合</strong>
                                <p style="font-size:12px;opacity:0.85;margin:5px 0 0">金屬粉末＋添加劑依配方混合</p>
                            </div>
                            <div style="background:#1a47b8;color:white;padding:20px 15px;text-align:center;min-width:140px;flex:1">
                                <div style="font-size:28px;margin-bottom:8px">🔨</div>
                                <strong style="font-size:14px">2. 壓製成形</strong>
                                <p style="font-size:12px;opacity:0.85;margin:5px 0 0">400-700 MPa壓力在精密模具中成形</p>
                            </div>
                            <div style="background:#C5A059;color:white;padding:20px 15px;text-align:center;min-width:140px;flex:1;border:3px solid #8B6914">
                                <div style="font-size:28px;margin-bottom:8px">🔥</div>
                                <strong style="font-size:14px">3. 燒結</strong>
                                <p style="font-size:12px;opacity:0.95;margin:5px 0 0">1100-1300°C控制氣氛爐</p>
                            </div>
                            <div style="background:#1a47b8;color:white;padding:20px 15px;text-align:center;min-width:140px;flex:1;border-radius:0 8px 8px 0">
                                <div style="font-size:28px;margin-bottom:8px">✨</div>
                                <strong style="font-size:14px">4. 後處理</strong>
                                <p style="font-size:12px;opacity:0.85;margin:5px 0 0">整形、熱處理、電鍍等</p>
                            </div>
                        </div>

                        <h4 style="font-size:22px;font-weight:600;color:#002FA7;margin-bottom:15px;padding-left:15px;border-left:4px solid #C5A059">
                            燒結溫度與氣氛對照表
                        </h4>
                        <table class="term-table">
                            <thead><tr><th style="width:180px">材料</th><th>溫度 (°C)</th><th>氣氛</th><th>時間 (分)</th><th>要點</th></tr></thead>
                            <tbody>
                                <tr><td class="term-name">鐵碳鋼<br>(FC-0208)</td><td>1120 - 1150</td><td>N₂/H₂ (90/10)</td><td>20 - 30</td><td>最常用。碳含量控制是硬度的關鍵。</td></tr>
                                <tr><td class="term-name">鐵鎳鋼<br>(FN-0205)</td><td>1120 - 1150</td><td>N₂/H₂ (90/10)</td><td>25 - 35</td><td>更高強度。鎳提升韌性和淬透性。</td></tr>
                                <tr><td class="term-name">不鏽鋼<br>(SS-316L)</td><td>1250 - 1350</td><td>真空或H₂</td><td>30 - 60</td><td>需高溫。必須避免鉻氧化。</td></tr>
                                <tr><td class="term-name">青銅<br>(CT-1000)</td><td>800 - 850</td><td>N₂/H₂ 或吸熱式</td><td>15 - 25</td><td>較低溫度。用於軸承和襯套。</td></tr>
                                <tr><td class="term-name">軟磁材料<br>(純鐵)</td><td>1120 - 1150</td><td>H₂ 或分解氨</td><td>30 - 45</td><td>需高純度氣氛以確保磁性能。</td></tr>
                            </tbody>
                        </table>

                        <h4 style="font-size:22px;font-weight:600;color:#002FA7;margin-bottom:15px;margin-top:30px;padding-left:15px;border-left:4px solid #C5A059">
                            燒結過程中發生什麼？
                        </h4>
                        <table class="term-table">
                            <thead><tr><th style="width:180px">階段</th><th>溫度範圍</th><th>發生的變化</th></tr></thead>
                            <tbody>
                                <tr><td class="term-name">脫蠟階段</td><td>150 - 600°C</td><td>潤滑劑（硬脂酸鋅）蒸發。需控制升溫速率以避免起泡。</td></tr>
                                <tr><td class="term-name">還原氧化物</td><td>600 - 900°C</td><td>氫氣還原粉末顆粒表面氧化物，使金屬鍵結成為可能。</td></tr>
                                <tr><td class="term-name">顆粒結合</td><td>900 - 1150°C</td><td>原子擴散在顆粒間形成頸部。強度大幅提升。</td></tr>
                                <tr><td class="term-name">緻密化</td><td>峰值溫度</td><td>孔隙縮小，晶粒長大。零件達到最終密度（6.4-7.2 g/cm³）。</td></tr>
                                <tr><td class="term-name">冷卻</td><td>峰值 → 室溫</td><td>控制冷卻速率決定最終微觀組織和硬度。</td></tr>
                            </tbody>
                        </table>

                        <div class="decision-box" style="background:linear-gradient(135deg,#fff8e1 0%,#fff3e0 100%)">
                            <h4>🔬 冶聖的燒結品質管控</h4>
                            <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px">
                                <div style="background:white;padding:15px;border-radius:8px;border-left:3px solid #C5A059">
                                    <strong style="color:#002FA7">🌡️ 溫度監控</strong>
                                    <p style="font-size:13px;margin:8px 0 0;color:#666">爐區全程±5°C精度</p>
                                </div>
                                <div style="background:white;padding:15px;border-radius:8px;border-left:3px solid #C5A059">
                                    <strong style="color:#002FA7">💨 氣氛控制</strong>
                                    <p style="font-size:13px;margin:8px 0 0;color:#666">露點和氣體成分持續監測</p>
                                </div>
                                <div style="background:white;padding:15px;border-radius:8px;border-left:3px solid #C5A059">
                                    <strong style="color:#002FA7">📊 密度檢測</strong>
                                    <p style="font-size:13px;margin:8px 0 0;color:#666">每批次依MPIF Standard 42驗證</p>
                                </div>
                            </div>
                            <p style="margin-top:15px;font-size:14px;color:#666">
                                <strong>📧 對燒結有疑問？</strong>我們的工程團隊可以幫助您選擇正確的參數。<a href="contact.html" style="color:#002FA7;font-weight:600">聯絡我們 →</a>
                            </p>
                        </div>
                    </div>
'''

# zh/ Traditional Chinese
with open('zh/resources.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert before legal statement
content = content.replace('<!-- 法律聲明 -->', BEARINGS_ZH + SINTERING_ZH + '\n                        <!-- 法律聲明 -->')

# Add sidebar nav
old_nav = '<li><a href="#faq">❓ 常見問題</a></li>'
new_nav = '<li><a href="#bearings-guide">🔩 含油軸承</a></li>\n                        <li><a href="#sintering-guide">🔥 燒結製程</a></li>\n                        <li><a href="#faq">❓ 常見問題</a></li>'
content = content.replace(old_nav, new_nav)

# Update JS sections
old_js = "const sections = ['process-guide', 'faq', 'glossary', 'materials', 'iron-steel', 'stainless', 'magnetic', 'bronze-brass'];"
new_js = "const sections = ['process-guide', 'gear-types', 'bearings-guide', 'sintering-guide', 'faq', 'glossary', 'materials', 'iron-steel', 'stainless', 'magnetic', 'bronze-brass'];"
content = content.replace(old_js, new_js)

with open('zh/resources.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("zh/resources.html updated!")
