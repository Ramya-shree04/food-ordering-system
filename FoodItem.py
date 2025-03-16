from AbstractItem import AbstractItem

class FoodItem(AbstractItem):
    def __init__(self, name, rating, price, description):
        super().__init__(name=name, rating=rating)
        self.price = price 
        self.description = description

    def displayitem(self,start):
        print(f"{start} name : {self.name} price  : {self.price} rating : {self.rating}")