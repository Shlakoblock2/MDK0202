from PySide6.QtWidgets import QMainWindow
from src.client.ui.main import Ui_MainWindow
import random

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.current_table_index = None
        self.current_table_keys = []
        self.user_data = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.onoff.pressed.connect(self.button_on_off)
        self.ui.rand.pressed.connect(self.shuffle_list)
        for i in range(10):
            self.ui.list.addItem(str(i))

    def button_on_off(self):
        self.ui.list.setVisible(not self.ui.list.isVisible())
        self.ui.onoff.setText("on") if self.ui.list.isVisible() else self.ui.onoff.setText("off")

    def shuffle_list(self):
        items = []
        for i in range(self.ui.list.count()):
            items.append(self.ui.list.item(i).text())
        random.shuffle(items)
        self.ui.list.clear()
        print(items)
        self.ui.list.addItems(items)
