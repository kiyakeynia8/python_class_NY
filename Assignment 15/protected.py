class Password:
    def __init__(self):
        self._password = "@kiyakeynia8"

    def check_password(self, u_pass):
        if self._password == u_pass:
            return True
        else:
            return False

class Pass2(Password):
    def __init__(self, n):
        super().__init__(n)

    def show_pass(self):
        print(self._password)

p = Pass2()
u_pass = input("enter password: ")
print(p.check_password(u_pass))
print(p._password)
print(p.__password)