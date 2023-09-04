import sys
from functools import partial
from database import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = Database()
        self.read_from_database()

        self.ui.btn_new_task.clicked.connect(self.new_tasks)

    def new_tasks(self):
        new_title = self.ui.tb_ne_task.text()
        new_description = self.ui.tb_n_t_d.toPlainText()
        new_date = self.ui.date.text()
        new_time = self.ui.time.text()
        i_o_n = self.ui.i_o_n.text()
        feedback = self.db.add_new_task(new_title, new_description, new_date, new_time, i_o_n) 

        if feedback == True:
            self.read_from_database()
            self.ui.tb_ne_task.setText("")
            self.ui.tb_n_t_d.setText("")
            self.ui.date.setText("")
            self.ui.time.setText("")
            self.ui.i_o_n.setText("")

        else:
            msg_box = QMessageBox()
            msg_box.setText("مشکلی پیش امده!!")
            msg_box.exec_()

    def remove_task(self,id):
        feedback = self.db.remove_task(id)

        if feedback == True:
            self.read_from_database()

        else:
            msg_box = QMessageBox()
            msg_box.setText("مشکلی پیش امده!!")
            msg_box.exec_()
    
    def task_done(self,id):
        feedback = self.db.task_done(id)

        if feedback == True:
            self.read_from_database()

        else:
            msg_box = QMessageBox()
            msg_box.setText("مشکلی پیش امده!!")
            msg_box.exec_()

    def read_from_database(self):
        tasks = self.db.get_tasks()

        for i in range(len(tasks)):
            new_checkbox = QCheckBox()
            new_label_n = QLabel()
            new_label_d = QLabel()
            new_label_date = QLabel()
            new_label_time = QLabel()
            new_btn_del = QPushButton("❌")
            new_btn_del.setStyleSheet('background-color: rgb(255, 0, 0);')
            
            new_label_n.setText(tasks[i][1])
            new_label_d.setText(tasks[i][2]) 
            new_label_date.setText(tasks[i][3])
            new_label_time.setText(tasks[i][4])

            if tasks[i][5] == 1: 
                new_checkbox.setChecked(True)

            if str(tasks[i][6]) == "important" or str(tasks[i][6]) == "Important":
                new_label_n.setStyleSheet('color: rgb(255, 0, 0);')
            
            self.ui.gl_tasks.addWidget(new_checkbox, i, 0)
            self.ui.gl_tasks.addWidget(new_label_n, i, 1)
            self.ui.gl_tasks.addWidget(new_label_d, i, 2)
            self.ui.gl_tasks.addWidget(new_label_date, i, 3)
            self.ui.gl_tasks.addWidget(new_label_time, i, 4)
            self.ui.gl_tasks.addWidget(new_btn_del, i, 5)

            new_checkbox.clicked.connect(partial(self.task_done, tasks[i][0]))
            new_btn_del.clicked.connect(partial(self.remove_task, tasks[i][0]))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec_()