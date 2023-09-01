import random 

def start_game():
    mat = []

    for i in range(4):
        mat.append([0] * 4)
    
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
                return "Game Not Over"

    for i in range(3):
        for j in range(3):
            if (mat[i][j] == mat[i+1][j]) or (mat[i][j] == mat[i][j+1]):
                return "Game Not Over"

    for i in range(3):
        if mat[3][i] == mat[3][i+1]:
            return "Game Not Over"

    for i in range(3):
        if mat[i][3] == mat[i+1][3]:
            return "Game Not Over"

    return "Lose"

def compress(mat):
    flag = False
    new_mat = []

    for i in range(4):
        new_mat.append([0]*4)

    for i in range(4):
        p = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][p] = mat[i][j]
                if j != p:
                    flag = True

                p+=1

    return new_mat, flag

def merge(mat):
    flag = False

    for i in range(4): # i = 3
        for j in range(3): # j = 1
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0 and mat[i][j+1] != 0:
                mat[i][j] = mat[i][j] + mat[i][j+1]
                mat[i][j+1] = 0
                flag = True

    return mat, flag 

def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3-j])

    return new_mat

def reverse_2(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[3-i][j])

    return new_mat

def transpose(mat):
    new_mat = []

    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])

    return new_mat

def move_left(mat):
    new_grid, flag_1 = compress(mat)
    new_grid, flag_2 = merge(new_grid)
    flag = flag_1 or flag_2
    new_grid, _ = compress(new_grid)
    return new_grid, flag

def move_right(mat):
    new_grid = reverse(mat)
    new_grid, flag = move_left(new_grid)
    new_grid = reverse(new_grid)

    return new_grid, flag

def move_up(mat):
    new_grid = transpose(mat)
    new_grid, flag = move_left(new_grid)
    new_grid = transpose(new_grid)

    return new_grid, flag

def move_down(mat):
    new_grid = reverse_2(mat)
    new_grid, flag = move_up(new_grid)
    new_grid = reverse_2(new_grid)

    return new_grid, flag