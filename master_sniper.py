import requests, os, subprocess, time

class EliteEmpireMaster:
    def __init__(self, token, chat_id):
        self.token, self.chat_id = token, chat_id
        self.path = os.path.expanduser("~/hacker_dropship")
        # דאטה אמיתי מהחיפושים שלך
        self.raw_data = [
            {"name": "MagSafe Solar Hub", "cost_nis": 101.01, "cat": "Electronics", "stars": 5},
            {"name": "Smart AI Pet Feeder", "cost_nis": 60.64, "cat": "Lifestyle", "stars": 4},
            {"name": "Ultra-HD Gym Projector", "cost_nis": 215.43, "cat": "Tech", "stars": 5}
        ]

    def get_desc(self, name):
        descs = {
            "MagSafe Solar Hub": "Military-grade 50,000mAh power bank. Features advanced magnetic solar cells for the ultimate off-grid experience. Compatible with iPhone 15/16 and all USB-C devices.",
            "Smart AI Pet Feeder": "Keep your pets loved even when you're away. Featuring 4K camera monitoring, two-way audio, and AI-driven portion control directly from your smartphone.",
            "Ultra-HD Gym Projector": "Turn any wall into a 200-inch 4K theater. Wi-Fi 6 enabled for seamless streaming. The perfect companion for home gym workouts and cinematic nights."
        }
        return descs.get(name, "Premium tech accessory designed for the 2025 global market.")

    def generate_html(self):
        products = []
        for item in self.raw_data:
            # המרת שקלים לדולרים + רווח מותגי (Multiplied for premium feel)
            price = round((item['cost_nis'] / 3.7) * 2.2, 2)
            products.append({**item, "price": price, "desc": self.get_desc(item['name'])})

        html = f"""
        <!DOCTYPE html>
        <html lang="en" class="scroll-smooth">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Elite Trends | Future Tech Today</title>
            <script src="https://cdn.tailwindcss.com"></script>
            <script src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js" defer></script>
            <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
            <style>
                [x-cloak] {{ display: none !important; }}
                .glass {{ background: rgba(15, 23, 42, 0.7); backdrop-filter: blur(15px); }}
                .hero-gradient {{ background: radial-gradient(circle at center, #1e293b 0%, #020617 100%); }}
                .glow-border {{ transition: 0.3s; border: 1px solid rgba(59, 130, 246, 0.2); }}
                .glow-border:hover {{ border-color: #3b82f6; box-shadow: 0 0 20px rgba(59, 130, 246, 0.4); }}
            </style>
        </head>
        <body class="bg-[#020617] text-slate-100 font-sans" x-data="{{ open: false, activeP: {{}}, category: 'All' }}">
            
            <nav class="fixed w-full z-[100] glass border-b border-slate-800 px-10 py-6 flex justify-between items-center">
                <h1 class="text-3xl font-black text-blue-500 italic tracking-tighter">ELITE TRENDS</h1>
                <div class="flex space-x-10 text-[10px] font-bold uppercase tracking-[0.3em]">
                    <button @click="category = 'All'" :class="category === 'All' ? 'text-blue-400' : 'text-slate-500'">All</button>
                    <button @click="category = 'Electronics'" :class="category === 'Electronics' ? 'text-blue-400' : 'text-slate-500'">Electronics</button>
                    <button @click="category = 'Lifestyle'" :class="category === 'Lifestyle' ? 'text-blue-400' : 'text-slate-500'">Lifestyle</button>
                </div>
            </nav>

            <header class="hero-gradient min-h-screen flex flex-col justify-center items-center text-center px-6">
                <div data-aos="zoom-out" data-aos-duration="1500">
                    <h2 class="text-7xl md:text-9xl font-black mb-8 leading-none">VIRAL TECH.<br><span class="text-blue-600 italic">ZERO EFFORT.</span></h2>
                    <p class="text-slate-400 text-xl md:text-2xl max-w-3xl mx-auto font-light mb-12">Hand-picked by AI. Trending globally in 2025.</p>
                    <a href="#store" class="bg-blue-600 px-12 py-5 rounded-full font-black text-lg hover:scale-110 transition shadow-2xl shadow-blue-500/20">EXPLORE COLLECTION</a>
                </div>
            </header>

            <section id="store" class="max-w-7xl mx-auto px-6 py-32 grid grid-cols-1 md:grid-cols-3 gap-12">
        """
        for p in products:
            html += f"""
                <div class="glow-border bg-[#0f172a] rounded-[3rem] p-10 flex flex-col justify-between" 
                     x-show="category === 'All' || category === '{p['cat']}'" data-aos="fade-up">
                    <div>
                        <div class="flex justify-between items-center mb-10">
                            <span class="text-blue-400 text-[10px] font-black uppercase tracking-widest bg-blue-500/10 px-4 py-1.5 rounded-full">{p['cat']}</span>
                            <span class="text-yellow-500 text-xs font-bold">{'★' * p['stars']}</span>
                        </div>
                        <h3 class="text-3xl font-bold mb-4 tracking-tight">{p['name']}</h3>
                        <p class="text-slate-400 text-sm leading-relaxed mb-10 line-clamp-3">{p['desc']}</p>
                    </div>
                    <div class="flex justify-between items-center border-t border-slate-800 pt-8">
                        <span class="text-4xl font-black">${p['price']}</span>
                        <button @click="open = true; activeP = {{name:'{p['name']}', price:'{p['price']}', desc:'{p['desc']}', cat:'{p['cat']}'}}" 
                                class="bg-white text-black px-8 py-4 rounded-2xl font-black hover:bg-blue-600 hover:text-white transition-all">VIEW</button>
                    </div>
                </div>"""
        
        html += """
            </section>

            <div x-show="open" x-cloak class="fixed inset-0 z-[200] flex items-center justify-center p-6 bg-black/90 backdrop-blur-md">
                <div class="bg-[#0f172a] max-w-3xl w-full rounded-[4rem] p-16 border border-slate-700 relative shadow-2xl" @click.away="open = false">
                    <button @click="open = false" class="absolute top-10 right-10 text-slate-500 hover:text-white text-4xl">&times;</button>
                    <span class="text-blue-500 text-xs font-black uppercase tracking-widest" x-text="activeP.cat"></span>
                    <h2 class="text-6xl font-black mt-4 mb-8 leading-tight" x-text="activeP.name"></h2>
                    <p class="text-slate-400 text-xl leading-relaxed mb-12" x-text="activeP.desc"></p>
                    
                    <div class="bg-blue-600/10 p-6 rounded-3xl border border-blue-600/30 mb-12">
                        <p class="text-blue-400 font-bold">⚡ FLASH DEAL: Limited 2025 stock available for global shipping.</p>
                    </div>

                    <div class="flex justify-between items-center">
                        <span class="text-6xl font-black" x-text="'$' + activeP.price"></span>
                        <button class="bg-blue-600 text-white px-12 py-6 rounded-[2rem] font-black text-2xl hover:bg-blue-500 shadow-xl shadow-blue-500/20">SECURE CHECKOUT</button>
                    </div>
                </div>
            </div>

            <footer class="py-20 text-center text-slate-600 text-[10px] font-bold uppercase tracking-[0.5em]">
                &copy; 2025 ELITE TRENDS GLOBAL. ALL RIGHTS RESERVED.
            </footer>

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
            subprocess.run(["git", "commit", "-m", "Brand Restoration: Ultra-Pro Design v19"], capture_output=True)
            subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
            return True
        except Exception as e:
            print(f"Deployment Error: {e}")
            return False

    def run(self):
        print("👿 המפלצת בונה את האתר מחדש ברמת גימור של אפל...")
        self.generate_html()
        if self.deploy():
            requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage", 
                         json={"chat_id": self.chat_id, "text": "🔥 *EMPIRE RESTORED*: The professional design is back and better!"})
            print("🚀 הכל מוכן! האתר שלך חזר להיות מותג על.")

if __name__ == "__main__":
    EmpireMaster = EliteEmpireMaster("8360823180:AAFUG7AhmzCl_6h1G_20oRgcWL8YbQ67r84", "5257373536")
    EmpireMaster.run()
