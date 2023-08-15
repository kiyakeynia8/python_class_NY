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

def get_current_state(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return "WON"
    
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return "Game Not Ever"

    for i in range(3):
        for j in range(3):
            if (mat[i][j] == mat[i+1][j]) or (mat[i][j] == mat[i][j+1]):
                return "Game Not Ever"

    for i in range(3):
        if mat[3][i] == mat[3][i+1]:
            return "Game Not Ever"

    for i in range(3):
        if mat[i][3] == mat[i+1][3]:
            return "Game Not Ever"

    return "lose"