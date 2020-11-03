import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui


class Example(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.qtw = QtWidgets
        self.qticon = QtGui.QIcon
        self.init_ui()

    def init_ui(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu('File')

        edt_menu = self.qtw.QMenu('Edit', self)
        edt_act = self.qtw.QAction('Copy', self)
        pste_act = self.qtw.QAction('Paste', self)

        edt_menu.addAction(edt_act)
        edt_menu.addAction(pste_act)

        new_act = self.qtw.QAction('New', self)
        save_act = self.qtw.QAction('Save', self)
        save_act.setShortcut('Ctrl+S')

        file_menu.addAction(new_act)
        file_menu.addMenu(edt_menu)
        file_menu.addAction(save_act)

        exit_act = self.qtw.QAction(
            self.qticon('moveon_in_life.png'),
            'Exit', self
        )
        exit_act.setShortcut('Ctrl+Q')
        exit_act.setStatusTip('Exit application')
        exit_act.triggered.connect(self.qtw.QApplication.instance().quit)

        file_menu.addAction(exit_act)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Exercise 2')

        self.statusBar().addPermanentWidget(
            QtWidgets.QLabel('By {}'.format(sys.argv[1])), 1
        )

        self.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    print(ex.isActiveWindow())
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
