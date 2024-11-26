import sys
from PyQt6.QtWidgets import QApplication
from view.currency_view import CurrencyConverterWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CurrencyConverterWindow()
    window.show()
    sys.exit(app.exec())
