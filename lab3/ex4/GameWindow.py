from PySide6.QtWidgets import QMainWindow, QMessageBox
from ex4.game import Ui_MainWindow
from ex4.GameLogic import GameLogic

class GameWindow(QMainWindow):
    def __init__(self, parent=None):
        super(GameWindow, self).__init__(parent)
        self.current_table_index = None
        self.current_table_keys = []
        self.user_data = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.game_logic = GameLogic(self.update_ui, self.on_end)

        self.ui.b1.pressed.connect(lambda: self.game_logic.action(1))
        self.ui.b2.pressed.connect(lambda: self.game_logic.action(2))
        self.ui.b3.pressed.connect(lambda: self.game_logic.action(3))

        self.ui.Start.pressed.connect(self.start)

    def start(self):
        text = self.ui.StartAmount.text()
        if not text.isdigit():
            text = len(text)
        self.game_logic.start(int(text))
        self.ui.stackedWidget.setCurrentIndex(0)

    def update_ui(self, amount):
        self.ui.CurrentAmount.setText(f"Камней: {str(amount)}")

    def on_end(self, is_player):
        text = "Победа!" if is_player else "Поражение"
        QMessageBox.information(self, " ", text, QMessageBox.StandardButton.Ok)
        self.ui.stackedWidget.setCurrentIndex(1)
