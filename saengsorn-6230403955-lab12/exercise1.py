import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, \
    QHBoxLayout, QFormLayout, QPushButton, QLabel, QSlider
from PyQt5.QtGui import QFont
from PyQt5.Qt import Qt


class Calulator(QWidget):
    def __init__(self):
        super().__init__()
        self.val_1 = 50
        self.val_2 = 50
        self.val_result = self.val_1 + self.val_2
        self.oper = -1
        self.cur_but = None

        self.init_ui()

    def init_ui(self):
        f_layout = QFormLayout()

        val_1_slid = QSlider(Qt.Horizontal)
        val_1_slid.setMinimum(0)
        val_1_slid.setMaximum(100)
        val_1_slid.setValue(self.val_1)
        val_1_slid.setTickPosition(QSlider.TicksBelow)
        val_1_slid.setTickInterval(5)

        self.label_1 = QLabel()
        self.label_1.setFont(QFont("Arial", 20))
        self.label_1.setStyleSheet("color: blue")
        self.label_1.setText(str(self.val_1))

        f_layout.addRow(self.label_1, val_1_slid)

        val_1_slid.valueChanged[int].connect(
            self.change_val_1
        )
        val_2_slid = QSlider(Qt.Horizontal)
        val_2_slid.setMinimum(0)
        val_2_slid.setMaximum(100)
        val_2_slid.setValue(self.val_2)
        val_2_slid.setTickPosition(QSlider.TicksBelow)
        val_2_slid.setTickInterval(5)

        self.label_2 = QLabel()
        self.label_2.setFont(QFont("Arial", 20))
        self.label_2.setStyleSheet("color: blue")
        self.label_2.setText(str(self.val_2))

        f_layout.addRow(self.label_2, val_2_slid)

        val_2_slid.valueChanged[int].connect(
            self.change_val_2
        )

        titles = ['Add', 'Subtract', 'Multiply', 'Divide']
        buttons = [QPushButton(title) for title in titles]

        hbox = QHBoxLayout()

        for b in buttons:
            hbox.addWidget(b)
            f_layout.addRow(hbox)
            b.clicked.connect(self.but_change)

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

        f_layout.addRow(label_res, self.line_cal_out)

        self.setLayout(f_layout)
        self.setWindowTitle('Simple Calculator')
        self.show()

    def change_val_1(self, value):
        self.label_1.setText(str(value))
        self.val_1 = value
        self.math_cal()

    def change_val_2(self, value):
        self.label_2.setText(str(value))
        self.val_2 = value
        self.math_cal()

    def math_cal(self):
        if self.oper >= 0:
            if self.oper == 0:
                self.val_result = str(self.val_1 + self.val_2)
            elif self.oper == 1:
                self.val_result = str(self.val_1 - self.val_2)
            elif self.oper == 2:
                self.val_result = str(self.val_1 * self.val_2)
            elif self.oper == 3:
                if self.val_2:
                    self.val_result = "{0:.3g}".format(self.val_1 / self.val_2)
                else:
                    self.val_result = "No Error"
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
