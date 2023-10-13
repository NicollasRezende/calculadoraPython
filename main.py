import sys

from display import Display
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH
from info import Info
from qt_material import apply_stylesheet
from buttons import ButtonsGrid

extra = {
    # font
    'font_family': 'Roboto',
}

if __name__ == '__main__':
    # cria app
    app = QApplication(sys.argv)
    window = MainWindow()

    # cria icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    info = Info('Sua Conta')
    window.addWidgetToVLayout(info)

    # cria display
    display = Display()
    window.addWidgetToVLayout(display)

    # ButtonGrid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.v_layout.addLayout(buttonsGrid)

    # Buttons

    # executa tudo
    window.ajustFixedSize()
    apply_stylesheet(app, theme='dark_pink.xml', extra=extra)
    window.show()
    app.exec()
