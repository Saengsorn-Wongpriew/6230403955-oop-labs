import sys
from PyQt5 import QtWidgets


def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    print(ex.isActiveWindow())
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()