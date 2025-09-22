# iron_scrap_manager.py

from datetime import datetime

class IronScrap:
    def __init__(self, category, weight_kg, location):
        self.category = category
        self.weight_kg = weight_kg
        self.location = location
        self.date_added = datetime.now()

    def __str__(self):
        return f"{self.category} | {self.weight_kg}kg | {self.location} | {self.date_added.strftime('%Y-%m-%d %H:%M')}"

class ScrapInventory:
    def __init__(self):
        self.scraps = []

    def add_scrap(self, category, weight_kg, location):
        scrap = IronScrap(category, weight_kg, location)
        self.scraps.append(scrap)
        print("✅ ضایعه ثبت شد:", scrap)

    def list_scraps(self):
        print("\n📦 لیست ضایعات:")
        for scrap in self.scraps:
            print("-", scrap)

# نمونه استفاده
inventory = ScrapInventory()
inventory.add_scrap("آهن زنگ‌زده", 150, "تهران")
inventory.add_scrap("ورق بریده", 80, "اصفهان")
inventory.list_scraps()