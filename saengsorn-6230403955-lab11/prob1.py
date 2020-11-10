import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtWidgets import QFormLayout, QVBoxLayout, QLineEdit
from PyQt5.QtWidgets import QRadioButton, QHBoxLayout, QPushButton


class SimpleForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FormLayout")
        self.init_line_edit()

    def init_line_edit(self):
        fbox = QFormLayout()
        self.setLayout(fbox)
        label_sf = QLabel('SimpleForm')
        label_sf.setStyleSheet("color: blue; font: bold 20px")

        vbox = QVBoxLayout()
        fbox.addRow(None, label_sf)

        label_name = QLabel('Name')
        fbox.addRow(label_name, vbox)

        edit_name = QLineEdit()
        edit_name.setMinimumWidth(300)
        fbox.addRow(label_name, edit_name)

        hbox = QHBoxLayout()
        radio_male = QRadioButton("Male")
        radio_female = QRadioButton("Female")
        hbox.addWidget(radio_male)
        hbox.addWidget(radio_female)
        hbox.addStretch()
        fbox.addRow(QLabel("Gender"), hbox)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(QPushButton("Submit"))
        hbox.addWidget(QPushButton("Cancel"))
        fbox.addRow(hbox)


def main():
    app = QApplication(sys.argv)
    ex = SimpleForm()
    ex.show()
    print(ex.isActiveWindow())
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
