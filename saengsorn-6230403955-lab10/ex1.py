import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QMessageBox, QPushButton


class Exercise1(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        WIDTH = 300
        HEIGHT = 200
        self.setGeometry(1200, 600, WIDTH, HEIGHT)
        self.setWindowTitle('Exercise 1')
        label = QLabel('My name is ' + sys.argv[1], self)
        label.move(90, 80)
        btn = QPushButton('Quit', self)
        btn.clicked.connect(QApplication.instance().quit)
        btn.setToolTip('Click to exit')
        btn.move(100, 100)
        self.show()

    def closeEvent(self, e):
        reply = QMessageBox.question(
            self, 'Quit', 'Are you sure you want to quit?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            e.accept()
        else:
            e.ignore()


def main():
    app = QApplication(sys.argv)
    ex1 = Exercise1()
    print(ex1.isActiveWindow())
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
