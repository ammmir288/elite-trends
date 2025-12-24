import requests, os, subprocess, time

class EmpireIntegrator:
    def __init__(self, token, chat_id):
        self.token, self.chat_id = token, chat_id
        self.path = os.path.expanduser("~/hacker_dropship")
        # נתונים מדויקים מהחיפושים שלך (עליאקספרס)
        self.products = [
            {"id": "1", "name": "MagSafe Solar Hub", "cost": 101.01, "cat": "Electronics", "ali_id": "1005007559196303", "img": "https://ae01.alicdn.com/kf/S8f21e06d649e4860b76e105828469d44Y.jpg"},
            {"id": "2", "name": "Smart AI Pet Feeder", "cost": 60.64, "cat": "Lifestyle", "ali_id": "1005007137060377", "img": "https://ae01.alicdn.com/kf/Sf66649f847284b159f8a3779e5192137D.jpg"},
            {"id": "3", "name": "Ultra-HD Gym Projector", "cost": 215.43, "cat": "Tech", "ali_id": "1005007559196303", "img": "https://ae01.alicdn.com/kf/S706cad101.jpg"}
        ]

    def generate_elite_site(self):
        """בונה אתר יוקרתי עם קטגוריות, אנימציות ודפי מוצר מלאים"""
        html_start = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Elite Trends | 2025 Global Collection</title>
            <script src="https://cdn.tailwindcss.com"></script>
            <script src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js" defer></script>
            <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
            <style>[x-cloak] { display: none !important; } .glass { background: rgba(15, 23, 42, 0.8); backdrop-filter: blur(12px); }</style>
        </head>
        <body class="bg-[#020617] text-white font-sans" x-data="{ open: false, activeP: {}, category: 'All' }">
            <nav class="fixed w-full z-50 glass border-b border-slate-800 px-10 py-6 flex justify-between items-center">
                <h1 class="text-3xl font-black text-blue-500 italic">ELITE TRENDS</h1>
                <div class="flex space-x-8 text-[10px] font-bold uppercase tracking-widest text-slate-500">
                    <button @click="category = 'All'" :class="category === 'All' ? 'text-blue-400' : ''">All</button>
                    <button @click="category = 'Electronics'" :class="category === 'Electronics' ? 'text-blue-400' : ''">Electronics</button>
                    <button @click="category = 'Tech'" :class="category === 'Tech' ? 'text-blue-400' : ''">Tech</button>
                </div>
            </nav>
            <header class="pt-48 pb-20 text-center">
                <h2 class="text-7xl font-black mb-4" data-aos="zoom-in">VIRAL PRODUCTS.<br><span class="text-blue-600">ZERO EFFORT.</span></h2>
            </header>
            <main class="max-w-7xl mx-auto px-6 py-10 grid grid-cols-1 md:grid-cols-3 gap-10">"""
        
        cards = ""
        for p in self.products:
            sale_price = round((p['cost'] / 3.7) * 2.5, 2)
            desc = f"Professional grade {p['name']} with global shipping and 2025 technology features."
            # שימוש ב-{{}} כדי למנוע את שגיאת ה-NameError שקיבלת
            cards += f"""
                <div class="bg-[#0f172a] rounded-[3rem] p-10 border border-slate-800 hover:border-blue-500 transition-all shadow-2xl" 
                     x-show="category === 'All' || category === '{p['cat']}'" data-aos="fade-up">
                    <span class="text-blue-400 text-[10px] font-black uppercase tracking-widest">{p['cat']}</span>
                    <h3 class="text-2xl font-bold mt-4 mb-6">{p['name']}</h3>
                    <div class="flex justify-between items-center border-t border-slate-800 pt-8">
                        <span class="text-4xl font-black text-white">${sale_price}</span>
                        <button @click="open = true; activeP = {{name:'{p['name']}', price:'{sale_price}', desc:'{desc}', cat:'{p['cat']}'}}" 
                                class="bg-blue-600 px-8 py-3 rounded-2xl font-bold hover:bg-blue-500">VIEW</button>
                    </div>
                </div>"""
        
        html_end = """
            </main>
            <div x-show="open" x-cloak class="fixed inset-0 z-[100] flex items-center justify-center p-6 bg-black/95 backdrop-blur-md">
                <div class="bg-[#0f172a] max-w-2xl w-full rounded-[4rem] p-16 border border-slate-700 relative shadow-2xl" @click.away="open = false">
                    <button @click="open = false" class="absolute top-10 right-10 text-slate-500 text-4xl">&times;</button>
                    <span class="text-blue-500 text-xs font-black uppercase" x-text="activeP.cat"></span>
                    <h2 class="text-6xl font-black mt-4 mb-8 leading-tight" x-text="activeP.name"></h2>
                    <p class="text-slate-400 text-xl leading-relaxed mb-12" x-text="activeP.desc"></p>
                    <div class="flex justify-between items-center">
                        <span class="text-6xl font-black" x-text="'$' + activeP.price"></span>
                        <button class="bg-white text-black px-12 py-5 rounded-[2rem] font-black text-xl hover:bg-blue-600 hover:text-white transition">BUY NOW</button>
                    </div>
                </div>
            </div>
            <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
            <script>AOS.init({ duration: 1000, once: true });</script>
        </body></html>"""
        
        with open(f"{self.path}/index.html", "w") as f: f.write(html_start + cards + html_end)

    def send_media_packet(self, p):
        """שולח לטלגרם גלריית תמונות, קישור עמוק ופרטי פרסום"""
        deep_link = f"https://www.aliexpress.com/item/{p['ali_id']}.html"
        caption = (
            f"👿 *NEW ITEM DEPLOYED* 👿\n"
            f"━━━━━━━━━━━━━━━\n"
            f"📦 *Item:* {p['name']}\n"
            f"💰 *Ali Cost:* {p['cost']} NIS\n"
            f"🎯 *Marketplace Tip:* פרסם במחיר פי 2!\n"
            f"━━━━━━━━━━━━━━━\n"
            f"🔗 [DIRECT DEEP LINK]({deep_link})\n"
            f"━━━━━━━━━━━━━━━\n"
            f"⚡ האתר שלך בגיטהאב עודכן עם המוצר הזה וכל המלל השיווקי!"
        )
        # שליחת התמונה המרכזית (ניתן להוסיף שליחת גלריה מלאה)
        requests.post(f"https://api.telegram.org/bot{self.token}/sendPhoto", 
                     data={"chat_id": self.chat_id, "photo": p['img'], "caption": caption, "parse_mode": "Markdown"})

    def deploy(self):
        os.chdir(self.path)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "All-In-One Empire Update v21"], capture_output=True)
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)

    def run(self):
        print("👿 המפלצת המאוחדת התחילה לעבוד על האימפריה שלך...")
        self.generate_elite_site()
        self.deploy()
        for p in self.products:
            self.send_media_packet(p)
            time.sleep(2) # מניעת ספאם בטלגרם
        print("🚀 האתר באוויר! כל חבילות המדיה נשלחו לטלגרם שלך.")

if __name__ == "__main__":
    bot = EmpireIntegrator("8360823180:AAFUG7AhmzCl_6h1G_20oRgcWL8YbQ67r84", "5257373536")
    bot.run()
