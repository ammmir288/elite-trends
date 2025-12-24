import os, subprocess, time

class EmpireFinalBuilder:
    def __init__(self, token, chat_id):
        self.root = os.path.expanduser("~/hacker_dropship")
        # הגדרה מפורשת של הנתיבים למניעת שגיאות AttributeError
        self.prod_dir = os.path.join(self.root, "products")
        self.legal_dir = os.path.join(self.root, "legal")
        self.assets_dir = os.path.join(self.root, "assets")
        
        # יצירת התיקיות
        for d in [self.prod_dir, self.legal_dir, self.assets_dir]:
            os.makedirs(d, exist_ok=True)
        
        # קטלוג 12 מוצרי העל מהמחקר שלך
        self.catalog = [
            {"id": "solar-hub", "name": "MagSafe Solar Hub Pro", "cost": 101.01, "cat": "Electronics", "img": "https://ae01.alicdn.com/kf/S8f21e06d649e4860b76e105828469d44Y.jpg", "desc": "Military-grade 50,000mAh solar charging solution. Optimized for iPhone 15/16 with magnetic alignment and fast-charge technology."},
            {"id": "pet-feeder", "name": "AI Smart Pet Feeder", "cost": 60.64, "cat": "Lifestyle", "img": "https://ae01.alicdn.com/kf/Sf66649f847284b159f8a3779e5192137D.jpg", "desc": "Smartphone controlled feeding with 4K night-vision camera and AI dietary tracking. Keep them loved from anywhere."},
            {"id": "hd-projector", "name": "4K Ultra Gym Projector", "cost": 215.43, "cat": "Tech", "img": "https://ae01.alicdn.com/kf/S706cad101.jpg", "desc": "Cinema in your pocket. Native 4K, Wi-Fi 6, and 360-degree immersive sound for workouts or movie nights."},
            {"id": "rgb-hub", "name": "Smart Ambient RGB Hub", "cost": 22.90, "cat": "Home", "img": "https://ae01.alicdn.com/kf/S55443322.jpg", "desc": "16 million colors synced to your music. Smart app control for the ultimate gaming or relaxation setup."},
            {"id": "sleep-mask", "name": "Deep Sleep Bluetooth Mask", "cost": 32.10, "cat": "Lifestyle", "img": "https://ae01.alicdn.com/kf/S12345678.jpg", "desc": "Total blackout meets HD audio. Bluetooth 5.3 sleep mask designed for deep recovery and travelers."},
            {"id": "sonic-cleaner", "name": "Professional Sonic Cleaner", "cost": 18.50, "cat": "Tech", "img": "https://ae01.alicdn.com/kf/S99887766.jpg", "desc": "High-frequency ultrasonic cleaning for jewelry, watches, and lenses."},
            {"id": "portable-espresso", "name": "Nano Espresso Maker", "cost": 55.00, "cat": "Tech", "img": "https://ae01.alicdn.com/kf/S11223344.jpg", "desc": "Manual espresso machine with 18 bar pressure. Perfect crema for digital nomads."},
            {"id": "magsafe-wallet", "name": "Smart Trackable Wallet", "cost": 25.40, "cat": "Electronics", "img": "https://ae01.alicdn.com/kf/S33445566.jpg", "desc": "Leather MagSafe wallet with built-in Find My support."},
            {"id": "massager-gun", "name": "Pro Recovery Mini Gun", "cost": 45.00, "cat": "Lifestyle", "img": "https://ae01.alicdn.com/kf/S77889900.jpg", "desc": "Compact percussion massager for athletes. Quiet-torque motor."},
            {"id": "smart-tag", "name": "Elite Bluetooth Tracker", "cost": 12.00, "cat": "Electronics", "img": "https://ae01.alicdn.com/kf/S10102020.jpg", "desc": "Ultra-thin global tracker for keys and luggage."},
            {"id": "water-purifier", "name": "UV-C Self-Cleaning Bottle", "cost": 38.00, "cat": "Lifestyle", "img": "https://ae01.alicdn.com/kf/S44556677.jpg", "desc": "Insulated bottle with built-in UV-C sterilization."},
            {"id": "levitating-lamp", "name": "Anti-Gravity Moon Lamp", "cost": 75.00, "cat": "Home", "img": "https://ae01.alicdn.com/kf/S88990011.jpg", "desc": "Magnetic levitation moon lamp. A masterpiece for any modern office."}
        ]

    def get_template(self, content, title="Elite Trends", is_sub=False):
        prefix = "../" if is_sub else ""
        return f"""
        <!DOCTYPE html>
        <html lang="en" class="scroll-smooth">
        <head>
            <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{title} | Official Store</title>
            <script src="https://cdn.tailwindcss.com"></script>
            <script src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js" defer></script>
            <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
            <style>[x-cloak] {{ display: none !important; }} .glass {{ background: rgba(15, 23, 42, 0.9); backdrop-filter: blur(20px); }}</style>
        </head>
        <body class="bg-[#020617] text-white font-sans" x-data="{{ cart: 0 }}">
            <nav class="fixed w-full z-50 glass border-b border-slate-800 px-10 py-5 flex justify-between items-center">
                <a href="{prefix}index.html" class="text-3xl font-black text-blue-500 italic tracking-tighter">ELITE TRENDS</a>
                <div class="flex items-center space-x-8 text-[10px] font-bold uppercase tracking-widest text-slate-400">
                    <a href="{prefix}index.html">Home</a><button class="relative">🛒 <span x-text="cart" class="absolute -top-2 -right-2 bg-blue-600 px-2 py-0.5 rounded-full text-[8px]"></span></button>
                </div>
            </nav>
            {content}
            <footer class="py-20 border-t border-slate-800 text-center bg-[#020617]">
                <div class="flex justify-center space-x-10 mb-8 text-[10px] font-bold text-slate-500">
                    <a href="{prefix}legal/shipping.html">Shipping</a><a href="{prefix}legal/terms.html">Terms</a><a href="{prefix}legal/privacy.html">Privacy</a>
                </div>
                <p class="text-slate-700 text-[10px] uppercase tracking-[0.5em]">&copy; 2025 ELITE TRENDS GLOBAL</p>
            </footer>
            <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script><script>AOS.init();</script>
        </body></html>"""

    def build_pages(self):
        # 1. דפי מוצר נפרדים
        for p in self.catalog:
            price = round((p['cost'] / 3.7) * 2.6, 2)
            content = f"""
            <main class="max-w-7xl mx-auto pt-48 pb-20 px-6 flex flex-col md:flex-row gap-20">
                <div class="md:w-1/2 rounded-[3rem] overflow-hidden border border-slate-800"><img src="{p['img']}" class="w-full h-full object-cover"></div>
                <div class="md:w-1/2" data-aos="fade-left">
                    <span class="text-blue-500 font-bold uppercase text-xs">{p['cat']}</span>
                    <h1 class="text-6xl font-black mt-4 mb-8 leading-tight">{p['name']}</h1>
                    <p class="text-slate-400 text-xl leading-relaxed mb-10">{p['desc']}</p>
                    <div class="text-6xl font-black mb-12">${price}</div>
                    <button @click="cart++" class="w-full bg-blue-600 py-6 rounded-3xl font-black text-2xl hover:bg-blue-500 shadow-xl transition">ADD TO CART</button>
                    <div class="mt-12 grid grid-cols-2 gap-4 text-xs text-slate-500">
                        <div class="p-4 border border-slate-800 rounded-2xl text-center">✓ Free Shipping</div><div class="p-4 border border-slate-800 rounded-2xl text-center">✓ Secure Payment</div>
                    </div>
                </div>
            </main>"""
            with open(os.path.join(self.prod_dir, f"{p['id']}.html"), "w") as f: 
                f.write(self.get_template(content, p['name'], True))

        # 2. דף הבית הראשי
        home_content = """
        <header class="pt-64 pb-20 text-center px-4" data-aos="zoom-in">
            <h2 class="text-8xl font-black mb-8 leading-none">THE <span class="text-blue-600">NEW</span> ELITE.</h2>
            <p class="text-slate-400 text-xl max-w-2xl mx-auto italic">Curated viral technology for the global generation.</p>
        </header>
        <main class="max-w-7xl mx-auto px-6 py-20 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">"""
        for p in self.catalog:
            price = round((p['cost'] / 3.7) * 2.6, 2)
            home_content += f"""
            <div class="bg-[#0f172a] rounded-[2.5rem] border border-slate-800 overflow-hidden group hover:border-blue-500 transition-all shadow-2xl" data-aos="fade-up">
                <img src="{p['img']}" class="h-48 w-full object-cover group-hover:scale-105 transition duration-500">
                <div class="p-8">
                    <h3 class="text-xl font-bold mb-6 h-12 line-clamp-2">{p['name']}</h3>
                    <div class="flex justify-between items-center border-t border-slate-800 pt-6">
                        <span class="text-2xl font-black">${price}</span>
                        <a href="products/{p['id']}.html" class="bg-blue-600 px-6 py-2 rounded-xl text-xs font-bold hover:bg-blue-500">VIEW</a>
                    </div>
                </div>
            </div>"""
        with open(os.path.join(self.root, "index.html"), "w") as f: 
            f.write(self.get_template(home_content + "</main>"))

        # 3. דפים משפטיים
        for legal in ["shipping", "terms", "privacy"]:
            path = os.path.join(self.legal_dir, f"{legal}.html")
            content = f"<main class='max-w-3xl mx-auto pt-48 pb-40 px-6'><h1 class='text-4xl font-black mb-10 capitalize'>{legal} Policy</h1><p class='text-slate-400 leading-relaxed'>Professional {legal} policy for Elite Trends customers.</p></main>"
            with open(path, "w") as f: 
                f.write(self.get_template(content, legal.capitalize(), True))

    def check_and_deploy(self):
        print("👿 בודק תקינות מערכת (Self-Check)...")
        index_exists = os.path.exists(os.path.join(self.root, "index.html"))
        products_ready = len(os.listdir(self.prod_dir)) >= 12
        
        if index_exists and products_ready:
            print("✅ בדיקה עברה: הקניון הדיגיטלי מוכן לשיגור.")
            os.chdir(self.root)
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "Final Enterprise Mall Build v28"], capture_output=True)
            subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
            print("🚀 שיגור סופי ל-GitHub הושלם! האימפריה באוויר.")
        else:
            print("❌ שגיאה בבנייה. וודא שאין קבצים פתוחים ב-Kali.")

    def run(self):
        print("👿 המפלצת בונה כעת את האימפריה השלמה שלך...")
        self.build_pages()
        self.check_and_deploy()

if __name__ == "__main__":
    # שימוש בטוקן ובשם המשתמש ammmir288 מהחיבור הקודם
    bot = EmpireFinalBuilder("8360823180:AAFUG7AhmzCl_6h1G_20oRgcWL8YbQ67r84", "5257373536")
    bot.run()
