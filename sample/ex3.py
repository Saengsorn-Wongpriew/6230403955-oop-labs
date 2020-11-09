import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QVBoxLayout, QRadioButton, QPushButton
from PyQt5.QtWidgets import QFormLayout, QHBoxLayout


class FormLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label_name = QLabel("Name")
        edit_name = QLineEdit()

        fbox = QFormLayout()
        fbox.addRow(label_name, edit_name)
        vbox = QVBoxLayout()

        label_addr = QLabel("Address")
        addr1 = QLineEdit()
        addr2 = QLineEdit()

        vbox.addWidget(addr1)
        vbox.addWidget(addr2)
        fbox.addRow(label_addr, vbox)

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

        self.setLayout(fbox)
        self.setWindowTitle("FormLayout")
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = FormLayout()
    print(ex.isActiveWindow)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
