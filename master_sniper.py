import requests, os, subprocess, time, random

class EmpireMaster:
    def __init__(self, token, chat_id):
        self.token, self.chat_id = token, chat_id
        self.path = os.path.expanduser("~/hacker_dropship")
        # דאטה מהחיפושים האמיתיים שלך ב-AliExpress
        self.raw_data = [
            {"name": "MagSafe Solar Hub", "ali_price": 101.01, "category": "Electronics"},
            {"name": "Smart AI Pet Feeder", "ali_price": 60.64, "category": "Lifestyle"},
            {"name": "Ultra-HD Gym Projector", "ali_price": 215.43, "category": "Tech"}
        ]

    def generate_sales_copy(self, name):
        """מנוע לכתיבת מלל שיווקי אוטונומי"""
        copies = {
            "MagSafe Solar Hub": "Engineered for the modern explorer. This 50,000mAh monster uses military-grade solar cells to keep your devices alive in the wildest conditions. Features magnetic MagSafe alignment for seamless charging.",
            "Smart AI Pet Feeder": "Never worry about your pet again. Our AI-driven feeder ensures precise nutrition with smartphone scheduling, a 4K wide-angle camera, and two-way audio to talk to your best friend from anywhere.",
            "Ultra-HD Gym Projector": "Transform any space into a high-end cinema. Native 4K resolution, Wi-Fi 6 connectivity, and 360-degree immersive sound. Perfect for movies, gaming, and professional presentations."
        }
        return copies.get(name, "Premium high-quality product designed for 2025.")

    def build_site(self):
        print("🏗️ בונה את האתר ואת דפי המוצר המלאים...")
        products = []
        for item in self.raw_data:
            # חישוב מחיר מכירה (עלות + רווח של ~150%)
            sale_price = round((item['ali_price'] / 3.7) * 2.5, 2) 
            products.append({
                "name": item['name'],
                "price": sale_price,
                "category": item['category'],
                "desc": self.generate_sales_copy(item['name'])
            })

        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8"><title>Elite Trends | Official</title>
            <script src="https://cdn.tailwindcss.com"></script>
            <script src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js" defer></script>
        </head>
        <body class="bg-[#020617] text-white font-sans" x-data="{{ open: false, p: {{}} }}">
            <nav class="p-6 border-b border-slate-800 flex justify-between bg-[#0f172a] fixed w-full z-50">
                <h1 class="text-2xl font-black text-blue-500 italic">ELITE TRENDS</h1>
                <div class="text-xs font-bold text-slate-500 uppercase">2025 Collection</div>
            </nav>

            <main class="max-w-7xl mx-auto px-6 pt-40 pb-20 grid grid-cols-1 md:grid-cols-3 gap-10">
        """
        for p in products:
            html += f"""
                <div class="bg-[#0f172a] rounded-[2.5rem] p-8 border border-slate-800 shadow-2xl">
                    <span class="text-blue-400 text-[10px] font-black uppercase tracking-widest">{p['category']}</span>
                    <h3 class="text-2xl font-bold mt-4">{p['name']}</h3>
                    <div class="mt-8 flex justify-between items-center">
                        <span class="text-3xl font-black">${p['price']}</span>
                        <button @click="open = true; p = {{name:'{p['name']}', price:'{p['price']}', desc:'{p['desc']}', cat:'{p['category']}'}}" 
                                class="bg-blue-600 px-6 py-3 rounded-xl font-bold hover:bg-blue-500 transition">VIEW PRODUCT</button>
                    </div>
                </div>"""
        
        html += """
            </main>

            <div x-show="open" class="fixed inset-0 z-[100] flex items-center justify-center p-6 bg-black/90 backdrop-blur-md" x-cloak>
                <div class="bg-[#0f172a] max-w-2xl w-full rounded-[3rem] p-12 border border-slate-700 relative shadow-2xl" @click.away="open = false">
                    <button @click="open = false" class="absolute top-8 right-8 text-slate-500 text-3xl">&times;</button>
                    <span class="text-blue-400 text-xs font-black uppercase" x-text="p.cat"></span>
                    <h2 class="text-5xl font-black mt-4 mb-6" x-text="p.name"></h2>
                    <div class="h-1 w-20 bg-blue-600 mb-8"></div>
                    <p class="text-slate-400 text-lg leading-relaxed mb-10" x-text="p.desc"></p>
                    <div class="flex justify-between items-center border-t border-slate-800 pt-8">
                        <span class="text-5xl font-black" x-text="'$' + p.price"></span>
                        <button class="bg-white text-black px-12 py-5 rounded-2xl font-black text-xl hover:bg-blue-400 hover:text-white transition-all">ADD TO CART</button>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
        with open(f"{self.path}/index.html", "w", encoding="utf-8") as f: f.write(html)

    def deploy(self):
        try:
            os.chdir(self.path)
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "Full Autonomous Content Update"], capture_output=True)
            subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
            return True
        except: return False

    def run(self):
        print("👿 המוח המרכזי התחיל לעבוד...")
        self.build_site()
        if self.deploy():
            requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage", 
                         json={"chat_id": self.chat_id, "text": "✅ *EMPIRE UPDATED*: Products, pages, and descriptions are LIVE!"})
            print("🚀 הכל מוכן! האתר שלך מעודכן עם כל המלל והמוצרים.")

if __name__ == "__main__":
    EmpireMaster("8360823180:AAFUG7AhmzCl_6h1G_20oRgcWL8YbQ67r84", "5257373536").run()
