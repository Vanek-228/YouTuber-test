from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton


def show_lose():
    add_window = QMessageBox()
    add_window.setText('Нет, в 2015 году\nВы выиграли фирменный плакат')
    add_window.setWindowTitle('Результат теста:')
    add_window.exec_()


def show_win():
    add_losewindow = QMessageBox()
    add_losewindow.setText('Верно!\nВы выиграли гироскутер')
    add_losewindow.setWindowTitle('Результат теста:')   
    add_losewindow.exec_()


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Конкурс от Crazy People')
main_win.resize(400, 200)

which = QLabel('В каком году канал получил "золотую кнопку" от YouTube?')
button1 = QRadioButton('2005')
button2 = QRadioButton('2010')
button3 = QRadioButton('2015')
button4 = QRadioButton('2020')

v_line = QVBoxLayout()
h_line = QHBoxLayout()
h1_line = QHBoxLayout()
h2_line = QHBoxLayout() 

h_line.addWidget(which, alignment = Qt.AlignCenter)
h1_line.addWidget(button1, alignment = Qt.AlignCenter)
h1_line.addWidget(button2, alignment = Qt.AlignCenter)
h2_line.addWidget(button3, alignment = Qt.AlignCenter)
h2_line.addWidget(button4, alignment = Qt.AlignCenter)

v_line.addLayout(h_line)
v_line.addLayout(h1_line)
v_line.addLayout(h2_line)
main_win.setLayout(v_line)

button1.clicked.connect(show_lose)
button2.clicked.connect(show_lose)
button3.clicked.connect(show_win)
button4.clicked.connect(show_lose)

main_win.show()
app.exec_()