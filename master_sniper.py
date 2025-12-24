import requests, os, subprocess

class EmpireMegaUpgrade:
    def __init__(self, token, chat_id):
        self.token, self.chat_id = token, chat_id
        self.path = os.path.expanduser("~/hacker_dropship")

    def generate_pro_site(self, products):
        # אתר משודרג עם AOS (אנימציות) ו-Alpine.js (לוגיקה של קטגוריות)
        html = f"""
        <!DOCTYPE html>
        <html lang="en" class="scroll-smooth">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Elite Trends | Global 2025</title>
            <script src="https://cdn.tailwindcss.com"></script>
            <script src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js" defer></script>
            <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
            <style>
                .glass {{ background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); }}
                .gradient-text {{ background: linear-gradient(90deg, #60a5fa, #34d399); -webkit-background-clip: text; color: transparent; }}
            </style>
        </head>
        <body class="bg-[#020617] text-slate-200" x-data="{{ category: 'All' }}">
            <nav class="fixed w-full z-50 glass border-b border-slate-800 p-5 flex justify-between items-center">
                <h1 class="text-2xl font-black gradient-text italic">ELITE TRENDS</h1>
                <div class="flex space-x-6 text-xs font-bold uppercase tracking-widest">
                    <button @click="category = 'All'" :class="category === 'All' ? 'text-blue-400' : ''">All</button>
                    <button @click="category = 'Electronics'" :class="category === 'Electronics' ? 'text-blue-400' : ''">Electronics</button>
                    <button @click="category = 'Tech'" :class="category === 'Tech' ? 'text-blue-400' : ''">Tech</button>
                </div>
            </nav>

            <header class="h-screen flex flex-col justify-center items-center text-center px-6">
                <h2 class="text-7xl font-black mb-6" data-aos="zoom-in">THE FUTURE OF <br><span class="gradient-text">SHOPPING</span></h2>
                <p class="text-slate-400 text-xl max-w-xl" data-aos="fade-up" data-aos-delay="200">AI-Curated viral trends from across the globe, delivered to your door.</p>
                <a href="#store" class="mt-10 bg-blue-600 px-10 py-4 rounded-full font-bold shadow-lg shadow-blue-500/20 hover:scale-105 transition">Explore Now</a>
            </header>

            <main id="store" class="max-w-7xl mx-auto px-6 py-24 grid grid-cols-1 md:grid-cols-3 gap-12">
        """
        for p in products:
            html += f"""
                <div class="group relative" x-show="category === 'All' || category === '{p['category']}'" data-aos="fade-up">
                    <div class="absolute -inset-1 bg-gradient-to-r from-blue-600 to-emerald-600 rounded-3xl blur opacity-25 group-hover:opacity-100 transition duration-1000"></div>
                    <div class="relative bg-[#0f172a] rounded-3xl p-8 border border-slate-800">
                        <div class="flex justify-between items-center mb-6">
                            <span class="text-[10px] font-black text-emerald-400 uppercase tracking-widest bg-emerald-400/10 px-3 py-1 rounded-full">{p['category']}</span>
                            <span class="text-slate-500 text-xs">#2025_TREND</span>
                        </div>
                        <h3 class="text-2xl font-bold mb-4">{p['name']}</h3>
                        <p class="text-slate-400 text-sm mb-8 leading-relaxed">{p['desc']}</p>
                        <div class="flex justify-between items-center">
                            <span class="text-3xl font-black text-white">${p['price']}</span>
                            <a href="{p['buy_link']}" target="_blank" class="bg-white text-black px-6 py-3 rounded-xl font-bold hover:bg-blue-400 transition">Get It Now</a>
                        </div>
                    </div>
                </div>"""
        
        html += """
            </main>
            <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
            <script>AOS.init({ duration: 1000, once: true });</script>
        </body>
        </html>
        """
        with open(f"{self.path}/index.html", "w", encoding="utf-8") as f: f.write(html)

    def deploy(self):
        try:
            os.chdir(self.path)
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "Mega Upgrade: Animations & Filters"], check=True)
            subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
            return True
        except: return False

    def run(self):
        # מוצרים אמיתיים מהמחקר שלך עם קישורים
        winners = [
            {"name": "MagSafe Solar Hub", "price": 49.99, "category": "Electronics", "desc": "Charge your iPhone 15/16 anywhere with next-gen solar technology.", "buy_link": "https://www.aliexpress.com/wholesale?SearchText=solar+power+bank+magsafe"},
            {"name": "4K Smart Mini Projector", "price": 120.50, "category": "Tech", "desc": "Crystal clear cinema in your pocket. Connects to everything.", "buy_link": "https://www.aliexpress.com/wholesale?SearchText=4k+mini+projector"},
            {"name": "Automatic AI Pet Feeder", "price": 89.00, "category": "Tech", "desc": "Smart scheduling and 4K camera for your pets while you're away.", "buy_link": "https://www.aliexpress.com/wholesale?SearchText=smart+pet+feeder"}
        ]
        self.generate_pro_site(winners)
        if self.deploy():
            print("🚀 המפלצת שודרגה! האתר חי, זז ומוכר בשידור חי!")

if __name__ == "__main__":
    GlobalEmpire = EmpireMegaUpgrade("8360823180:AAFUG7AhmzCl_6h1G_20oRgcWL8YbQ67r84", "5257373536")
    GlobalEmpire.run()
