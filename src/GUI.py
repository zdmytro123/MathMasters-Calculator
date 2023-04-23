from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import math
import random
import logic
import re

class CALCULATOR(QWidget):

    def __init__(self):
        super().__init__()
        self.draggable = True
        self.mousePresspos = None
        self.mouseMovePos = None
        self.setMouseTracking(True)
        self.title = 'MATHMASTERS CALCULATOR'
        self.left = 10
        self.top = 40
        self.width = 1060
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: #000000;")
        self.setFixedSize(self.width, self.height)
        main_layout = QVBoxLayout(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        def output_style (self):
            self.output = QLineEdit(self)
            self.output.setFixedSize(1030, 50)
            self.output.setFocusPolicy(Qt.ClickFocus)
            self.output.setAlignment(QtCore.Qt.AlignRight)
            self.output.setCursor(QCursor(Qt.IBeamCursor))
            self.output.mousePressEvent = lambda _: self.output.setFocus(True)
            self.output.setReadOnly(False)
            self.output.setStyleSheet(f"background-color: #000000; color: #FFFFFF ; font-family: Comic Sans MS; font-size: 20px; border-radius: 15px; border: 2px solid #FFFFFF;")
            self.output.setPlaceholderText(" ")
            self.output.setMaxLength(100)
            self.output.setDragEnabled(True)
            self.show()
        output_style(self)

	###################KeyBoard###################
        def keyPressEvent(self, event):
            key = event.key()
            if key >= QtCore.Qt.Key_0 and key <= QtCore.Qt.Key_9:
                click_number(key)
            else:
                if key == QtCore.Qt.Key_Plus:
                    click_plus()
                elif key == QtCore.Qt.Key_Minus:
                    click_minus()
                elif key == QtCore.Qt.Key_Asterisk:
                    click_multiply()
                elif key == QtCore.Qt.Key_Slash:
                    click_divide()
                elif key == QtCore.Qt.Key_Period:
                    click_comma()
                elif key == QtCore.Qt.Key_Return:
                    click_equals()
                elif key == QtCore.Qt.Key_Backspace:
                    clear_last()
                elif key == QtCore.Qt.Key_Escape:
                    click_clear()
                elif key == QtCore.Qt.Key_ParenLeft:
                    click_LBrace()
                elif key == QtCore.Qt.Key_ParenRight:
                    click_RBrace
                else:
                    pass

                keyPressEvent(self, event)

	############################# LAYOUTS ########################################
        buttons_layout = QGridLayout()
        main_layout.addWidget(self.output)
        main_layout.addLayout(buttons_layout)

	############################# BUTTONS ########################################
        def click_NONE():
            self.output.setText(self.output.text() + "")

        def click_number(num):
            self.output.setText(self.output.text() + str(num))

        def click_plus():
            self.output.setText(self.output.text() + "+")

        def click_minus():
            self.output.setText(self.output.text() + "-")

        def click_multiply():
            self.output.setText(self.output.text() + "*")

        def click_divide():
            self.output.setText(self.output.text() + "/")

        def click_power():
            self.output.setText(self.output.text() + "^")

        def click_comma():
            self.output.setText(self.output.text() + ".")

        def click_equals():

            try:
                text = self.output.text()

                if 'e' in text:
                    self.output.setText(str(logic.e()))

                if 'п' in text:
                    self.output.setText(str(logic.pi()))

                def make_expression(tokens):
                    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '√': 4, 'abs': 4, '!': 4, '(': 5, ')': 5}
                    operators = []
                    operands = []
                    for token in tokens:
                        if token.isdigit():
                            operands.append(float(token))
                        elif token == '(':
                            operators.append(token)
                        elif token == ')':
                            while operators[-1] != '(':
                                op = operators.pop()
                                right = operands.pop()
                                left = operands.pop()
                                operands.append((op, left, right))
                            operators.pop()
                            if operators and operators[-1] in ('√', 'abs', '!'):
                                op = operators.pop()
                                right = operands.pop()
                                left = operands.pop()
                                operands.append((op, left, right))
                        elif token in precedence:
                            while operators and operators[-1] != '(' and precedence[operators[-1]] >= precedence[token]:
                                op = operators.pop()
                                right = operands.pop()
                                left = operands.pop()
                                operands.append((op, left, right))
                            operators.append(token)
                        else:
                            raise ValueError(f"Invalid token: {token}")
                    while operators:
                        op = operators.pop()
                        right = operands.pop()
                        left = operands.pop()
                        operands.append((op, left, right))
                    return operands[0]

                def parse_input(input_string):
                    tokens = re.findall(r'\(|\)|\d+|[+\-*/^]|√|abs|!', input_string)
                    return tokens

                def evaluate(expression):
                    if isinstance(expression, float):
                        return expression
                    op, left, right = expression
                    if op == '+':
                        return logic.add(evaluate(left), evaluate(right))
                    elif op == '-':
                        return logic.sub(evaluate(left), evaluate(right))
                    elif op == '*':
                        return logic.mul(evaluate(left), evaluate(right))
                    elif op == '/':
                        return logic.div(evaluate(left), evaluate(right))
                    elif op == '^':
                        return logic.exponentiation(evaluate(left), evaluate(right))
                    elif op == '√':
                        return logic.sqrt(evaluate(right), evaluate(left))
                    elif op == '|':
                        return logic.abs(evaluate(left))
                    elif op == '!':
                        return logic.factorial(evaluate(left))

                tokens = parse_input(text)
                expression_tree = make_expression(tokens)
                result = evaluate(expression_tree)
                self.output.setText(str(result))

                """ if "+" in text:
                    num1, num2 = text.split("+")
                    num1, num2 = map(float, [num1, num2])
                    text1 = logic.add(num1, num2)
                if ("-" in text) and ("|" not in text):
                    num1, num2 = text.split("-")
                    num1, num2 = map(float, [num1, num2])
                    text1 = logic.sub(num1, num2)
                if "*" in text:
                    num1, num2 = text.split("*")
                    num1, num2 = map(float, [num1, num2])
                    text1 = logic.mul(num1, num2)
                if "/" in text:
                    num1, num2 = text.split("/")
                    num1, num2 = map(float, [num1, num2])
                    text1 = logic.div(num1, num2)
                if "π" in text:
                    text1 = text.replace("π", str(logic.pi()))
                if "e" in text:
                    text1 = text.replace("e", str(logic.e()))
                if "√" in text:
                    num1, num2 = text.split("√")
                    if not num1:
                        num1 = "2"
                    num1, num2 = map(float, [num1, num2])
                    text1 = logic.sqrt(num2, num1)
                if "!" in text:
                    text1 = logic.factorial(eval(text.replace("!", "")))
                if "|" in text:
                    text = text.replace("-", "")
                    text1 = logic.abs(eval(text.replace("|", "")))
                if "^" in text:
                    num1, num2 = text.split("^")
                    num1, num2 = map(float, [num1, num2])
                    text1 = logic.exponentiation(num1, num2)

                self.output.setText(str(round(text1, 10)))"""

            except ZeroDivisionError:
                self.output.setText("Math Error")
            except SyntaxError:
                self.output.setText("Syntax Error")

        def click_clear():
            self.output.setText("")

        def clear_last():
            self.output.setText(self.output.text()[:-1])

        def click_root():
            self.output.setText(self.output.text() + "√")

        def click_factorial():
            self.output.setText(self.output.text() + "!")

        def click_pi():
            self.output.setText(self.output.text() + "π")

        def click_e():
            self.output.setText(self.output.text() + "e")

        def click_LBrace():
            self.output.setText(self.output.text() + "(")

        def click_RBrace():
            self.output.setText(self.output.text() + ")")

        def click_module():
            self.output.setText(self.output.text() + "|")

        def click_close():
            self.close()

        def click_minimize():
            self.showMinimized()

        def click_FIT():
            pixmap = QPixmap("C:/Users/kiril/OneDrive/Рабочий стол/PROGRAMING/PYTHON/FIT.png")
            url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            button.setStyleSheet(f"background-image: url({pixmap.toImage()}); border-radius: 15px; border: 2px solid red;")
            button.setCursor(QCursor(Qt.PointingHandCursor))
            href_label = QLabel(f'<a href="{url}"></a>')
            href_label.setOpenExternalLinks(True)
            href_label.linkActivated.connect(lambda: QDesktopServices.openUrl(QUrl(url)))
            return href_label

        def click_help():
            self.help_window = QWidget()
            self.help_window.setWindowTitle("Help")
            self.help_window.setFixedSize(800, 400)
            self.help_window.setStyleSheet("background-color: #000000;")
            self.help_window_layout = QVBoxLayout(self.help_window)
            self.help_window_label = QLabel(self.help_window)
            self.help_window_label.setText("This is a simple calculator.")
            self.help_window_label.setStyleSheet("background-color: #000000; color: #FFFFFF; font-family: Comic Sans MS; font-size: 20px; font-weight: bold; text-align: center;")
            self.help_window_layout.addWidget(self.help_window_label)
            self.help_window.show()

        def style_for_button(button):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            if r + g + b > 400:
                r -= 50
                g -= 50
                b -= 50
            color = QColor(r, g, b)
            button.setFixedSize(100, 100)
            button.setStyleSheet(f"background-color: #FFFFFF; color: {color.name()}; font-size: 20px; font-weight: bold; text-align: center; border-radius: 15px; border: 2px solid {color.name()};")
            button.setCursor(QCursor(Qt.PointingHandCursor))
            button.enterEvent = lambda _: button.setStyleSheet(f"background-color: {color.name()}; color: #000000; font-size: 20px; font-weight: bold; text-align: center; border-radius: 15px; border: 2px solid #FFFFFF;")
            button.leaveEvent = lambda _: button.setStyleSheet(f"background-color: #FFFFFF; color: {color.name()}; font-size: 20px; font-weight: bold; text-align: center; border-radius: 15px; border: 2px solid {color.name()};")

        def style_for_button2(button):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = QColor(r, g, b)
            button.setFixedSize(100, 100)
            button.setStyleSheet(f"background-color: #000000; color: {color.name()}; font-size: 20px; font-weight: bold; text-align: center; border-radius: 15px; border: 2px solid {color.name()};")
            button.setCursor(QCursor(Qt.PointingHandCursor))
            button.enterEvent = lambda _: button.setStyleSheet(f"background-color: {color.name()}; color: #000000; font-size: 20px; font-weight: bold; text-align: center; border-radius: 15px; border: 2px solid #000000;")
            button.leaveEvent = lambda _: button.setStyleSheet(f"background-color: #000000; color: {color.name()}; font-size: 20px; font-weight: bold; text-align: center; border-radius: 15px; border: 2px solid {color.name()};")

        for i in range(1, 10):
            button = QPushButton(str(i))
            button.clicked.connect(lambda _, num=i: click_number(num))
            style_for_button(button)
            buttons_layout.addWidget(button, (i-1)//3, (i-1)%3, alignment=Qt.AlignCenter)

        plus_button = QPushButton("+")
        plus_button.clicked.connect(click_plus)
        style_for_button2(plus_button)
        buttons_layout.addWidget(plus_button, 0, 3, alignment=Qt.AlignCenter)

        power_button = QPushButton("^")
        power_button.clicked.connect(click_power)
        style_for_button2(power_button)
        buttons_layout.addWidget(power_button, 0, 4, alignment=Qt.AlignCenter)

        e_button = QPushButton("e")
        e_button.clicked.connect(click_e)
        style_for_button2(e_button)
        buttons_layout.addWidget(e_button, 0, 5, alignment=Qt.AlignCenter)

        minus_button = QPushButton("-")
        minus_button.clicked.connect(click_minus)
        style_for_button2(minus_button)
        buttons_layout.addWidget(minus_button, 1, 3, alignment=Qt.AlignCenter)

        comma_button = QPushButton(".")
        comma_button.clicked.connect(click_comma)
        style_for_button2(comma_button)
        buttons_layout.addWidget(comma_button, 1, 4, alignment=Qt.AlignCenter)

        pi_button = QPushButton("π")
        pi_button.clicked.connect(click_pi)
        style_for_button2(pi_button)
        buttons_layout.addWidget(pi_button, 1, 5, alignment=Qt.AlignCenter)

        multiply_button = QPushButton("×")
        multiply_button.clicked.connect(click_multiply)
        style_for_button2(multiply_button)
        buttons_layout.addWidget(multiply_button, 2, 3, alignment=Qt.AlignCenter)

        root_button = QPushButton("√")
        root_button.clicked.connect(click_root)
        style_for_button2(root_button)
        buttons_layout.addWidget(root_button, 2, 4, alignment=Qt.AlignCenter)

        close_button = QPushButton("Close")
        close_button.clicked.connect(click_close)
        style_for_button2(close_button)
        buttons_layout.addWidget(close_button, 2, 5, alignment=Qt.AlignCenter)

        clear_button = QPushButton("🗑")
        clear_button.clicked.connect(click_clear)
        style_for_button2(clear_button)
        buttons_layout.addWidget(clear_button, 3, 0, alignment=Qt.AlignCenter)
        zero_button = QPushButton("0")
        zero_button.clicked.connect(lambda: click_number(0))
        style_for_button(zero_button)
        buttons_layout.addWidget(zero_button, 3, 1, alignment=Qt.AlignCenter)

        clear_last_button = QPushButton("⌫")
        clear_last_button.clicked.connect(clear_last)
        style_for_button2(clear_last_button)
        buttons_layout.addWidget(clear_last_button, 3,2, alignment=Qt.AlignCenter)

        divide_button = QPushButton("÷")
        divide_button.clicked.connect(click_divide)
        style_for_button2(divide_button)
        buttons_layout.addWidget(divide_button, 3, 3, alignment=Qt.AlignCenter)

        factorial_button = QPushButton("!")
        factorial_button.clicked.connect(click_factorial)
        style_for_button2(factorial_button)
        buttons_layout.addWidget(factorial_button, 3, 4, alignment=Qt.AlignCenter)

        minimize_button = QPushButton("Minimize")
        minimize_button.clicked.connect(click_minimize)
        style_for_button2(minimize_button)
        buttons_layout.addWidget(minimize_button, 3, 5, alignment=Qt.AlignCenter)

        LBrace_button = QPushButton("(")
        LBrace_button.clicked.connect(click_LBrace)
        style_for_button2(LBrace_button)
        buttons_layout.addWidget(LBrace_button, 4, 0, alignment=Qt.AlignCenter)

        module_button = QPushButton("|")
        module_button.clicked.connect(click_module)
        style_for_button2(module_button)
        buttons_layout.addWidget(module_button, 4, 1, alignment=Qt.AlignCenter)

        RBrace_button = QPushButton(")")
        RBrace_button.clicked.connect(click_RBrace)
        style_for_button2(RBrace_button)
        buttons_layout.addWidget(RBrace_button, 4, 2, alignment=Qt.AlignCenter)

        equals_button = QPushButton("=")
        equals_button.clicked.connect(click_equals)
        style_for_button2(equals_button)
        buttons_layout.addWidget(equals_button, 4, 3, alignment=Qt.AlignCenter)

        help_button = QPushButton("Help")
        help_button.clicked.connect(click_help)
        style_for_button2(help_button)
        buttons_layout.addWidget(help_button, 4, 4, alignment=Qt.AlignCenter)

        fit_buton = QPushButton("FIT")
        fit_buton.clicked.connect(click_FIT)
        style_for_button2(fit_buton)
        buttons_layout.addWidget(fit_buton, 4, 5, alignment=Qt.AlignCenter)

        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = CALCULATOR()
    sys.exit(app.exec_())
