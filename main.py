import loginUI
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    loginUi = loginUI.Ui_Form()
    loginUi.setupUi(win)
    win.show()
    sys.exit(app.exec_())