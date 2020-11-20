import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QAction,
    QMenu, QFileDialog, QTextEdit, QColorDialog
)
from PyQt5.QtGui import QKeySequence, QFont
from PyQt5.QtCore import QDir


class Dialog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.bar = self.menuBar()
        self.editor = QTextEdit()
        self.bg_color = None
        self.font_color = None
        self.cur_save_path = ""
        self.init_ui()

    def init_ui(self):
        self.create_file_menu()
        self.create_edit_menu()

        self.editor.setFont(QFont("Arial", 12))
        self.setCentralWidget(self.editor)

        self.setWindowTitle('File dialog')
        self.setGeometry(500, 300, 600, 500)
        self.show()

    def create_file_menu(self):
        file_menu = self.bar.addMenu("File")
        open_act = QAction('Open', self)
        open_act.setShortcut(QKeySequence('Ctrl+O'))
        open_act.triggered.connect(self.get_text_file)
        save_act = QAction('Save', self)
        save_act.setShortcut(QKeySequence('Ctrl+S'))
        save_act.triggered.connect(self.write_text_file)
        file_menu.addAction(open_act)
        file_menu.addAction(save_act)

    def create_edit_menu(self):
        edit_menu = self.bar.addMenu("Edit")
        bg_act = QAction('Background color', self)
        fg_act = QAction('Foreground color', self)
        bg_act.triggered.connect(self.change_color_style)
        fg_act.triggered.connect(self.change_color_style)
        color_menu = QMenu('Color', self)
        font_act = QAction('Font', self)
        color_menu.addAction(bg_act)
        color_menu.addAction(fg_act)
        edit_menu.addMenu(color_menu)
        edit_menu.addAction(font_act)

    def get_text_file(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec_():
            file_name = dialog.selectedFiles()

            with open(file_name[0], 'r', encoding='utf-8') as f:
                data = f.read()
                self.editor.setPlainText(data)
                f.close()

    def write_text_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(
            self, "QFileDialog.getSaveFileName()", "",
            "All Files (*);;Text Files (*.txt)", options=options
        )
        if file_name:
            self.cur_save_path = file_name
            with open(self.cur_save_path, "w") as f:
                f.write(self.editor.toPlainText())
                f.close()

    def change_color_style(self):
        sender = self.sender()
        color = QColorDialog.getColor()
        if sender.text() == 'Foreground color':
            color_name = color.name()
            self.font_color = color_name
        elif sender.text() == 'Background color':
            color_name = color.name()
            self.bg_color = color_name
        self.editor.setStyleSheet(
            "background-color: {}; color: {}"
            "".format(self.bg_color, self.font_color)
        )


def main():
    app = QApplication(sys.argv)
    win = Dialog()
    print(win.isActiveWindow())
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
