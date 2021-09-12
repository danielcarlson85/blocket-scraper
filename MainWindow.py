from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton, QMessageBox
from components import center_window
from components import TextBox_Url

from blocket_scraper import start_blocket_scraper
import sys


class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("QTextEdit")
        self.resize(300, 270)

        self.btnPress1 = QPushButton("Button 1")
        self.textbox = TextBox_Url.create()

        layout = QVBoxLayout()
        layout.addWidget(self.textbox)

        layout.addWidget(self.btnPress1)
        self.setLayout(layout)
        center_window.center(self)

        self.btnPress1.clicked.connect(self.btnPress1_Clicked)

    def btnPress1_Clicked(self):
        found_products = start_blocket_scraper(self.textbox.toPlainText())
        print(found_products[0].name)
        QMessageBox.about(self, "Title", "found" + str(len(found_products)) + " products")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
