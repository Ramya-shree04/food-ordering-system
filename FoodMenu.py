from AbstractItem import AbstractItem
from FoodItem import FoodItem

class FoodMenu(AbstractItem):
    def __init__(self, name):
        super().__init__(name)
        self.__FoodItems =[]

    @property
    def FoodItems(self):
        return self.__FoodItems
    
    @FoodItems.setter
    def FoodItems(self, items):
        for item in items:
            if not isinstance(item, FoodItem):
                print("Invalid food Item")
                return
        self.__FoodItems = items

    def displayitem(self,start):
        print(f"{start} name : {self.name}")