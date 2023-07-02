r = float(input("r: "))
h = float(input("h: "))

masahat_janeby = 2*3.141592653589793*r*h
masahat_kol = masahat_janeby + (2*3.141592653589793*r**2)
hajm = 3.141592653589793*r**2*h

print(f"masahat_janeby -> {masahat_janeby}")
print(f"masahat_kol -> {masahat_kol}")
print(f"hajm -> {hajm}")