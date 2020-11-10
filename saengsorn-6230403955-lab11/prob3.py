import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtWidgets import QFormLayout, QVBoxLayout, QLineEdit
from PyQt5.QtWidgets import QHBoxLayout, QPushButton
from PyQt5.QtWidgets import QCheckBox


class SimpleForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FormLayout")
        self.init_line_edit()

    def init_line_edit(self):
        fbox = QFormLayout()
        self.setLayout(fbox)

        vbox = QVBoxLayout()

        label_name = QLabel('Name')
        fbox.addRow(label_name, vbox)

        self.edit_name = QLineEdit()
        self.edit_name.setMinimumWidth(300)
        fbox.addRow(label_name, self.edit_name)

        hbox = QHBoxLayout()
        pyqt_cbox = QCheckBox('PyQt')
        pyqt_cbox.setChecked(True)
        pygame_cbox = QCheckBox('PyGame')
        pytrch_cbox = QCheckBox('PyTorch')

        hbox.addWidget(pyqt_cbox)
        hbox.addWidget(pygame_cbox)
        hbox.addWidget(pytrch_cbox)
        hbox.addStretch()
        fbox.addRow(QLabel("Gender"), hbox)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        submit_button = QPushButton("Submit")
        hbox.addWidget(submit_button)
        hbox.addWidget(QPushButton("Cancel"))
        fbox.addRow(hbox)

        submit_button.clicked.connect(self.say_name)
        pyqt_cbox.stateChanged.connect(lambda: self.cbox_change(pyqt_cbox))
        pygame_cbox.stateChanged.connect(lambda: self.cbox_change(pygame_cbox))
        pytrch_cbox.stateChanged.connect(lambda: self.cbox_change(pytrch_cbox))

    def say_name(self):
        print("Name is", self.edit_name.text())

    def cbox_change(self, cbox):
        if cbox.isChecked():
            print(cbox.text(), "is selected")
        else:
            print(cbox.text(), "is deselected")


def main():
    app = QApplication(sys.argv)
    ex = SimpleForm()
    ex.show()
    print(ex.isActiveWindow())
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
