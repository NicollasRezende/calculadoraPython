from PySide6.QtWidgets import (QMainWindow, QVBoxLayout, QWidget, QMessageBox)


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        # Configurando o layout basico
        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)

        self.setWindowTitle('Calculadora')

    # Ultima coisa a ser feita
    def ajustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.v_layout.addWidget(widget)

    def makeMsgBox(self):
        return QMessageBox(self)
