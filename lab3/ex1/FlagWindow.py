from PySide6.QtWidgets import QMainWindow, QMessageBox
from ex1.flag import Ui_MainWindow

class FlagWindow(QMainWindow):
    def __init__(self, parent=None):
        super(FlagWindow, self).__init__(parent)
        self.current_table_index = None
        self.current_table_keys = []
        self.user_data = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.draw.pressed.connect(self.select_color)

    def select_color(self):
        colors = []
        for layout_item in layout_widgets(self.ui.colors):
            widget = layout_item.widget()
            if widget.isChecked():
                colors.append(widget.text())
        self.ui.statusbar.showMessage("".join(colors))

def layout_widgets(layout):
    return (layout.itemAt(i) for i in range(layout.count()))