import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction


class Dialog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.bar = self.menuBar()
        self.init_ui()

    def init_ui(self):
        file_menu = self.bar.addMenu("File")
        open_act = QAction("Open", self)
        save_act = QAction("Save", self)
        file_menu.addAction(open_act)
        file_menu.addAction(save_act)

        open_act.triggered.connect(self.balls)

        self.show()

    def balls(self):
        print("open")


def main():
    app = QApplication(sys.argv)
    win = Dialog()
    print(win.isActiveWindow())
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
