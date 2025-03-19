import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout, QHBoxLayout

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("계산기")
        self.setGeometry(300, 300, 400, 500)

        # 레이아웃 설정
        self.layout = QVBoxLayout()

        # 수식을 입력할 공간
        self.input_display = QLineEdit(self)
        self.input_display.setReadOnly(True)  # 읽기 전용
        self.input_display.setStyleSheet("background-color: #f0f0f0; font-size: 18px;")  # 스타일 설정
        self.layout.addWidget(self.input_display)

        # 결과를 표시할 공간
        self.result_display = QLineEdit(self)
        self.result_display.setReadOnly(True)  # 읽기 전용
        self.result_display.setStyleSheet("background-color: #e0e0e0; font-size: 18px;")  # 스타일 설정
        self.layout.addWidget(self.result_display)

        # 그리드 레이아웃으로 숫자와 연산 버튼 배치
        self.button_layout = QGridLayout()

        # 숫자 버튼과 연산 버튼 배열
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '=', '.', '+')
        ]

        # 버튼을 그리드에 배치
        row = 0
        for btn_row in buttons:
            col = 0
            for btn in btn_row:
                button = QPushButton(btn)
                button.clicked.connect(self.on_button_click)
                self.button_layout.addWidget(button, row, col)
                col += 1
            row += 1

        self.layout.addLayout(self.button_layout)

        # 레이아웃을 윈도우에 적용
        self.setLayout(self.layout)

    def on_button_click(self):
        sender = self.sender()
        text = sender.text()

        current_input = self.input_display.text()
        current_result = self.result_display.text()

        if text == "=":
            try:
                # 수식을 계산해서 결과 표시
                result = str(eval(current_input))
                self.result_display.setText(result)
            except Exception:
                self.result_display.setText("오류")
        else:
            # 수식 입력창에 추가
            self.input_display.setText(current_input + text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
