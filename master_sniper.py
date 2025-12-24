import requests, os, subprocess

class EmpireGlobalV9:
    def __init__(self, token, chat_id):
        self.token, self.chat_id = token, chat_id
        self.path = os.path.expanduser("~/hacker_dropship")
        # מילות זהב לקידום בחו"ל (SEO Gold)
        self.keywords = "viral gadgets 2025, best solar charger for hiking, smart home deals USA, trending tech accessories"

    def generate_site(self, products):
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="description" content="{self.keywords}">
            <title>Elite Trends 2025 | Global Shopping</title>
            <script src="https://cdn.tailwindcss.com"></script>
        </head>
        <body class="bg-[#0f172a] text-slate-200 font-sans">
            <nav class="bg-[#1e293b] p-6 flex justify-between items-center border-b border-slate-700">
                <h1 class="text-3xl font-black text-blue-400 italic">ELITE TRENDS</h1>
                <div class="space-x-8 text-sm font-bold uppercase tracking-tighter">
                    <a href="#electronics" class="hover:text-blue-300">Electronics</a>
                    <a href="#lifestyle" class="hover:text-blue-300">Lifestyle</a>
                </div>
            </nav>
            <header class="py-20 text-center bg-gradient-to-b from-[#1e293b] to-[#0f172a]">
                <h2 class="text-6xl font-black mb-4">Viral Products. <span class="text-blue-500">Zero Effort.</span></h2>
                <p class="text-slate-400 italic">Hand-picked by AI. Trending globally in 2025.</p>
            </header>
            <main class="max-w-7xl mx-auto px-6 py-12 grid grid-cols-1 md:grid-cols-3 gap-10">
        """
        for p in products:
            html += f"""
                <div class="bg-[#1e293b] rounded-3xl p-8 border border-slate-700 hover:border-blue-500 transition-all duration-300 shadow-2xl">
                    <span class="bg-blue-900/50 text-blue-400 text-[10px] font-black px-3 py-1 rounded-full uppercase">{p['category']}</span>
                    <h3 class="text-2xl font-bold mt-4">{p['name']}</h3>
                    <p class="text-slate-400 text-sm mt-2">{p['desc']}</p>
                    <div class="mt-8 flex justify-between items-center">
                        <span class="text-3xl font-black">${p['price']}</span>
                        <a href="#" class="bg-blue-600 hover:bg-blue-500 text-white px-6 py-3 rounded-xl font-bold transition">Buy Now</a>
                    </div>
                </div>"""
        html += "</main></body></html>"
        with open(f"{self.path}/index.html", "w") as f: f.write(html)

    def deploy(self):
        try:
            os.chdir(self.path)
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "AI Market Research Update"], check=True)
            subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
            return True
        except: return False

    def run(self):
        winners = [
            {"name": "MagSafe Solar Hub", "price": 49.99, "category": "Electronics", "desc": "Next-gen solar charging for iPhone 15/16."},
            {"name": "Automatic Pet Feeder", "price": 89.00, "category": "Lifestyle", "desc": "Smartphone controlled feeding with 4K camera."},
            {"name": "Ultra-Light Gym Projector", "price": 120.50, "category": "Tech", "desc": "Transform any wall into a home cinema."}
        ]
        self.generate_site(winners)
        if self.deploy():
            requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage", 
                         json={"chat_id": self.chat_id, "text": "👿 *GLOBAL EMPIRE LIVE*: Site updated with Market Research Keywords!"})

if __name__ == "__main__":
    EmpireGlobalV9("8360823180:AAFUG7AhmzCl_6h1G_20oRgcWL8YbQ67r84", "5257373536").run()
