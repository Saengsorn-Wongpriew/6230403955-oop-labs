import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, \
    QHBoxLayout, QFormLayout, QPushButton, QLabel, QSlider
from PyQt5.QtGui import QFont
from PyQt5.Qt import Qt


class Calulator(QWidget):
    def __init__(self):
        super().__init__()
        self.label_val = []
        self.slider_val = []
        self.vals = [50, 50]
        self.val_result = 0
        self.oper = -1
        self.cur_but = None

        self.init_ui()

    def init_ui(self):
        self.f_layout = QFormLayout()

        self.new_label("Arial", 20, self.vals[0])
        self.new_slider(self.vals[0])
        self.f_layout.addRow(self.label_val[0], self.slider_val[0])

        self.new_label("Arial", 20, self.vals[1])
        self.new_slider(self.vals[1])
        self.f_layout.addRow(self.label_val[1], self.slider_val[1])

        self.slider_val[0].valueChanged[int].connect(
            lambda x: self.change_val(x, 0)
        )
        self.slider_val[1].valueChanged[int].connect(
            lambda x: self.change_val(x, 1)
        )

        button_names = ['Add', 'Subtract', 'Multiply', 'Divide']
        self.create_buttons(button_names)

        self.result_line()

        self.setLayout(self.f_layout)
        self.setWindowTitle('Simple Calculator')
        self.show()

    def new_label(self, font, size, default_value):
        a_label = QLabel()
        a_label.setFont(QFont(font, size))
        a_label.setStyleSheet("color: blue")
        a_label.setText(str(default_value))
        self.label_val.append(a_label)

    def new_slider(self, default_value):
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(default_value)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickInterval(5)
        self.slider_val.append(slider)

    def create_buttons(self, names):
        buttons = [QPushButton(title) for title in names]
        hbox = QHBoxLayout()
        for b in buttons:
            hbox.addWidget(b)
            self.f_layout.addRow(hbox)
            b.clicked.connect(self.but_change)

    def result_line(self):
        label_res = QLabel('Result')
        label_res.setFont(QFont("Arial", 15))

        self.line_cal_out = QLineEdit()
        self.line_cal_out.setEnabled(False)
        self.line_cal_out.setFont(QFont("Arial", 25))
        self.line_cal_out.setStyleSheet(
            "color: yellow; background-color: grey"
        )
        self.line_cal_out.setAlignment(Qt.AlignRight)
        self.line_cal_out.setMinimumSize(100, 25)
        self.f_layout.addRow(label_res, self.line_cal_out)

    def change_val(self, value, n):
        self.label_val[n].setText(str(value))
        self.vals[n] = value
        self.math_cal()

    def math_cal(self):
        if self.oper >= 0:
            if self.oper == 0:
                self.val_result = str(self.vals[0] + self.vals[1])
            elif self.oper == 1:
                self.val_result = str(self.vals[0] - self.vals[1])
            elif self.oper == 2:
                self.val_result = str(self.vals[0] * self.vals[1])
            elif self.oper == 3:
                if self.vals[1]:
                    self.val_result = "{0:.3g}".format(
                        self.vals[0] / self.vals[1]
                    )
                else:
                    self.val_result = "Cannot Divide by 0"
            self.line_cal_out.setText(self.val_result)

    def but_change(self):
        sender = self.sender()
        if self.cur_but:
            self.cur_but.setStyleSheet(
                "background-color: white"
            )
        sender.setStyleSheet(
            "background-color: lightgreen"
        )
        self.cur_but = sender

        if sender.text() == "Add":
            self.oper = 0
        elif sender.text() == "Subtract":
            self.oper = 1
        elif sender.text() == "Multiply":
            self.oper = 2
        elif sender.text() == "Divide":
            self.oper = 3

        self.math_cal()


def main():
    app = QApplication(sys.argv)
    cal_wid = Calulator()
    print(cal_wid.isActiveWindow())
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
