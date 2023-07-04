username_1 = "kiyakeynia8"
password_1 = "kia1388keynia"

username_2 = "kia13kia"
password_2 = "@kiyakeynia8"

# if user_input_n == username_1 and user_input_p == password_1 or user_input_n == username_2 and user_input_p == password_2:
for i in range(3):
    user_input_n = input("enter username: ")
    user_input_p = input("enter password: ")

    if user_input_n == username_1 and user_input_p == password_1:
        print("welcome kiyakeynia8")
        break

    elif user_input_n == username_2 and user_input_p == password_2:
        print("welcome kia13kia")
        break

    else:
        print("The password is wrong !!!")