from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QScreen
from controller.currency_controller import CurrencyConverter

class CurrencyConverterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conversor de Monedas")
        self.resize(300, 200)  # Configura un tamaño inicial para la ventana
        self.initUI()

    def initUI(self):
        # Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout()

        # Input amount
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Ingrese el monto")
        layout.addWidget(self.amount_input)

        # From currency
        self.from_currency = QComboBox()
        self.from_currency.addItems(['Soles (PEN)', 'Dólares (USD)', 'Euros (EUR)'])
        layout.addWidget(QLabel("De:"))
        layout.addWidget(self.from_currency)

        # To currency
        self.to_currency = QComboBox()
        self.to_currency.addItems(['Soles (PEN)', 'Dólares (USD)', 'Euros (EUR)'])
        layout.addWidget(QLabel("A:"))
        layout.addWidget(self.to_currency)

        # Convert button
        convert_button = QPushButton("Convertir")
        convert_button.clicked.connect(self.convert_currency)
        layout.addWidget(convert_button)

        # Result
        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.result_label)

        # Set layout
        central_widget.setLayout(layout)

    def convert_currency(self):
        try:
            amount = float(self.amount_input.text())
            from_curr = self.from_currency.currentText().split(' ')[1].strip('()')
            to_curr = self.to_currency.currentText().split(' ')[1].strip('()')
            result = CurrencyConverter.convert(amount, from_curr, to_curr)
            self.result_label.setText(f"{amount} {from_curr} = {result} {to_curr}")
        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))

    def center_window(self):
        """Centra la ventana en la pantalla."""
        available_geometry = QScreen.availableGeometry(QApplication.primaryScreen())
        x = (available_geometry.width() - self.width()) // 2
        y = (available_geometry.height() - self.height()) // 2
        self.move(x, y)
