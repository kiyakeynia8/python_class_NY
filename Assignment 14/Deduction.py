def show(a,b):
    print("  "+str(a)+ "\n-----\n  "+ str(b))

class Deduction:
    def __init__(self, dict1 , dict2):
        self.dict1, self.dict2 = dict1, dict2
    
    def mul(self):
        r_sorat, r_makhraj = self.dict1["sorat"] * self.dict2["sorat"], self.dict1["makhraj"] * self.dict2["makhraj"]

        return r_sorat , r_makhraj

    def sub(self):
        r_sorat, r_makhraj = (self.dict1["sorat"] * self.dict2["makhraj"]) - (self.dict2["sorat"] * self.dict1["makhraj"]), self.dict1["makhraj"] * self.dict2["makhraj"]
        
        return r_sorat , r_makhraj
    
    def sum(self):
        r_sorat, r_makhraj = (self.dict1["sorat"] * self.dict2["makhraj"]) + (self.dict2["sorat"] * self.dict1["makhraj"]), self.dict1["makhraj"] * self.dict2["makhraj"]
    
        return r_sorat , r_makhraj
    
    def div(self):
        r_sorat, r_makhraj = self.dict1["sorat"] * self.dict2["majhraj"], self.dict1["makhraj"] * self.dict2["sorat"]

        return r_sorat , r_makhraj

op = int(input("1=sum, 2=sub, 3=mul, 4=div\n"))

for i in range (2):
    sorat = float(input("enter numerator: "))
    makhraj = float(input("enter denumerator: "))
   
    if i == 0:
        dct1  = {"sorat": sorat, "makhraj": makhraj}
    else:
        dct2 = {"sorat": sorat, "makhraj": makhraj}

deduction = Deduction(dct1, dct2)

if op == 1:
    s,m = deduction.sum()
    show(s,m)
elif op == 2:
    s,m = deduction.sub()
    show(s,m)
elif op == 3:
    s,m = deduction.mul()
    show(s,m)
elif op == 4:
    s,m = deduction.div()
    show(s,m)