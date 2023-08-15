import random 

def start_game():
    mat = []

    for i in range(4):
        mat.append([0] * 4)
    
    print("Commands:\nw: up\ns: down\na: left\nd: right")

    mat = add_new_2(mat)
    return mat

def add_new_2(mat):
    while True:
        row = random.randint(0, 3)
        column = random.randint(0, 3)

        if mat[row][column] == 0:
            mat[row][column] = 2
            break

    return mat

def get_current_state():
    pass