import os, subprocess, time, json

class EnterpriseEngineV26:
    def __init__(self, token, chat_id):
        self.token, self.chat_id = token, chat_id
        self.root = os.path.expanduser("~/hacker_dropship")
        self.prod_dir = os.path.join(self.root, "products")
        os.makedirs(self.prod_dir, exist_ok=True)
        
        # ניהול מוצרים - קל להוסיף כאן עוד 100 מוצרים
        self.catalog = [
            {"id": "solar-hub", "name": "MagSafe Solar Hub Pro", "cost": 101.01, "cat": "Electronics", "img": "https://ae01.alicdn.com/kf/S8f21e06d649e4860b76e105828469d44Y.jpg", "desc": "Next-gen 50,000mAh solar charging for elite explorers. Rugged, magnetic, and waterproof."},
            {"id": "pet-feeder", "name": "AI Smart Pet Feeder", "cost": 60.64, "cat": "Lifestyle", "img": "https://ae01.alicdn.com/kf/Sf66649f847284b159f8a3779e5192137D.jpg", "desc": "Smartphone controlled feeding with 4K camera and AI dietary tracking."},
            {"id": "hd-projector", "name": "Ultra-HD Gym Projector", "cost": 215.43, "cat": "Tech", "img": "https://ae01.alicdn.com/kf/S706cad101.jpg", "desc": "Cinema in your pocket. Native 4K, Wi-Fi 6, and 360-degree immersive sound."},
            {"id": "sleep-mask", "name": "Deep Sleep Bluetooth Mask", "cost": 32.10, "cat": "Lifestyle", "img": "https://ae01.alicdn.com/kf/S12345678.jpg", "desc": "Total blackout with HD audio. Perfect for recovery and travel."},
            {"id": "rgb-lamp", "name": "Smart Ambient RGB Hub", "cost": 22.90, "cat": "Home", "img": "https://ae01.alicdn.com/kf/S55443322.jpg", "desc": "Sync your room with your music. 16M colors with smart app control."}
        ]

    def get_header(self, title, is_sub=False):
        prefix = "../" if is_sub else ""
        return f"""
        <!DOCTYPE html>
        <html lang="en" class="scroll-smooth">
        <head>
            <meta charset="UTF-8"><title>{title} | Elite Trends Official</title>
            <script src="https://cdn.tailwindcss.com"></script>
            <script src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js" defer></script>
            <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
            <style>[x-cloak] {{ display: none !important; }} .glass {{ background: rgba(15, 23, 42, 0.9); backdrop-filter: blur(20px); }}</style>
        </head>
        <body class="bg-[#020617] text-white font-sans" x-data="{{ cart: 0, openCart: false }}">
            <nav class="fixed w-full z-50 glass border-b border-slate-800 px-10 py-5 flex justify-between items-center">
                <a href="{prefix}index.html" class="text-3xl font-black text-blue-500 italic tracking-tighter">ELITE TRENDS</a>
                <div class="flex items-center space-x-8">
                    <button @click="openCart = true" class="relative text-xl">🛒 <span x-text="cart" class="absolute -top-2 -right-2 bg-blue-600 text-[10px] px-2 py-0.5 rounded-full font-bold"></span></button>
                </div>
            </nav>
        """

    def generate_product_pages(self):
        for p in self.catalog:
            price = round((p['cost'] / 3.7) * 2.6, 2)
            html = self.get_header(p['name'], True) + f"""
            <main class="max-w-7xl mx-auto pt-40 pb-20 px-6 flex flex-col md:flex-row gap-20">
                <div class="md:w-1/2 rounded-[3rem] overflow-hidden border border-slate-800"><img src="{p['img']}" class="w-full h-full object-cover"></div>
                <div class="md:w-1/2">
                    <span class="text-blue-500 font-bold uppercase tracking-widest text-xs">{p['cat']}</span>
                    <h1 class="text-6xl font-black mt-4 mb-8">{p['name']}</h1>
                    <p class="text-slate-400 text-xl leading-relaxed mb-10">{p['desc']}</p>
                    <div class="text-6xl font-black mb-12">${price}</div>
                    <button @click="cart++" class="w-full bg-blue-600 py-6 rounded-3xl font-black text-2xl hover:bg-blue-500 shadow-xl transition">ADD TO CART</button>
                    <div class="mt-12 p-8 border border-slate-800 rounded-3xl bg-slate-900/50">
                        <h4 class="font-bold mb-4">Why shop with us?</h4>
                        <ul class="text-slate-400 space-y-2 text-sm"><li>✓ Insured Global Shipping</li><li>✓ 24/7 Concierge Support</li><li>✓ 30-Day Money Back Guarantee</li></ul>
                    </div>
                </div>
            </main>
            </body></html>"""
            with open(f"{self.prod_dir}/{p['id']}.html", "w", encoding="utf-8") as f: f.write(html)

    def generate_index(self):
        html = self.get_header("Official Mall") + """
        <header class="pt-56 pb-20 text-center px-4" x-data="{ search: '' }">
            <h2 class="text-8xl font-black mb-8 leading-none" data-aos="fade-up">CURATED <span class="text-blue-600">VIRAL</span> TECH.</h2>
            <div class="max-w-xl mx-auto mt-10"><input type="text" x-model="search" placeholder="Search our 2025 collection..." class="w-full bg-slate-900 border border-slate-800 p-5 rounded-2xl focus:border-blue-500 outline-none"></div>
        </header>
        <main class="max-w-7xl mx-auto px-6 py-20 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-12" x-data="{ category: 'All' }">"""
        
        for p in self.catalog:
            price = round((p['cost'] / 3.7) * 2.6, 2)
            html += f"""
            <div class="bg-[#0f172a] rounded-[3rem] border border-slate-800 overflow-hidden group hover:border-blue-500 transition-all shadow-2xl" data-aos="fade-up">
                <img src="{p['img']}" class="h-64 w-full object-cover group-hover:scale-105 transition duration-500">
                <div class="p-10">
                    <h3 class="text-2xl font-bold mb-8">{p['name']}</h3>
                    <div class="flex justify-between items-center border-t border-slate-800 pt-8">
                        <span class="text-4xl font-black">${price}</span>
                        <a href="products/{p['id']}.html" class="bg-blue-600 px-8 py-4 rounded-2xl font-bold hover:bg-blue-500 transition">VIEW ITEM</a>
                    </div>
                </div>
            </div>"""
        
        html += "</main><script src='https://unpkg.com/aos@2.3.1/dist/aos.js'></script><script>AOS.init();</script></body></html>"
        with open(f"{self.root}/index.html", "w", encoding="utf-8") as f: f.write(html)

    def deploy(self):
        os.chdir(self.root)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "V26: Full Enterprise Mall Deployment"], capture_output=True)
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)

    def run(self):
        print("👿 ה-Empire Engine V26 התחיל בבניית החברה שלך...")
        self.generate_index()
        self.generate_product_pages()
        self.deploy()
        print("🚀 החברה באוויר! דף בית מקצועי ודפי מוצר אישיים מעודכנים ב-GitHub.")

if __name__ == "__main__":
    bot = EnterpriseEngineV26("8360823180:AAFUG7AhmzCl_6h1G_20oRgcWL8YbQ67r84", "5257373536")
    bot.run()
