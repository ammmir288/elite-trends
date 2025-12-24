import requests, os, subprocess, time

class EmpireArchitect:
    def __init__(self, token, chat_id):
        self.token, self.chat_id = token, chat_id
        self.root_path = os.path.expanduser("~/hacker_dropship")
        self.prod_path = os.path.join(self.root_path, "products")
        if not os.path.exists(self.prod_path): os.makedirs(self.prod_path)
        
        # דאטה מהמחקר שלך (כאן נכנסים מוצרים חדשים אוטומטית)
        self.catalog = [
            {"id": "solar-hub", "name": "MagSafe Solar Hub", "cost": 101.01, "cat": "Electronics", "img": "https://ae01.alicdn.com/kf/S8f21e06d649e4860b76e105828469d44Y.jpg", "desc": "The ultimate 50,000mAh solar charging solution. Military-grade build with MagSafe support."},
            {"id": "pet-feeder", "name": "Smart AI Pet Feeder", "cost": 60.64, "cat": "Lifestyle", "img": "https://ae01.alicdn.com/kf/Sf66649f847284b159f8a3779e5192137D.jpg", "desc": "Automated dietary control with integrated 4K camera. Keep your pets healthy and safe."},
            {"id": "gym-projector", "name": "Ultra-HD Gym Projector", "cost": 215.43, "cat": "Tech", "img": "https://ae01.alicdn.com/kf/S706cad101.jpg", "desc": "Native 4K cinematic experience for home and gym. Pocket-sized with Wi-Fi 6 technology."}
        ]

    def build_product_page(self, p):
        """יוצר דף HTML נפרד ומקצועי לכל מוצר"""
        price = round((p['cost'] / 3.7) * 2.5, 2)
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8"><title>{p['name']} | Elite Trends</title>
            <script src="https://cdn.tailwindcss.com"></script>
        </head>
        <body class="bg-[#020617] text-white font-sans">
            <nav class="p-8 border-b border-slate-800 bg-[#0f172a]"><a href="../index.html" class="text-blue-500 font-bold">← Back to Store</a></nav>
            <main class="max-w-6xl mx-auto py-20 px-6 flex flex-col md:flex-row gap-16">
                <div class="md:w-1/2 rounded-[3rem] overflow-hidden border border-slate-800 shadow-2xl">
                    <img src="{p['img']}" class="w-full h-full object-cover">
                </div>
                <div class="md:w-1/2">
                    <span class="text-blue-400 font-black uppercase tracking-widest">{p['cat']}</span>
                    <h1 class="text-6xl font-black mt-4 mb-8">{p['name']}</h1>
                    <p class="text-slate-400 text-xl leading-relaxed mb-10">{p['desc']}</p>
                    <div class="text-5xl font-black mb-10">${price}</div>
                    <button class="bg-blue-600 px-12 py-5 rounded-2xl font-black text-2xl hover:bg-blue-500 shadow-xl shadow-blue-500/20">ORDER NOW</button>
                    <p class="mt-8 text-slate-500 text-sm italic">✓ Global shipping included | ✓ 2025 Model Certified</p>
                </div>
            </main>
        </body></html>"""
        with open(f"{self.prod_path}/{p['id']}.html", "w", encoding="utf-8") as f: f.write(html)

    def build_main_index(self):
        """בונה את דף הבית הראשי שמקשר לדפים החדשים"""
        html_start = """
        <!DOCTYPE html>
        <html lang="en">
        <head><meta charset="UTF-8"><title>Elite Trends Official</title><script src="https://cdn.tailwindcss.com"></script></head>
        <body class="bg-[#020617] text-white">
            <nav class="p-8 border-b border-slate-800 text-center"><h1 class="text-3xl font-black text-blue-500">ELITE TRENDS</h1></nav>
            <main class="max-w-7xl mx-auto px-6 py-20 grid grid-cols-1 md:grid-cols-3 gap-10">"""
        
        cards = ""
        for p in self.catalog:
            price = round((p['cost'] / 3.7) * 2.5, 2)
            cards += f"""
                <div class="bg-[#0f172a] rounded-[2.5rem] overflow-hidden border border-slate-800 shadow-2xl hover:scale-105 transition">
                    <img src="{p['img']}" class="h-56 w-full object-cover">
                    <div class="p-8">
                        <h3 class="text-2xl font-bold">{p['name']}</h3>
                        <div class="mt-8 flex justify-between items-center">
                            <span class="text-3xl font-black">${price}</span>
                            <a href="products/{p['id']}.html" class="bg-blue-600 px-6 py-3 rounded-xl font-bold">VIEW PRODUCT</a>
                        </div>
                    </div>
                </div>"""
        
        with open(f"{self.root_path}/index.html", "w") as f: f.write(html_start + cards + "</main></body></html>")

    def run(self):
        print("👿 ה-Empire Architect התחיל בבניית האימפריה...")
        for p in self.catalog:
            self.build_product_page(p)
            print(f"✅ נוצר דף נפרד ל: {p['name']}")
        self.build_main_index()
        
        # אוטומציה של ה-Git
        os.chdir(self.root_path)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Full Site Architecture Deployment"], capture_output=True)
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        print("🚀 האתר המלא באוויר ב-GitHub!")

if __name__ == "__main__":
    EmpireArchitect("8360823180:AAFUG7AhmzCl_6h1G_20oRgcWL8YbQ67r84", "5257373536").run()
