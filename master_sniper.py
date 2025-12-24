import requests, os, subprocess, time

class InteractiveBrand:
    def __init__(self, token, chat_id):
        self.token, self.chat_id = token, chat_id
        self.path = os.path.expanduser("~/hacker_dropship")

    def generate_interactive_site(self, products):
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>ELITE TRENDS | Official Store</title>
            <script src="https://cdn.tailwindcss.com"></script>
            <script src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js" defer></script>
            <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
        </head>
        <body class="bg-[#020617] text-white" x-data="{{ openModal: false, activeProduct: {{}} }}">
            
            <nav class="p-6 border-b border-slate-800 flex justify-between items-center bg-[#0f172a]/80 backdrop-blur-md fixed w-full z-50">
                <h1 class="text-2xl font-black text-blue-500 italic">ELITE TRENDS</h1>
                <div class="flex space-x-4">
                    <span class="text-[10px] bg-red-500 px-2 py-1 rounded-full animate-pulse">LIVE DEALS</span>
                </div>
            </nav>

            <header class="pt-40 pb-20 text-center px-6">
                <h2 class="text-6xl font-black mb-4" data-aos="fade-down">Future Tech, <span class="text-blue-500">Today.</span></h2>
                <p class="text-slate-400">Exclusive viral products curated for the elite.</p>
            </header>

            <main class="max-w-7xl mx-auto px-6 py-10 grid grid-cols-1 md:grid-cols-3 gap-10">
        """
        for p in products:
            html += f"""
                <div class="bg-[#0f172a] rounded-[2rem] p-8 border border-slate-800 hover:border-blue-500 transition-all group" data-aos="fade-up">
                    <span class="text-blue-400 text-[10px] font-bold uppercase">{p['category']}</span>
                    <h3 class="text-2xl font-bold mt-2">{p['name']}</h3>
                    <p class="text-slate-500 text-sm mt-4 line-clamp-2">{p['desc']}</p>
                    <div class="mt-8 flex justify-between items-center">
                        <span class="text-3xl font-black">${p['price']}</span>
                        <button @click="openModal = true; activeProduct = {{ name: '{p['name']}', price: '{p['price']}', desc: '{p['desc']}', category: '{p['category']}' }}" 
                                class="bg-blue-600 px-6 py-3 rounded-xl font-bold hover:bg-blue-500 transition">
                            VIEW DETAILS
                        </button>
                    </div>
                </div>"""
        
        html += """
            </main>

            <div x-show="openModal" class="fixed inset-0 z-[100] flex items-center justify-center p-6 bg-black/90 backdrop-blur-sm" x-cloak>
                <div class="bg-[#0f172a] max-w-2xl w-full rounded-[3rem] p-12 border border-slate-700 relative shadow-2xl" @click.away="openModal = false">
                    <button @click="openModal = false" class="absolute top-8 right-8 text-slate-500 hover:text-white text-2xl">&times;</button>
                    
                    <span class="text-blue-400 text-xs font-black uppercase tracking-widest" x-text="activeProduct.category"></span>
                    <h2 class="text-5xl font-black mt-4 mb-6" x-text="activeProduct.name"></h2>
                    <p class="text-slate-400 text-lg leading-relaxed mb-10" x-text="activeProduct.desc"></p>
                    
                    <div class="bg-blue-900/20 p-6 rounded-2xl border border-blue-500/30 mb-10">
                        <p class="text-blue-400 text-sm font-bold">⚡ LIMITED STOCK: Only 4 units left in our US warehouse!</p>
                    </div>

                    <div class="flex justify-between items-center">
                        <span class="text-5xl font-black" x-text="'$' + activeProduct.price"></span>
                        <button class="bg-white text-black px-12 py-5 rounded-2xl font-black text-xl hover:bg-blue-500 hover:text-white transition-all">
                            PROCEED TO SECURE CHECKOUT
                        </button>
                    </div>
                </div>
            </div>

            <footer class="py-20 text-center text-slate-700 text-[10px] font-bold uppercase tracking-widest">
                &copy; 2025 ELITE TRENDS GLOBAL. ALL RIGHTS RESERVED.
            </footer>

            <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
            <script>AOS.init();</script>
        </body>
        </html>
        """
        with open(f"{self.path}/index.html", "w", encoding="utf-8") as f: f.write(html)

    def deploy(self):
        try:
            os.chdir(self.path)
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "Interactive Modal Update"], check=True)
            subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
            return True
        except: return False

    def run(self):
        print("👿 הופך את האתר לאינטראקטיבי (Adding Product Modals)...")
        winners = [
            {"name": "MagSafe Solar Hub", "price": 49.99, "category": "Electronics", "desc": "The most powerful solar bank for 2025. Features magnetic alignment, 50,000mAh capacity, and military-grade durability."},
            {"name": "Smart AI Pet Feeder", "price": 89.00, "category": "Lifestyle", "desc": "Keep your pets healthy and happy. Smart AI schedules, 4K camera monitoring, and instant alerts to your phone."},
            {"name": "Ultra-HD Gym Projector", "price": 120.50, "category": "Tech", "desc": "Experience true 4K cinema anywhere. Ultra-portable, Wi-Fi 6 enabled, and connects directly to your favorite streaming apps."}
        ]
        self.generate_interactive_site(winners)
        if self.deploy():
            print("🚀 האתר שודרג! עכשיו כשלוחצים על מוצר נפתח עולם שלם.")

if __name__ == "__main__":
    InteractiveBrand("8360823180:AAFUG7AhmzCl_6h1G_20oRgcWL8YbQ67r84", "5257373536").run()
