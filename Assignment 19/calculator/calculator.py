import math
from functools import partial
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader

s = 0

def s_s():
    main_window.btn_0.setStyleSheet(''' QPushButton {font: 20pt "MV Boli";background-color: rgb(84, 84, 84);border-radius: 20px;padding: 4px;}QPushButton:hover:!pressed {background-color:rgb(58, 58, 58);}''')
    main_window.btn_1.setStyleSheet(''' QPushButton {font: 20pt "MV Boli";background-color: rgb(84, 84, 84);border-radius: 20px;padding: 4px;}QPushButton:hover:!pressed {background-color:rgb(58, 58, 58);}''')
    main_window.btn_2.setStyleSheet(''' QPushButton {font: 20pt "MV Boli";background-color: rgb(84, 84, 84);border-radius: 20px;padding: 4px;}QPushButton:hover:!pressed {background-color:rgb(58, 58, 58);}''')
    main_window.btn_3.setStyleSheet(''' QPushButton {font: 20pt "MV Boli";background-color: rgb(84, 84, 84);border-radius: 20px;padding: 4px;}QPushButton:hover:!pressed {background-color:rgb(58, 58, 58);}''')
    main_window.btn_4.setStyleSheet(''' QPushButton {font: 20pt "MV Boli";background-color: rgb(84, 84, 84);border-radius: 20px;padding: 4px;}QPushButton:hover:!pressed {background-color:rgb(58, 58, 58);}''')
    main_window.btn_5.setStyleSheet(''' QPushButton {font: 20pt "MV Boli";background-color: rgb(84, 84, 84);border-radius: 20px;padding: 4px;}QPushButton:hover:!pressed {background-color:rgb(58, 58, 58);}''')
    main_window.btn_6.setStyleSheet(''' QPushButton {font: 20pt "MV Boli";background-color: rgb(84, 84, 84);border-radius: 20px;padding: 4px;}QPushButton:hover:!pressed {background-color:rgb(58, 58, 58);}''')
    main_window.btn_7.setStyleSheet(''' QPushButton {font: 20pt "MV Boli";background-color: rgb(84, 84, 84);border-radius: 20px;padding: 4px;}QPushButton:hover:!pressed {background-color:rgb(58, 58, 58);}''')
    main_window.btn_8.setStyleSheet(''' QPushButton {font: 20pt "MV Boli";background-color: rgb(84, 84, 84);border-radius: 20px;padding: 4px;}QPushButton:hover:!pressed {background-color:rgb(58, 58, 58);}''')
    main_window.btn_9.setStyleSheet(''' QPushButton {font: 20pt "MV Boli";background-color: rgb(84, 84, 84);border-radius: 20px;padding: 4px;}QPushButton:hover:!pressed {background-color:rgb(58, 58, 58);}''')

    main_window.btn_po.setStyleSheet(''' QPushButton {font: 20pt "MV Boli";background-color: rgb(0, 255, 127);border-radius: 20px;padding: 4px;}QPushButton:hover:!pressed {background-color:rgb(0, 255, 167);}''')
    main_window.btn_sqrt.setStyleSheet(''' QPushButton {font: 20pt "MV Boli";background-color: rgb(0, 255, 127);border-radius: 20px;padding: 4px;}QPushButton:hover:!pressed {background-color:rgb(0, 255, 167);}''')
    main_window.btn_fac.setStyleSheet(''' QPushButton {font: 20pt "MV Boli";background-color: rgb(0, 255, 127);border-radius: 20px;padding: 4px;}QPushButton:hover:!pressed {background-color:rgb(0, 255, 167);}''')
    main_window.btn_sin.setStyleSheet(''' QPushButton {font: 20pt "MV Boli";background-color: rgb(0, 255, 127);border-radius: 20px;padding: 4px;}QPushButton:hover:!pressed {background-color:rgb(0, 255, 167);}''')
    main_window.btn_cos.setStyleSheet(''' QPushButton {font: 20pt "MV Boli";background-color: rgb(0, 255, 127);border-radius: 20px;padding: 4px;}QPushButton:hover:!pressed {background-color:rgb(0, 255, 167);}''')
    main_window.btn_tan.setStyleSheet(''' QPushButton {font: 20pt "MV Boli";background-color: rgb(0, 255, 127);border-radius: 20px;padding: 4px;}QPushButton:hover:!pressed {background-color:rgb(0, 255, 167);}''')
    main_window.btn_cot.setStyleSheet(''' QPushButton {font: 20pt "MV Boli";background-color: rgb(0, 255, 127);border-radius: 20px;padding: 4px;}QPushButton:hover:!pressed {background-color:rgb(0, 255, 167);}''')
    main_window.btn_abs.setStyleSheet(''' QPushButton {font: 20pt "MV Boli";background-color: rgb(0, 255, 127);border-radius: 20px;padding: 4px;}QPushButton:hover:!pressed {background-color:rgb(0, 255, 167);}''')
    main_window.btn_rou.setStyleSheet(''' QPushButton {font: 20pt "MV Boli";background-color: rgb(0, 255, 127);border-radius: 20px;padding: 4px;}QPushButton:hover:!pressed {background-color:rgb(0, 255, 167);}''')

    main_window.btn_c.setStyleSheet(''' QPushButton {font: 20pt "MV Boli";background-color: rgb(0, 255, 255);border-radius: 20px;padding: 4px;}QPushButton:hover:!pressed {background-color:rgb(200, 255, 255);}''')
    main_window.btn_sum.setStyleSheet(''' QPushButton {font: 20pt "MV Boli";background-color: rgb(0, 255, 255);border-radius: 20px;padding: 4px;}QPushButton:hover:!pressed {background-color:rgb(200, 255, 255);}''')
    main_window.btn_sub.setStyleSheet(''' QPushButton {font: 20pt "MV Boli";background-color: rgb(0, 255, 255);border-radius: 20px;padding: 4px;}QPushButton:hover:!pressed {background-color:rgb(200, 255, 255);}''')
    main_window.btn_div.setStyleSheet(''' QPushButton {font: 20pt "MV Boli";background-color: rgb(0, 255, 255);border-radius: 20px;padding: 4px;}QPushButton:hover:!pressed {background-color:rgb(200, 255, 255);}''')
    main_window.btn_eql.setStyleSheet(''' QPushButton {font: 20pt "MV Boli";background-color: rgb(0, 255, 255);border-radius: 20px;padding: 4px;}QPushButton:hover:!pressed {background-color:rgb(200, 255, 255);}''')
    main_window.btn_mul.setStyleSheet(''' QPushButton {font: 20pt "MV Boli";background-color: rgb(0, 255, 255);border-radius: 20px;padding: 4px;}QPushButton:hover:!pressed {background-color:rgb(200, 255, 255);}''')
    main_window.btn_dot.setStyleSheet(''' QPushButton {font: 20pt "MV Boli";background-color: rgb(0, 255, 255);border-radius: 20px;padding: 4px;}QPushButton:hover:!pressed {background-color:rgb(200, 255, 255);}''')

def num(x):
    global s
    if s == 1:
        s = 0
        ac()

    text = main_window.text_line.text()
    new_text = text + x 
    main_window.text_line.setText(new_text)

def c():
    t = main_window.text_line.text()
    new_t = t[:-1]
    main_window.text_line.setText(new_t)

def ac():
    main_window.text_line.setText("")

def eql():
    global s
    text = main_window.text_line.text()
    if "^" in text:
        text = text.split("^")
        text = "**".join(text)
    elif "➗" in text:
        text = text.split("➗")
        text = "/".join(text)
    elif "×" in text:
        text = text.split("×")
        text = "*".join(text)
    try:
        new_t = eval(text)
        main_window.text_line.setText(str(new_t))
        s = 1
    except:
        main_window.text_line.setText("invalid Syntax")
        s = 1

def sqrt():
    global s
    if s == 1:
        s = 0
        ac()
    text = float(main_window.text_line.text())
    result = math.sqrt(text)
    main_window.text_line.setText(str(result))

def fac():
    global s
    if s == 1:
        s = 0
        ac()
    text = float(main_window.text_line.text())
    result = math.factorial(text)
    main_window.text_line.setText(str(result))
    
def sin():
    global s
    if s == 1:
        s = 0
        ac()
    text = float(main_window.text_line.text())
    n = math.radians(text)
    result = math.sin(n)
    main_window.text_line.setText(str(result))

def cos():
    global s
    if s == 1:
        s = 0
        ac()
    text = float(main_window.text_line.text())
    n = math.radians(text)
    result = math.cos(n)
    main_window.text_line.setText(str(result))
    
def tan():
    global s
    if s == 1:
        s = 0
        ac()
    text = float(main_window.text_line.text())
    n = math.radians(text)
    result = math.tan(n)
    main_window.text_line.setText(str(result))

def cot():
    global s
    if s == 1:
        s = 0
        ac()
    text = float(main_window.text_line.text())
    n = math.radians(text)
    result = math.atan(n)
    main_window.text_line.setText(str(result))

def abs_():
    global s
    if s == 1:
        s = 0
        ac()
    text = float(main_window.text_line.text())
    result = abs(text)
    main_window.text_line.setText(str(result))
    
def rou():
    global s
    if s == 1:
        s = 0
        ac()
    text = float(main_window.text_line.text())
    result = round(text)
    main_window.text_line.setText(str(result))

app = QApplication([])
loader = QUiLoader()

main_window = loader.load("calculator/calculator_ui.ui")
s_s()
main_window.show()

main_window.btn_0.clicked.connect(partial(num, "0"))
main_window.btn_1.clicked.connect(partial(num, "1"))
main_window.btn_2.clicked.connect(partial(num, "2"))
main_window.btn_3.clicked.connect(partial(num, "3"))
main_window.btn_4.clicked.connect(partial(num, "4"))
main_window.btn_5.clicked.connect(partial(num, "5"))
main_window.btn_6.clicked.connect(partial(num, "6"))
main_window.btn_7.clicked.connect(partial(num, "7"))
main_window.btn_8.clicked.connect(partial(num, "8"))
main_window.btn_9.clicked.connect(partial(num, "9"))
main_window.btn_dot.clicked.connect(partial(num, "."))


main_window.btn_c.clicked.connect(c)
main_window.btn_ac.clicked.connect(ac)

main_window.btn_sum.clicked.connect(partial(num, "+"))
main_window.btn_sub.clicked.connect(partial(num, "-"))
main_window.btn_mul.clicked.connect(partial(num, "×"))
main_window.btn_div.clicked.connect(partial(num, "➗"))
main_window.btn_po.clicked.connect(partial(num, "^"))
main_window.btn_sqrt.clicked.connect(partial(sqrt))
main_window.btn_fac.clicked.connect(partial(fac))
main_window.btn_sin.clicked.connect(partial(sin))
main_window.btn_tan.clicked.connect(partial(tan))
main_window.btn_cos.clicked.connect(partial(cos))
main_window.btn_cot.clicked.connect(partial(cot))
main_window.btn_abs.clicked.connect(partial(abs_))
main_window.btn_rou.clicked.connect(partial(rou))
main_window.btn_eql.clicked.connect(partial(eql))

app.exec_()