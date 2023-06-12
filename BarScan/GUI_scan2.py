import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QPixmap

from scan_functionlized import *

class ImageDisplayWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Display")
        self.setGeometry(100, 100, 400, 450)

        self.label = QLabel(self)
        self.label.setGeometry(10, 10, 380, 300)
        self.label.setScaledContents(True)

        self.path_label = QLabel(self)
        self.path_label.setGeometry(10, 320, 380, 30)

        self.res_label = QLabel(self)
        self.res_label.setGeometry(10, 320, 380, 50)

        self.button = QPushButton("Select Image", self)
        self.button.setGeometry(150, 360, 100, 130)
        self.button.clicked.connect(self.open_file_dialog)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.path_label)
        layout.addWidget(self.button)

        widget = QWidget(self)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def open_file_dialog(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.bmp)", options=options)
        if file_path:
            self.path_label.setText(file_path)
            res = scan_bar_func(file_path)
            self.res_label.setText(res)
            pixmap = QPixmap(file_path)
            self.label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageDisplayWindow()
    window.show()
    sys.exit(app.exec_())
