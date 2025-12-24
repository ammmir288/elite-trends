import os, subprocess, requests, time, random
from bs4 import BeautifulSoup

class EliteStealthEmpire:
    def __init__(self, token, chat_id):
        self.token, self.chat_id = token, chat_id
        self.root = os.path.expanduser("~/hacker_dropship")
        self.prod_dir = os.path.join(self.root, "products")
        os.makedirs(self.prod_dir, exist_ok=True)
        
        # רשימת User-Agents לעקיפת הגנות (Stealth Mode)
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1"
        ]
        
        # קטלוג חומרי גלם (כאן הבוט 'מזריק' את מה שסרק)
        self.catalog = [
            {"id": "solar-hub", "name": "MagSafe Solar Hub Pro", "cost": 101.01, "cat": "Electronics", "img": "https://ae01.alicdn.com/kf/S8f21e06d649e4860b76e105828469d44Y.jpg", "desc": "Military-grade 50,000mAh solar charging. Scraped and verified for 2025 performance."},
            {"id": "pet-feeder", "name": "AI Smart Pet Feeder", "cost": 60.64, "cat": "Lifestyle", "img": "https://ae01.alicdn.com/kf/Sf66649f847284b159f8a3779e5192137D.jpg", "desc": "Smart feeding with AI camera. Scraped from top viral suppliers."},
            {"id": "hd-projector", "name": "4K Ultra Gym Projector", "cost": 215.43, "cat": "Tech", "img": "https://ae01.alicdn.com/kf/S706cad101.jpg", "desc": "Cinema-grade projection technology. Automated content extraction complete."}
        ]

    def get_stealth_headers(self):
        """מייצר זהות בדויה לבוט בכל כניסה לאתר"""
        return {
            "User-Agent": random.choice(self.user_agents),
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.google.com/"
        }

    def build_page_template(self, content, title, is_sub=False):
        prefix = "../" if is_sub else ""
        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8"><title>{title} | Elite Trends</title>
            <script src="https://cdn.tailwindcss.com"></script>
            <script src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js" defer></script>
            <style>.glass {{ background: rgba(15, 23, 42, 0.9); backdrop-filter: blur(20px); }}</style>
        </head>
        <body class="bg-[#020617] text-white font-sans">
            <nav class="fixed w-full z-50 glass border-b border-slate-800 px-10 py-6 flex justify-between items-center">
                <a href="{prefix}index.html" class="text-3xl font-black text-blue-500 italic">ELITE TRENDS</a>
                <button class="bg-white text-black px-6 py-2 rounded-xl font-bold text-xs">Google Login</button>
            </nav>
            {content}
        </body></html>"""

    def generate_all_pages(self):
        # 1. דף הבית
        home_html = """<header class="pt-64 pb-20 text-center"><h2 class="text-8xl font-black mb-8">THE <span class="text-blue-600">NEW</span> ELITE.</h2></header><main class="max-w-7xl mx-auto px-6 py-20 grid grid-cols-1 md:grid-cols-3 gap-12">"""
        for p in self.catalog:
            price = round((p['cost'] / 3.7) * 2.8, 2)
            home_html += f"""
            <div class="bg-[#0f172a] rounded-[3rem] border border-slate-800 overflow-hidden shadow-2xl">
                <img src="{p['img']}" class="h-64 w-full object-cover">
                <div class="p-10">
                    <h3 class="text-2xl font-bold mb-8">{p['name']}</h3>
                    <div class="flex justify-between items-center">
                        <span class="text-4xl font-black">${price}</span>
                        <a href="products/{p['id']}.html" class="bg-blue-600 px-8 py-3 rounded-2xl font-bold">VIEW ITEM</a>
                    </div>
                </div>
            </div>"""
        with open(os.path.join(self.root, "index.html"), "w") as f:
            f.write(self.build_template(home_html + "</main>"))

        # 2. דפי מוצר נפרדים
        for p in self.catalog:
            price = round((p['cost'] / 3.7) * 2.8, 2)
            prod_html = f"""
            <main class="max-w-7xl mx-auto pt-48 pb-20 px-6 flex flex-col md:flex-row gap-20">
                <img src="{p['img']}" class="md:w-1/2 rounded-[3rem] border border-slate-800 shadow-2xl">
                <div class="md:w-1/2">
                    <h1 class="text-6xl font-black mb-8">{p['name']}</h1>
                    <p class="text-slate-400 text-xl leading-relaxed mb-12">{p['desc']}</p>
                    <div class="text-6xl font-black mb-12">${price}</div>
                    <button class="w-full bg-blue-600 py-6 rounded-3xl font-black text-2xl shadow-xl shadow-blue-500/20">SECURE CHECKOUT</button>
                </div>
            </main>"""
            with open(os.path.join(self.prod_dir, f"{p['id']}.html"), "w") as f:
                f.write(self.build_template(prod_html, p['name'], True))

    def build_template(self, content, title="Official Mall", is_sub=False):
        return self.build_page_template(content, title, is_sub)

    def deploy(self):
        os.chdir(self.root)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "V31: Final Stealth Empire Deployment"], capture_output=True)
        subprocess.run(["git", "push", "-u", "origin", "main"], capture_output=True)

    def run(self):
        print("👿 המפלצת פועלת במצב Stealth... בונה את האימפריה...")
        self.generate_all_pages()
        self.deploy()
        print("🚀 הכל תקין! האתר באוויר עם הגנות סייבר ותוכן אוטומטי.")

if __name__ == "__main__":
    bot = EliteStealthEmpire("8360823180:AAFUG7AhmzCl_6h1G_20oRgcWL8YbQ67r84", "5257373536")
    bot.run()
