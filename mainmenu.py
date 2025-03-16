from FoodManager import FoodManager
from cart import Cart

class mainmenu:

    __options = {1:"ShowRestaurant", 2:"ShowFoosItems", 3:"SearchRestaurant", 4:"SearchFoodItem", 5:"LogOut"}

    def __init__(self):
        self.__FoodManager = FoodManager()

    def ShowRestaurant(self):
        for i,res in enumerate(self.__FoodManager.Restaurants,1):
            res.displayitem(i)
        choice= int(input("please choose or select a restaurent"))
        res=self.__FoodManager.Restaurants[choice]
        self.ShowFoodMenus(res.FoodMenus)


    def ShowFoodItems(self, fooditems=None):
        if fooditems is not None:
            for i,fooditem in enumerate(self.__FoodManager.foodItems,1):
                fooditem.displayitem(i)
            choice = list(map(int, input("please choose your food items: ").split(",")))
            cart = Cart(fooditems, choice)
            cart.processorder(fooditems)
        else:
            pass


    def SearchRestaurant(self):
        resname = input("Enter the restaurant name: ")
        res = self.__FoodManager.FindRestaurant(resname)
        if res is not None:
            print("Restaurant found")
            print(f"Name: {res.name}, Rating: {res.rating}")
            self.ShowFoodMenus(res.FoodMenus)
        else:
            print(f"No Restaurant found on the name {res.name}")


    def SearchFoodItem(self):
        pass

    def ShowFoodMenus(self, menus):
        print("\n\nList of menus available")
        for i,menu in enumerate(self.__FoodManager.foodmenu,1):
            menu.displayitem(i)
        choice = int(input("Please Choose Menu: "))
        fooditems=menus[choice-1].FoodItems
        self.ShowFoodItems(fooditems)

    def start(self):
        while True:
            for option in  mainmenu.__options:
                print(f"{option}.{mainmenu.__options[option]}", end = "   ")
            print()

            try:
                choice = int(input("Please Enter Your Choice: "))
                value = mainmenu.__options[choice]
                getattr(self,value)()
            except (ValueError,KeyError):
                print("Invalid choice. Please choose a valid option.")