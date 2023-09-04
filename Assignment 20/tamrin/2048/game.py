from functools import partial
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
import logic

app = QApplication([])
loder = QUiLoader()
main_window = loder.load("assignment_20/2048/2048_mainwindow.ui")

game_board = logic.start_game()

widgets = [[main_window.btn_0_0,main_window.btn_0_1,main_window.btn_0_2,main_window.btn_0_3],
            [main_window.btn_1_0,main_window.btn_1_1,main_window.btn_1_2,main_window.btn_1_3],
            [main_window.btn_2_0,main_window.btn_2_1,main_window.btn_2_2,main_window.btn_2_3],
            [main_window.btn_3_0,main_window.btn_3_1,main_window.btn_3_2,main_window.btn_3_3]]
main_window.btn_up.setShortcut(app.tr("w"))
main_window.btn_down.setShortcut(app.tr("s"))
main_window.btn_right.setShortcut(app.tr("d"))
main_window.btn_left.setShortcut(app.tr("a"))

main_window.show()

def show_ui(game_board, widgets):
    colors = {2:"255, 255, 255", 4:"255, 255, 200", 8:"255, 190, 110", 16:"255, 150, 110", 32:"255, 100, 110", 64:"255, 50, 50", 128:"255, 255, 130", 256:"255, 255, 90", 512:"255, 255, 70", 1024:"255, 255, 40", 2048:"255, 255, 0", 4096:"0, 85, 255"}
    for i in range(4):
        for j in range(4):
            if game_board[i][j] == 0:
                widgets[i][j].setStyleSheet("")
                widgets[i][j].setText("")
            else:
                widgets[i][j].setStyleSheet("")
                widgets[i][j].setText(str(game_board[i][j]))
                widgets[i][j].setStyleSheet(f"background-color: rgb({colors[game_board[i][j]]});")
            
show_ui(game_board, widgets)

def up(widgets):
    global game_board
    game_board, flag = logic.move_up(game_board)
    status = logic.get_current_state(game_board)
    if status == "Game Not Over":
        logic.add_new_2(game_board)

    show_ui(game_board, widgets)

def down(widgets):
    global game_board
    game_board, flag = logic.move_down(game_board)
    status = logic.get_current_state(game_board)
    if status == "Game Not Over":
        logic.add_new_2(game_board)

    show_ui(game_board, widgets)

def left(widgets):
    global game_board
    game_board, flag = logic.move_left(game_board)
    status = logic.get_current_state(game_board)
    if status == "Game Not Over":
        logic.add_new_2(game_board)

    show_ui(game_board, widgets)

def right(widgets):
    global game_board
    game_board, flag = logic.move_right(game_board)
    status = logic.get_current_state(game_board)
    if status == "Game Not Over":
        logic.add_new_2(game_board)

    show_ui(game_board, widgets)

main_window.btn_up.clicked.connect(partial(up,widgets))
main_window.btn_down.clicked.connect(partial(down,widgets))
main_window.btn_left.clicked.connect(partial(left,widgets))
main_window.btn_right.clicked.connect(partial(right,widgets))

app.exec_()