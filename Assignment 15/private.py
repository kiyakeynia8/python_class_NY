class Password:
    def __init__(self):
        self.__password = "@kiyakeynia8"

    def check_password(self, u_pass):
        if self.__password == u_pass:
            return True
        else:
            return False

p = Password()
u_pass = input("enter password: ")
print(p.check_password(u_pass))
print(p.__password)
print(p.password)
