
from User import User

class UserManager:
    __USer = []

    @classmethod
    def adduser(cls, user):

        if isinstance(user,User):                      # isinstance is used ro find the type of a variable <syntax> : isinstance(variable, variabletype)
            cls.__USer.append(user)
        else:
            print("Invalid user")

    @classmethod
    def finduser(cls, mailid, pwd):
        for user in cls.__USer:
            if user.mailid == mailid and user.password == pwd:
                return user