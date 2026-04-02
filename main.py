import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("My Sampler App")

button = QPushButton("파일 불러오기")

layout = QVBoxLayout()
layout.addWidget(button)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())