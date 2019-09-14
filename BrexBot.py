#!/usr/bin/python
__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

import sys
import logging
from Db import Db
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog, QGridLayout, QLabel, QStyle)

class LoginForm(QDialog):

    def __init__(self, parent=None):
        super(LoginForm, self).__init__(parent)
        # TODO: try catch db conn init, raise statusline error on no-connect
        self.dbconn = Db()
        self.setFixedSize(300, 200)

        # get fonts
        self.input_font = QLineEdit("").font()
        self.input_font.setPointSize(14)
        self.label_font = QLabel("").font()
        self.label_font.setPointSize(12)

        # Create widgets
        self.username_label = QLabel("Username")
        self.username_label.setFont(self.label_font)
        self.username = QLineEdit("")
        self.username.setMinimumHeight(30)
        self.username.setFont(self.input_font)

        self.password_label = QLabel("Password")
        self.password_label.setFont(self.label_font)
        self.password = QLineEdit("")
        self.password.setMinimumHeight(30)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setFont(self.input_font)

        self.password2_label = QLabel("Confirm Password")
        self.password2_label.setFont(self.label_font)
        self.password2 = QLineEdit("Confirm password")
        self.password2.setMinimumHeight(30)
        self.password2.setFont(self.input_font)

        self.login_button = QPushButton("Login")
        self.login_button.setMinimumHeight(30)
        self.login_button.setFont(self.label_font)
        self.create_user_button = QPushButton("New user?")
        self.create_user_button.setFont(self.label_font)
        self.create_user_button.setMinimumHeight(30)
        self.create_user_button.setFlat(True)

        # Create layout and add widgets
        layout = QGridLayout()

        layout.addWidget(self.username_label)
        layout.addWidget(self.username)

        layout.addWidget(self.password_label)
        layout.addWidget(self.password)

        # TODO: add spacer thingymajingy
        layout.addWidget(self.login_button)
        layout.addWidget(self.create_user_button)

        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.login_button.clicked.connect(self.try_login)

    def try_login(self):
        try:
            if(self.dbconn.verify_user(self.username.text(), self.password.text())):
                logging.debug("User: " + self.username.text() + " verified and logged in!")
            else:
                logging.debug("User: " + self.username.text() + " verify failed")
        except Exception as e:
            logging.exception("Error on verifying user:", e)

    # Greets the user
    def log(self):
        try:
            logging.debug("User: " + self.username + " trying to log in")
        except Exception as e:
            logging.exception("No username typed")

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)

    # Create and show the form
    form = LoginForm()
    form.setWindowTitle("BrexBot")
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
