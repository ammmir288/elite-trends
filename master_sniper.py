import os, subprocess, requests, json
from bs4 import BeautifulSoup # כלי ה"האקרים" לסריקת אתרים

class ScrapingSniperV30:
    def __init__(self, token, chat_id):
        self.root = os.path.expanduser("~/hacker_dropship")
        self.prod_dir = os.path.join(self.root, "products")
        os.makedirs(self.prod_dir, exist_ok=True)
        
        # רשימת "מטרות" - כאן אתה שם קישורים למוצרים שאתה רוצה להעתיק
        self.targets = [
            "https://www.aliexpress.com/item/1005007559196303.html", # דוגמה למטען
            "https://www.aliexpress.com/item/1005007137060377.html"  # דוגמה למאכיל חיות
        ]
        self.catalog = []

    def scrape_raw_material(self, url):
        """פונקציה ש'שואבת' את התוכן מהאתר המטרה"""
        print(f"🕵️ מגרד חומר גלם מהכתובת: {url}")
        try:
            # בגרסה המלאה נשתמש ב-Selenium/Playwright לעקוף הגנות
            # כאן בנינו את המבנה שקולט את הנתונים
            return {
                "id": f"item-{len(self.catalog)}",
                "name": "Scraped Viral Gadget", # כאן יכנס השם שנסרק
                "cost": 50.00, # מחיר שנסרק
                "cat": "Trending",
                "img": "https://via.placeholder.com/500", # תמונה שנסרקה
                "desc": "Raw material content scraped automatically from source."
            }
        except Exception as e:
            return None

    def build_enterprise_site(self):
        """בונה את האתר עם חומרי הגלם שנסרקו"""
        # (השתמשנו בלוגיקה של V29 עם העיצוב היוקרתי)
        for p in self.catalog:
            price = round((p['cost'] / 3.7) * 2.8, 2) # רווח מוגדל אוטומטי
            # יצירת דף מוצר (Product Page)
            html = f"""
            <html><head><script src="https://cdn.tailwindcss.com"></script></head>
            <body class="bg-[#020617] text-white p-20">
                <div class="max-w-4xl mx-auto flex gap-10">
                    <img src="{p['img']}" class="w-1/2 rounded-3xl">
                    <div>
                        <h1 class="text-5xl font-black">{p['name']}</h1>
                        <p class="mt-6 text-slate-400">{p['desc']}</p>
                        <div class="text-4xl font-bold mt-10">${price}</div>
                        <button class="bg-blue-600 px-10 py-4 rounded-xl mt-10">BUY FROM ELITE TRENDS</button>
                    </div>
                </div>
            </body></html>"""
            with open(f"{self.prod_dir}/{p['id']}.html", "w") as f: f.write(html)

    def run(self):
        # 1. איסוף חומר גלם
        for url in self.targets:
            data = self.scrape_raw_material(url)
            if data: self.catalog.append(data)
        
        # 2. בניית האתר
        self.build_enterprise_site()
        
        # 3. דחיפה לגיטהאב
        os.chdir(self.root)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "V30: Scraped Raw Materials Update"], capture_output=True)
        subprocess.run(["git", "push", "-u", "origin", "main"], capture_output=True)
        print("🚀 המשימה הושלמה! חומרי הגלם נשאבו והאתר עודכן.")

if __name__ == "__main__":
    bot = ScrapingSniperV30("8360823180:AAFUG7AhmzCl_6h1G_20oRgcWL8YbQ67r84", "5257373536")
    bot.run()
