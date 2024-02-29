import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.expression_field = QLineEdit()
        self.expression_field.setReadOnly(True)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        grid_layout = QGridLayout()
        row, col = 0, 0
        for button_text in buttons:
            button = QPushButton(button_text)
            button.clicked.connect(self.on_button_click)
            grid_layout.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        central_widget = QWidget()
        central_widget.setLayout(grid_layout)

        layout = QVBoxLayout()
        layout.addWidget(self.expression_field)
        layout.addWidget(central_widget)

        main_widget = QWidget()
        main_widget.setLayout(layout)

        self.setCentralWidget(main_widget)

        self.current_expression = ""

    def on_button_click(self):
        clicked_button = self.sender().text()

        if clicked_button == '=':
            try:
                result = str(eval(self.current_expression))
                self.expression_field.setText(result)
            except Exception as e:
                self.expression_field.setText("Erreur")
        else:
            self.current_expression += clicked_button
            self.expression_field.setText(self.current_expression)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    calculator = CalculatorApp()
    calculator.setWindowTitle("Calculatrice POC")

    calculator.show()

    sys.exit(app.exec())