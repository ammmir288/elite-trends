import os, subprocess, time

class EliteFocusBuilder:
    def __init__(self, token, chat_id):
        self.root = os.path.expanduser("~/hacker_dropship")
        self.prod_dir = os.path.join(self.root, "products")
        os.makedirs(self.prod_dir, exist_ok=True)
        
        # התמקדות במוצר אחד בלבד כפי שביקשת
        self.focus_product = {
            "id": "solar-hub",
            "name": "MagSafe Solar Hub Pro",
            "cost_nis": 101.01,
            "cat": "Electronics",
            "img": "https://ae01.alicdn.com/kf/S8f21e06d649e4860b76e105828469d44Y.jpg",
            "desc": "The 2025 standard for off-grid power. Featuring 50,000mAh capacity, military-grade ruggedness, and advanced MagSafe magnetic alignment for iPhone 15/16 series."
        }

    def get_layout(self, content, title="Elite Trends", is_sub=False):
        prefix = "../" if is_sub else ""
        return f"""
        <!DOCTYPE html>
        <html lang="en" class="scroll-smooth">
        <head>
            <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{title} | Elite Trends</title>
            <script src="https://cdn.tailwindcss.com"></script>
            <script src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js" defer></script>
            <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
            <style>
                [x-cloak] {{ display: none !important; }}
                .glass {{ background: rgba(15, 23, 42, 0.8); backdrop-filter: blur(20px); }}
                .text-gradient {{ background: linear-gradient(to right, #60a5fa, #3b82f6); -webkit-background-clip: text; color: transparent; }}
            </style>
        </head>
        <body class="bg-[#020617] text-white font-sans" x-data="{{ cart: 0, openLogin: false }}">
            <nav class="fixed w-full z-50 glass border-b border-slate-800 px-10 py-6 flex justify-between items-center">
                <a href="{prefix}index.html" class="text-3xl font-black text-blue-500 italic tracking-tighter">ELITE TRENDS</a>
                <div class="flex items-center space-x-10 text-[10px] font-bold uppercase tracking-[0.2em] text-slate-400">
                    <a href="{prefix}index.html" class="hover:text-blue-500">Collection</a>
                    <button @click="openLogin = true" class="bg-white text-black px-6 py-2 rounded-full hover:bg-blue-500 hover:text-white transition">Google Login</button>
                    <div class="relative">🛒 <span x-text="cart" class="absolute -top-2 -right-2 bg-blue-600 px-2 py-0.5 rounded-full text-[8px]"></span></div>
                </div>
            </nav>
            {content}
            <footer class="py-20 text-center border-t border-slate-900 bg-[#020617]">
                <p class="text-slate-700 text-[10px] font-bold uppercase tracking-[0.5em]">&copy; 2025 ELITE TRENDS GLOBAL</p>
            </footer>
            <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script><script>AOS.init();</script>
        </body></html>"""

    def build_store(self):
        # 1. דף הבית (Main Hub) - עיצוב הייטק נקי
        p = self.focus_product
        price = round((p['cost_nis'] / 3.7) * 2.6, 2)
        home_content = f"""
        <header class="h-screen flex flex-col justify-center items-center text-center px-6 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-slate-900 to-black">
            <h2 class="text-8xl md:text-9xl font-black mb-8 leading-none" data-aos="zoom-out">THE <span class="text-gradient">NEW</span> ELITE.</h2>
            <p class="text-slate-400 text-xl max-w-2xl mx-auto mb-12">Curated viral technology for the global generation.</p>
            <a href="#product" class="bg-blue-600 px-12 py-5 rounded-full font-black text-lg shadow-2xl shadow-blue-500/20 hover:scale-110 transition">EXPLORE PRODUCT</a>
        </header>

        <section id="product" class="max-w-7xl mx-auto px-6 py-40">
            <div class="bg-[#0f172a] rounded-[4rem] overflow-hidden border border-slate-800 flex flex-col md:flex-row shadow-2xl" data-aos="fade-up">
                <div class="md:w-1/2 h-[500px]"><img src="{p['img']}" class="w-full h-full object-cover"></div>
                <div class="md:w-1/2 p-20 flex flex-col justify-center">
                    <span class="text-blue-500 font-bold uppercase text-xs tracking-widest">{p['cat']}</span>
                    <h3 class="text-5xl font-black mt-4 mb-8">{p['name']}</h3>
                    <p class="text-slate-400 text-lg leading-relaxed mb-12">{p['desc']}</p>
                    <div class="flex justify-between items-center border-t border-slate-800 pt-10">
                        <span class="text-5xl font-black">${price}</span>
                        <a href="products/{p['id']}.html" class="bg-white text-black px-12 py-5 rounded-3xl font-black text-xl hover:bg-blue-500 hover:text-white transition">VIEW DETAILS</a>
                    </div>
                </div>
            </div>
        </section>"""
        with open(os.path.join(self.root, "index.html"), "w", encoding="utf-8") as f:
            f.write(self.get_layout(home_content))

        # 2. דף מוצר נפרד (The Focus Page)
        prod_content = f"""
        <main class="max-w-7xl mx-auto pt-48 pb-40 px-6 flex flex-col md:flex-row gap-20">
            <div class="md:w-1/2 rounded-[3.5rem] overflow-hidden border border-slate-800 shadow-2xl"><img src="{p['img']}" class="w-full h-full object-cover"></div>
            <div class="md:w-1/2" data-aos="fade-left">
                <span class="text-blue-500 font-bold uppercase text-xs">OFFICIAL PRODUCT</span>
                <h1 class="text-7xl font-black mt-6 mb-10 leading-tight">{p['name']}</h1>
                <p class="text-slate-400 text-xl leading-relaxed mb-12">{p['desc']}</p>
                <div class="text-7xl font-black mb-14 text-gradient">${price}</div>
                <button @click="cart++" class="w-full bg-blue-600 py-8 rounded-[2.5rem] font-black text-3xl shadow-2xl shadow-blue-500/20 hover:bg-blue-500 transition">ORDER NOW</button>
                <div class="mt-16 grid grid-cols-2 gap-6 text-slate-500 font-bold text-xs uppercase tracking-widest">
                    <div class="p-6 border border-slate-800 rounded-3xl text-center">✓ 7-Day Shipping</div><div class="p-6 border border-slate-800 rounded-3xl text-center">✓ Secure Auth</div>
                </div>
            </div>
        </main>"""
        with open(os.path.join(self.prod_dir, f"{p['id']}.html"), "w", encoding="utf-8") as f:
            f.write(self.get_layout(prod_content, p['name'], True))

    def deploy(self):
        os.chdir(self.root)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "V32: Design Finalized & Focused on Single Product"], capture_output=True)
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)

    def run(self):
        print("👿 ה-Elite Builder בונה כעת את העיצוב הסופי והמוצר הנבחר...")
        self.build_store()
        self.deploy()
        print("🚀 האימפריה חזרה! העיצוב מושלם והמוצר באוויר ב-GitHub.")

if __name__ == "__main__":
    bot = EliteFocusBuilder("8360823180:AAFUG7AhmzCl_6h1G_20oRgcWL8YbQ67r84", "5257373536")
    bot.run()
