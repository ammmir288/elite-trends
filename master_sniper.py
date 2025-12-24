import requests
import os
import subprocess
import time

class GlobalEmpire:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.path = os.path.expanduser("~/hacker_dropship")

    def generate_site(self, products):
        # יצירת ה-HTML המודרני שאהבת (Dark Mode)
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8"><title>Elite Trends 2025</title>
            <script src="https://cdn.tailwindcss.com"></script>
        </head>
        <body class="bg-[#0f172a] text-slate-200 font-sans">
            <nav class="bg-[#1e293b] p-6 flex justify-between items-center border-b border-slate-700">
                <h1 class="text-3xl font-black text-blue-400">ELITE TRENDS</h1>
                <div class="space-x-8 text-sm font-bold uppercase">
                    <a href="#electronics">Electronics</a><a href="#lifestyle">Lifestyle</a>
                </div>
            </nav>
            <main class="max-w-7xl mx-auto px-6 py-20 grid grid-cols-1 md:grid-cols-3 gap-10">
        """
        for p in products:
            html += f"""
                <div class="bg-[#1e293b] rounded-3xl p-8 border border-slate-700 shadow-xl hover:border-blue-500 transition">
                    <span class="text-blue-400 text-[10px] font-black uppercase">{p['category']}</span>
                    <h3 class="text-2xl font-bold mt-2">{p['name']}</h3>
                    <p class="text-slate-400 text-sm mt-4">{p['desc']}</p>
                    <div class="mt-8 flex justify-between items-center">
                        <span class="text-3xl font-black">${p['price']}</span>
                        <button class="bg-blue-600 px-6 py-3 rounded-xl font-bold">Buy Now</button>
                    </div>
                </div>"""
        html += "</main></body></html>"
        with open(f"{self.path}/index.html", "w") as f: f.write(html)

    def deploy(self):
        # פקודה האקרית להעלאה אוטומטית ללא צורך בהתערבותך
        try:
            os.chdir(self.path)
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "Auto-update products"], check=True)
            subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
            return True
        except Exception as e:
            print(f"Deployment error: {e}")
            return False

    def run(self):
        print("👿 המפלצת סורקת, בונה ומעלה את האתר שלך...")
        # כאן הבוט מוצא את המוצרים שראינו ב-AliExpress ומחשב מחיר בדולרים
        winners = [
            {"name": "MagSafe Solar Hub", "price": 49.99, "category": "Electronics", "desc": "High-capacity solar power bank for mobile devices."},
            {"name": "4K Mini Smart Projector", "price": 120.50, "category": "Tech", "desc": "Transform your room into a high-end cinema."},
            {"name": "Automatic Pet Feeder", "price": 89.00, "category": "Lifestyle", "desc": "Smartphone controlled feeding with 4K camera."}
        ]
        self.generate_site(winners)
        if self.deploy():
            requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage", 
                         json={"chat_id": self.chat_id, "text": "🚀 *EMPIRE UPDATE*: Your site is now LIVE and updated automatically!"})

if __name__ == "__main__":
    TOKEN = "8360823180:AAFUG7AhmzCl_6h1G_20oRgcWL8YbQ67r84"
    CHAT_ID = "5257373536"
    GlobalEmpire(TOKEN, CHAT_ID).run()
