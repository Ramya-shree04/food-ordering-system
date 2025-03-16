from FoodItem import FoodItem
from FoodMenu import FoodMenu
from Restaurant import Restaurant

class FoodManager:
    def __init__(self):
        self.Restaurants = self.PrepareRestaurants()
        self.foodItems = self.PrepareFoodItems()
        self.foodmenu= self.PrepareFoodMenus()
    
    def PrepareFoodItems(self):
        item1= FoodItem(name=" Birayani", rating=4, price=250, description="*******")
        item2= FoodItem(name=" channa", rating=4.3, price=270, description="*******")
        item3= FoodItem(name=" noodles", rating=4.4, price=150, description="*******")
        item4= FoodItem(name=" naan", rating=4.6, price=50, description="*******")
        item5= FoodItem(name=" mutton rohenjosh", rating=4.3, price=350, description="*******")
        return[item1, item2, item3, item4, item5]

    def PrepareFoodMenus(self):
        FoodItems = self.PrepareFoodItems()
        menu1 = FoodMenu("veg")
        menu1.FoodItems = [FoodItems[1], FoodItems[2], FoodItems[3]]
        menu2 = FoodMenu("non_veg")
        menu2.FoodItems = [FoodItems[0], FoodItems[2], FoodItems[4]]
        menu3 = FoodMenu("egg")
        menu3.FoodItems = [FoodItems[0], FoodItems[2], FoodItems[3]]
        return [menu1, menu2, menu3]

    def PrepareRestaurants(self):
        FoodMenus = self.PrepareFoodMenus()
        res1 = Restaurant(name="a2b", rating=3, location="chennai", offer=10)
        res1.FoodMenus = [FoodMenus[0]]
        res2 = Restaurant(name="ramya", rating=4.9, location="kerala", offer=20)
        res2.FoodMenus = [FoodMenus[1]]
        res3 = Restaurant(name="ravi", rating=4.8, location="goa", offer=25)
        res3.FoodMenus = [FoodMenus[2]]
        return [res1, res2, res3]
    def FindRestaurant(self, name):
        for res in self.Restaurants:
            if res.name == name:
                return res
            