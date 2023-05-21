import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()

        #Создание осей выравнивания#

        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_second = QHBoxLayout()
        self.hbox_result = QHBoxLayout()

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_result)

        #Создание виджетов#

        self.input = QLineEdit()
        self.hbox_input.addWidget(self.input)

        self.b_1 = QPushButton("1", self)
        self.hbox_first.addWidget(self.b_1)

        self.b_2 = QPushButton("2", self)
        self.hbox_first.addWidget(self.b_2)

        self.b_3 = QPushButton("3", self)
        self.hbox_first.addWidget(self.b_3)

        self.b_4 = QPushButton("4", self)
        self.hbox_first.addWidget(self.b_4)

        self.b_5 = QPushButton("5", self)
        self.hbox_first.addWidget(self.b_5)

        self.b_plus = QPushButton("+", self)
        self.hbox_first.addWidget(self.b_plus)

        self.b_minus = QPushButton("-", self)
        self.hbox_first.addWidget(self.b_minus)

        self.b_clear = QPushButton("AC", self)
        self.hbox_first.addWidget(self.b_clear)

        self.b_6 = QPushButton("6", self)
        self.hbox_second.addWidget(self.b_6)

        self.b_7 = QPushButton("7", self)
        self.hbox_second.addWidget(self.b_7)

        self.b_8 = QPushButton("8", self)
        self.hbox_second.addWidget(self.b_8)

        self.b_9 = QPushButton("9", self)
        self.hbox_second.addWidget(self.b_9)

        self.b_10 = QPushButton("0", self)
        self.hbox_second.addWidget(self.b_10)

        self.b_point = QPushButton(".", self)
        self.hbox_second.addWidget(self.b_point)

        self.b_multiplication = QPushButton("*", self)
        self.hbox_second.addWidget(self.b_multiplication)

        self.b_division = QPushButton("%", self)
        self.hbox_second.addWidget(self.b_division)

        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)

        #Создание реакции нажатия по кнопкам#

        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_multiplication.clicked.connect(lambda: self._operation("*"))
        self.b_division.clicked.connect(lambda: self._operation("%"))
        self.b_result.clicked.connect(self._result)

        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_10.clicked.connect(lambda: self._button("0"))
        self.b_point.clicked.connect(lambda: self._button("."))
        self.b_clear.clicked.connect(lambda: self._clear())

    #Создание метода класса для обработки кнопок, отвечающих за ввод цифр в линию ввода текста#

    def _button(self, parametr):
        line = self.input.text()
        if parametr == ".":
            if parametr not in line:
                self.input.setText(line + parametr)
            return
        self.input.setText(line + parametr)

    # Создание метода класса для обработки нажатия на кнопку математической операции#

    def _operation(self, operation):
        self.num_1 = float(self.input.text())
        self.op = operation
        self.input.setText("")

    # Создание метода класса для обработки нажатия на кнопку результата#

    def _result(self):
        self.num_2 = float(self.input.text())
        if self.op == "+":
            self.input.setText(str(self.num_1 + self.num_2))
        if self.op == "-":
            self.input.setText(str(self.num_1 - self.num_2))
        if self.op == "*":
            self.input.setText(str(self.num_1 * self.num_2))
        if self.op == "%":
            try:
                self.input.setText(str(self.num_1 / self.num_2))
            except:
                self.input.setText("% Error %")

    #Очистить поле#

    def _clear(self):
        self.input.setText("")

#Запуск приложения#

app = QApplication(sys.argv)

win = Calculator()
win.show()

sys.exit(app.exec_())

