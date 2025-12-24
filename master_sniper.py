import requests, os, subprocess, time

class GhostStore:
    def __init__(self, token, chat_id):
        self.token, self.chat_id = token, chat_id
        self.path = os.path.expanduser("~/hacker_dropship")

    def generate_stealth_site(self, products):
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>ELITE TRENDS | Official Global Store</title>
            <script src="https://cdn.tailwindcss.com"></script>
        </head>
        <body class="bg-[#020617] text-slate-200">
            <nav class="p-8 border-b border-slate-800 flex justify-between items-center bg-[#0f172a]">
                <h1 class="text-3xl font-black text-blue-400">ELITE TRENDS</h1>
                <div class="space-x-8 text-xs font-bold uppercase tracking-widest">
                    <a href="#">New Arrivals</a><a href="#">Best Sellers</a><a href="#">Track Order</a>
                </div>
            </nav>
            <header class="py-24 text-center">
                <h2 class="text-6xl font-black mb-4">Quality. <span class="text-blue-500">Innovation.</span></h2>
                <p class="text-slate-400 text-xl">The world's most advanced gadgets, delivered to your door.</p>
            </header>
            <main class="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-12">
        """
        for p in products:
            # הקישור כאן הוא דף תשלום, לא אלי-אקספרס!
            checkout_url = f"https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business=YOUR_PAYPAL&amount={p['price']}&item_name={p['name']}"
            html += f"""
                <div class="bg-[#1e293b] rounded-3xl p-10 border border-slate-800 shadow-2xl hover:border-blue-500 transition">
                    <h3 class="text-3xl font-bold">{p['name']}</h3>
                    <p class="text-slate-400 mt-4 leading-relaxed">{p['desc']}</p>
                    <div class="mt-10 flex justify-between items-center border-t border-slate-700 pt-8">
                        <span class="text-4xl font-black text-white">${p['price']}</span>
                        <a href="{checkout_url}" class="bg-blue-600 px-8 py-4 rounded-2xl font-bold text-lg hover:bg-blue-500">Add to Cart</a>
                    </div>
                </div>"""
        html += "</main></body></html>"
        with open(f"{self.path}/index.html", "w") as f: f.write(html)

    def deploy(self):
        try:
            os.chdir(self.path)
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "Stealth Update: No AliExpress links"], check=True)
            subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
            return True
        except: return False

    def run(self):
        print("👿 הופך את האתר למותג יוקרתי (Stealth Mode)...")
        winners = [
            {"name": "MagSafe Solar Hub", "price": 49.99, "desc": "Military-grade solar power bank with 50,000mAh capacity. Fast charging for 3 devices."},
            {"name": "Cinema Pro Projector", "price": 129.00, "desc": "Native 4K smart projector with built-in Netflix and 360 sound."},
            {"name": "AutoPet Smart Feeder", "price": 89.00, "desc": "Keep your pets happy with AI-powered feeding schedules and 4K video."}
        ]
        self.generate_stealth_site(winners)
        if self.deploy():
            print("🚀 האתר מעודכן! אין יותר קישורים לאלי-אקספרס.")

if __name__ == "__main__":
    bot = GhostStore("8360823180:AAFUG7AhmzCl_6h1G_20oRgcWL8YbQ67r84", "5257373536")
    bot.run()
