import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import uic
import json


class User:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password


class AddUser(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("review_json.ui", self)
        self.pushButton.clicked.connect(self.add_user)
        self.pushButton_2.clicked.connect(self.show_user)

    def show_user(self):
        users_str = ""
        for user in users:
            users_str += f'{user["name"]} - {user["username"]} - {user["password"]}\n'
        self.label_4.setText(users_str)

    def add_user(self):
        name = self.lineEdit.text()
        username = self.lineEdit_2.text()
        password = self.lineEdit_3.text()
        user = User(name, username, password)
        users.append(user.__dict__)
        with open("review_json_data.json", "w") as file:
            file.write(json.dumps(users))


def load_data():
    with open("review_json_data.json", "r") as file:
        data = file.read()
        data = json.loads(data)
        return data


if __name__ == "__main__":
    users = load_data()
    app = QApplication(sys.argv)
    add_user = AddUser()
    add_user.show()
    sys.exit(app.exec())
