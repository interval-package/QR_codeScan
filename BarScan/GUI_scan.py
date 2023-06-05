import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog

from scan_functionlized import *

class FileViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文件浏览器')
        layout = QVBoxLayout()

        self.label = QLabel('文件解析结果会在这里')
        layout.addWidget(self.label)

        self.button = QPushButton('选择文件')
        self.button.clicked.connect(self.openFile)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def openFile(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "All Files (*);;Text Files (*.txt)", options=options)
        if file_path:
            self.label.setText(file_path)
            res = scan_bar_func(file_path)
            self.label.setText(res)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileViewer()
    window.show()
    sys.exit(app.exec_())
