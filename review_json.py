import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import uic


class AddUser(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("review_json.ui", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    add_user = AddUser()
    add_user.show()
    sys.exit(app.exec())
