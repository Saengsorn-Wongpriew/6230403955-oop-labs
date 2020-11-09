import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox


class ยาย(QWidget):
    def __init__(ตัวเอง):
        super().__init__()
        ตัวเอง.init_ตา()

    def init_ตา(ตัวเอง):
        ไก่ = QCheckBox('obama', ตัวเอง)
        ไก่.move(1, 1)


def เมน():
    แอป = QApplication(sys.argv)
    กาก = ยาย()
    กาก.show()
    sys.exit(แอป.exec_())


if __name__ == "__main__":
    เมน()
