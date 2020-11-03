import sys
from PyQt5 import QtWidgets


class Example(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        title = QtWidgets.QLabel('Title')
        author = QtWidgets.QLabel('Author')
        review = QtWidgets.QLabel('Review')
        boxh = QtWidgets.QHBoxLayout()
        boxv = QtWidgets.QVBoxLayout()

        titleEdit = QtWidgets.QLineEdit()
        authorEdit = QtWidgets.QLineEdit()
        reviewEdit = QtWidgets.QTextEdit()

        ok_but = QtWidgets.QPushButton('OK')
        can_but = QtWidgets.QPushButton('Cancel')

        grid = QtWidgets.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 0, 0)
        grid.addWidget(titleEdit, 0, 1)

        grid.addWidget(author, 1, 0)
        grid.addWidget(authorEdit, 1, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        boxv.addLayout(grid)
        boxh.addStretch(1)
        boxh.addWidget(ok_but)
        boxh.addWidget(can_but)
        boxv.addStretch(1)
        boxv.addLayout(boxh)
        self.setLayout(boxv)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review by {}'.format(sys.argv[1]))

        self.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    print(ex.isActiveWindow())
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
