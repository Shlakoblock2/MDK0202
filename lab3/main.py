import sys

from PySide6.QtWidgets import QApplication
from ex4.GameWindow import GameWindow
from ex1.FlagWindow import FlagWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GameWindow()
    window.show()
    sys.exit(app.exec())