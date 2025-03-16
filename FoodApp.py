import re
from User import User
from UserManager import UserManager
from FoodManager import FoodManager
from mainmenu import mainmenu

class LoginSystem:

    def Login(self):
        mailid = input("Email: ")
        password = input("Password: ")
        user = UserManager.finduser(mailid = mailid, pwd = password)
        if user is not None:
            menu = mainmenu()
            menu.start()

        else:
            print("Invalid email or password")


    def Register(self):
        # name
        while True:
            name = input("Name: ")
            if name.replace(" ", "").isalpha():                                     # Allow only alphabets and spaces
                break
            print("Invalid name. Only alphabets and spaces are allowed.")
        # mobile number
        while True:
            mobile = input("Mobile number: ")
            if mobile.isdigit() and len(mobile) == 10:
                break
            print("Invalid mobile number. Enter a 10-digit number.") 
        # mail id
        while True:
            mailid = input("Email: ")
            if re.match(r"[^@]+@[^@]+\.[^@]+", mailid):
                break
            print("Invalid email format.")
        # password    
        while True:
            password = input("Password: ")
            if len(password) == 8:
                break
            else:
                print("Password must be 8 characters long.")


        user = User(name=name, phn=mobile, mailid=mailid, pwd=password)
        UserManager.adduser(user)
        print("You have registered successfully")


    def GuestLogin(self):
        pass


    def Exit(self):
        print("Thankyou for usinf the App")
        exit()


    def ValidateOption(self,option):
        getattr(self,option)()      




class FoodApp:

    LoginOptions = {1:"Login", 2:"Register", 3: "GuestLogin", 4: "Exit"}

    @staticmethod
    def Init():                                                                              #initial method
        print("Welcome to SUNWON Food Ordering App")

        menu = mainmenu()
        menu.start()

        '''loginsystem = LoginSystem()                                                          # creating obj for the loginsyatem class in the food app class
        while True:
            for option in FoodApp.LoginOptions:
                print(f"{option}.{FoodApp.LoginOptions[option]}", end = "   ")
            print()
            try:
                choice = int(input("Please Enter Your Choice: "))
                loginsystem.ValidateOption(FoodApp.LoginOptions[choice])
            except (ValueError,KeyError):
                print("Invalid choice. Please choose a valid option.")'''