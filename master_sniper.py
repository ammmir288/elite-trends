import requests, os, subprocess, time

class MegaFactory:
    def __init__(self, token, chat_id):
        self.token, self.chat_id = token, chat_id
        self.path = os.path.expanduser("~/hacker_dropship")
        # בסיס נתונים מורחב של מוצרים ויראליים ל-2025
        self.catalog = [
            {"name": "MagSafe Solar Hub v2", "cost": 101.01, "cat": "Electronics", "img": "https://ae01.alicdn.com/kf/S8f21e06d649e4860b76e105828469d44Y.jpg", "desc": "50,000mAh military-grade solar bank. Features triple-coil magnetic alignment and IP68 waterproof rating for extreme outdoor use."},
            {"name": "AI Smart Pet Feeder Pro", "cost": 60.64, "cat": "Lifestyle", "img": "https://ae01.alicdn.com/kf/Sf66649f847284b159f8a3779e5192137D.jpg", "desc": "Automated feeding with 4K night-vision camera. Includes two-way audio to talk to your pets and AI portion control."},
            {"name": "4K Ultra-Gym Projector", "cost": 215.43, "cat": "Tech", "img": "https://ae01.alicdn.com/kf/S706cad101.jpg", "desc": "Native 4K resolution in a pocket size. Wi-Fi 6 enabled for lag-free streaming of workouts and movies anywhere."},
            {"name": "Magnetic Wireless Power-Bank", "cost": 45.20, "cat": "Electronics", "img": "https://ae01.alicdn.com/kf/S87654321.jpg", "desc": "Ultra-slim 10k mAh magnetic charger. Fits perfectly on iPhone 12-16 series."},
            {"name": "Smart Sleep Mask v4", "cost": 32.10, "cat": "Lifestyle", "img": "https://ae01.alicdn.com/kf/S12345678.jpg", "desc": "Bluetooth 5.3 sleep mask with HD speakers. Zero pressure on eyes, 100% blackout guaranteed."},
            {"name": "Electric Sonic Cleaner", "cost": 18.50, "cat": "Home", "img": "https://ae01.alicdn.com/kf/S99887766.jpg", "desc": "High-frequency ultrasonic cleaner for jewelry, glasses, and watches. Professional results at home."},
            {"name": "RGB Atmosphere Lamp", "cost": 22.90, "cat": "Home", "img": "https://ae01.alicdn.com/kf/S55443322.jpg", "desc": "Smart app-controlled RGB lamp. Syncs with music and features 16 million colors for the perfect setup."},
            {"name": "Portable Espresso Maker", "cost": 55.00, "cat": "Tech", "img": "https://ae01.alicdn.com/kf/S11223344.jpg", "desc": "Handheld espresso machine for travelers. 18 bar pressure for rich crema anywhere you go."}
        ]

    def build_site(self):
        """מייצר אתר מרובה מוצרים עם דפי מוצר (Modals) עשירים בתוכן ותמונות"""
        html_head = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8"><title>Elite Trends | 2025 Global Mall</title>
            <script src="https://cdn.tailwindcss.com"></script>
            <script src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js" defer></script>
            <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
            <style>[x-cloak] { display: none !important; } .glass { background: rgba(15, 23, 42, 0.9); backdrop-filter: blur(20px); }</style>
        </head>
        <body class="bg-[#020617] text-white" x-data="{ open: false, activeP: {}, cat: 'All' }">
            <nav class="fixed w-full z-50 glass border-b border-slate-800 px-10 py-6 flex justify-between items-center">
                <h1 class="text-3xl font-black text-blue-500 italic">ELITE TRENDS</h1>
                <div class="flex space-x-6 text-[10px] font-bold uppercase tracking-widest text-slate-400">
                    <button @click="cat = 'All'" :class="cat === 'All' ? 'text-blue-400' : ''">All</button>
                    <button @click="cat = 'Electronics'" :class="cat === 'Electronics' ? 'text-blue-400' : ''">Electronics</button>
                    <button @click="cat = 'Lifestyle'" :class="cat === 'Lifestyle' ? 'text-blue-400' : ''">Lifestyle</button>
                    <button @click="cat = 'Home'" :class="cat === 'Home' ? 'text-blue-400' : ''">Home</button>
                </div>
            </nav>
            <header class="pt-48 pb-10 text-center px-4">
                <h2 class="text-6xl md:text-8xl font-black mb-6 leading-tight" data-aos="zoom-in">VIRAL CURATED.<br><span class="text-blue-600">ZERO EFFORT.</span></h2>
                <p class="text-slate-400 text-xl italic max-w-2xl mx-auto">Global technology, premium lifestyle gadgets, and home innovation.</p>
            </header>
            <main class="max-w-7xl mx-auto px-6 py-20 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">"""
        
        cards = ""
        for p in self.catalog:
            price = round((p['cost'] / 3.7) * 2.5, 2)
            cards += f"""
                <div class="bg-[#0f172a] rounded-[2.5rem] border border-slate-800 overflow-hidden hover:border-blue-500 transition-all group" 
                     x-show="cat === 'All' || cat === '{p['cat']}'" data-aos="fade-up">
                    <div class="h-48 overflow-hidden bg-slate-800">
                        <img src="{p['img']}" class="w-full h-full object-cover group-hover:scale-110 transition duration-500" onerror="this.src='https://via.placeholder.com/300x200?text=Product+Image'">
                    </div>
                    <div class="p-8">
                        <span class="text-blue-400 text-[9px] font-black uppercase tracking-widest">{p['cat']}</span>
                        <h3 class="text-xl font-bold mt-2 h-14 line-clamp-2">{p['name']}</h3>
                        <div class="mt-6 flex justify-between items-center border-t border-slate-800 pt-6">
                            <span class="text-2xl font-black">${price}</span>
                            <button @click="open = true; activeP = {{name:'{p['name']}', price:'{price}', desc:'{p['desc']}', img:'{p['img']}', cat:'{p['cat']}'}}" 
                                    class="bg-blue-600 px-4 py-2 rounded-xl text-xs font-bold hover:bg-blue-500">DETAILS</button>
                        </div>
                    </div>
                </div>"""
        
        modal = """
            </main>
            <div x-show="open" x-cloak class="fixed inset-0 z-[100] flex items-center justify-center p-4 bg-black/95 backdrop-blur-md">
                <div class="bg-[#0f172a] max-w-4xl w-full rounded-[4rem] flex flex-col md:flex-row border border-slate-700 overflow-hidden shadow-2xl" @click.away="open = false">
                    <div class="md:w-1/2 h-64 md:h-auto bg-slate-800">
                        <img :src="activeP.img" class="w-full h-full object-cover">
                    </div>
                    <div class="p-12 md:w-1/2 relative">
                        <button @click="open = false" class="absolute top-8 right-8 text-slate-500 text-4xl">&times;</button>
                        <span class="text-blue-500 text-xs font-black uppercase tracking-widest" x-text="activeP.cat"></span>
                        <h2 class="text-5xl font-black mt-4 mb-8 leading-tight" x-text="activeP.name"></h2>
                        <p class="text-slate-400 text-lg leading-relaxed mb-10" x-text="activeP.desc"></p>
                        <div class="flex justify-between items-center border-t border-slate-800 pt-10">
                            <span class="text-5xl font-black" x-text="'$' + activeP.price"></span>
                            <button class="bg-white text-black px-12 py-5 rounded-[2rem] font-black text-xl hover:bg-blue-600 hover:text-white transition">BUY NOW</button>
                        </div>
                    </div>
                </div>
            </div>
            <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
            <script>AOS.init({ duration: 1000, once: true });</script>
        </body></html>"""
        
        with open(f"{self.path}/index.html", "w") as f: f.write(html_head + cards + modal)

    def deploy(self):
        os.chdir(self.path)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Mega-Mall Update: 12 Products with Images & Full Details"], capture_output=True)
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)

    def run(self):
        print("👿 ה-Mega-Factory התחיל לעבוד. בונה את הקניון הדיגיטלי שלך...")
        self.build_site()
        self.deploy()
        print("🚀 הכל מוכן! האתר שלך עכשיו מלא במוצרים, תמונות ותוכן שיווקי.")

if __name__ == "__main__":
    bot = MegaFactory("8360823180:AAFUG7AhmzCl_6h1G_20oRgcWL8YbQ67r84", "5257373536")
    bot.run()
