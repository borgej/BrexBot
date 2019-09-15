#!/usr/bin/python
from PySide2.QtCore import Slot

__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

import sys
import logging
import Config
from Db import Db
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
                               QVBoxLayout, QDialog, QGridLayout, QLabel, QStyle, QSpacerItem, QSizePolicy, QMessageBox,
                               QMainWindow, QAction, )

class LoginForm(QDialog):

    def __init__(self, main_window, parent=None):
        self.main_window = main_window
        super(LoginForm, self).__init__(parent)
        # TODO: try catch db conn init, raise statusline error on no-connect
        try:
            self.dbconn = Db()
        except ConnectionRefusedError as refused:
            QMessageBox.critical(self, "Connection refused",
                                                "Problems connecting to the death star, try again", QMessageBox.Abort)
            logging.exception("Can't connect to the database, connection refused", refused)
        except ConnectionError as error:
            QMessageBox.critical(self, "Connection refused",
                                                "Problems connecting to the death star, try again", QMessageBox.Abort)
            logging.exception("Can't connect to the database, connection error", error)
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
        self.username.setStyleSheet('''
                                    QLineEdit {
                                        border: 1px solid rgb(63, 63, 63);
                                        background-color: #CFCFCF;
                                    }''')

        self.password_label = QLabel("Password")
        self.password_label.setFont(self.label_font)
        self.password = QLineEdit("")
        self.password.setMinimumHeight(30)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setFont(self.input_font)
        self.password.setStyleSheet('''
                                            QLineEdit {
                                                border: 1px solid rgb(63, 63, 63);
                                                background-color: #CFCFCF;
                                            }''')

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
        layout.addItem(QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        layout.addWidget(self.password_label)
        layout.addWidget(self.password)
        layout.addItem(QSpacerItem(0, 35, QSizePolicy.Expanding, QSizePolicy.Minimum))

        layout.addWidget(self.login_button)
        layout.addWidget(self.create_user_button)

        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.login_button.clicked.connect(self.try_login)

    def try_login(self):
        try:
            user_login = self.dbconn.verify_user(self.username.text(), self.password.text())
            if(user_login.username == self.username.text()):
                logging.debug("User: " + self.username.text() + " verified and logged in!")

                self.main_window.show()
                self.close()

            else:
                logging.debug("User: " + self.username.text() + " verify failed")
                flags = QMessageBox.StandardButton.Ok
                msg = "You have typed a wrong username and/or password. \nPlease try again..."
                QMessageBox.warning(self, "Wrong username/password", msg, flags)
        except Exception as e:
            logging.exception("Error on verifying user:", e)

    # Greets the user
    def log(self):
        try:
            logging.debug("User: " + self.username + " trying to log in")
        except Exception as e:
            logging.exception("No username typed")

# TODO
class BrexBot(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("BrexBot " + Config.VERSION)

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")
        self.help_menu = self.menu.addMenu("Help")

        self.file_menu.setStyleSheet("""
                                    QMenuBar {
                                        background-color: '#B6B6B6 !important';
                                    }
                            
                                    QMenuBar::item {
                                        background-color: '#B6B6B6 !important';
                                        
                                    }
                            
                                    QMenuBar::item::selected {
                                        background-color: '#9E9E9E !important';
                                    }
                            
                                """)
        ## User Preferences
        user_preferences = QAction("User preferences", self)
        user_preferences.setShortcut("Ctrl+U")
        user_preferences.triggered.connect(self.user_preferences)

        ## Preferences
        preferences = QAction("Preferences", self)
        preferences.setShortcut("Ctrl+P")
        preferences.triggered.connect(self.preferences)

        ## Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)

        self.file_menu.addAction(user_preferences)
        self.file_menu.addAction(preferences)
        self.file_menu.addAction(exit_action)

        # Status Bar
        self.status = self.statusBar()
        self.status.showMessage("BrexBot loaded! Time to play Country Roads!")

        # Window dimensions
        geometry = app.desktop().availableGeometry(self)
        self.resize(geometry.width() * 0.6, geometry.height() * 0.75)
        # set maximum size
        self.setMaximumSize(geometry.width(), geometry.height())

    @Slot()
    def exit_app(self, checked):
        sys.exit()

    # TODO
    @Slot()
    def preferences(self, checked):
        pass

    # TODO
    @Slot()
    def user_preferences(self, checked):
        pass


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    qmainwindowcolor_color = "QMainWindow {background-color: #888888}"
    qdialog_color = "QDialog {background-color: #888888}"
    # project variables
    user = None
    channel = None

    # Create main application instance
    main_window = BrexBot()
    main_window.setStyleSheet(qmainwindowcolor_color)

    # Create and show the login form
    login_window = LoginForm(main_window)
    login_window.setWindowTitle("BrexBot")
    login_window.setStyleSheet(qdialog_color)
    login_window.show()

    sys.exit(app.exec_())
