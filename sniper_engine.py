import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
import random

class ProductSniper:
    def __init__(self):
        self.ua = UserAgent()
        self.winning_products = []

    def get_headers(self):
        return {
            "User-Agent": self.ua.random,
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.google.com/"
        }

    def calculate_viral_score(self, price, discount, reviews_per_day):
        # אלגוריתם חכם לדירוג פוטנציאל רווח
        # נוסחה: (אחוז הנחה * 0.5) + (קצב ביקורות * 0.3) + (בונוס מחיר נמוך * 0.2)
        score = (discount * 0.5) + (reviews_per_day * 0.3)
        if price < 20: score += 10 # מוצרים זולים נמכרים מהר יותר (Impulse Buy)
        return round(score, 2)

    def scan_market(self):
        print("🕵️ ה-Sniper התחיל בסריקה רב-שכבתית...")
        
        # סימולציה של נתוני שוק (במציאות נשאב מ-API של עליאקספרס/אמזון)
        market_data = [
            {"name": "RGB LED Strip 5M", "price": 4.5, "old_price": 19.9, "reviews_24h": 45},
            {"name": "Magnetic Phone Mount", "price": 2.1, "old_price": 12.0, "reviews_24h": 88},
            {"name": "Portable Blender", "price": 25.0, "old_price": 35.0, "reviews_24h": 12},
            {"name": "Self-Cleaning Water Bottle", "price": 45.0, "old_price": 55.0, "reviews_24h": 5}
        ]

        for item in market_data:
            discount = ((item['old_price'] - item['price']) / item['old_price']) * 100
            score = self.calculate_viral_score(item['price'], discount, item['reviews_24h'])
            
            if score > 40: # סף כניסה למוצר "מנצח"
                print(f"🔥 [WINNER FOUND] {item['name']}")
                print(f"   | Score: {score} | Profit Potential: HIGH")
                print(f"   | Price: {item['price']}$ (Discount: {round(discount)}%)")
                self.winning_products.append(item)

    def export_targets(self):
        print("\n📊 מייצא רשימת מטרות לפרסום...")
        with open("targets.json", "w") as f:
            import json
            json.dump(self.winning_products, f, indent=4)
        print("✅ הקובץ targets.json מוכן לשליחה לבוט הפרסום.")

if __name__ == "__main__":
    sniper = ProductSniper()
    sniper.scan_market()
    sniper.export_targets()
