class Cart:
    def __init__(self, items,choices):
        self.choices = choices
        self.fooditems = self.__addtocart(items)
        
    def __addtocart(self, items):
        fooddic = {}
        for choice in self.choices:
            if choice > len(items):
                raise KeyError
            if choice in fooddic:
                fooddic[choice]+=1
            else:
                fooddic[choice]=1
        return fooddic
    

    def processorder(self, fooditems):
        Total = 0
        for item in self.fooditems:
            price = self.fooditems[item] * fooditems[item-1].price
            Total += price
            print(f"{fooditems[item-1].name} x {self.fooditems[item]} = {price}")
        print(f"Total : {Total}")
        self.processpayment(Total)
        


    def processpayment(self,Total):
        print("\nPayment Options:")
        print("1. UPI Payment")
        print("2. Cash on Delivery")
        payment_choice = int(input("Choose payment method (1/2): "))

        if payment_choice == 1:
            print("\nUPI Payment Options:")
            print("1. GPay")
            print("2. PhonePe")
            print("3. Paytm")
            upi_choice = int(input("Select a UPI option (1/2/3): "))
            upi_methods = {1: "GPay", 2: "PhonePe", 3: "Paytm"}
            if upi_choice in upi_methods:
                print(f"Processing payment via {upi_methods[upi_choice]}...")
                print("Payment Completed! Order Confirmed.")
            else:
                print("Invalid UPI choice. Payment failed.")
        elif payment_choice == 2:
            print(f"Order placed successfully! Please pay {Total} upon delivery.")
        else:
            print("Invalid payment option. Please try again.")

