from PyQt5.QtWidgets import (
    QWidget, QPushButton, QLabel, QVBoxLayout,
    QFileDialog, QMessageBox
)

class SamplerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.current_file = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Rexim Elpmas")
        self.setGeometry(300, 200, 500, 250)

        self.title_label = QLabel("Mini Sampler App")
        self.file_label = QLabel("불러온 파일 없음")

        self.load_button = QPushButton("파일 불러오기")
        self.cut_button = QPushButton("자르기")
        self.save_button = QPushButton("저장하기")

        self.load_button.clicked.connect(self.load_file)
        self.cut_button.clicked.connect(self.cut_audio)
        self.save_button.clicked.connect(self.save_audio)

        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.file_label)
        layout.addWidget(self.load_button)
        layout.addWidget(self.cut_button)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "오디오 파일 선택",
            "",
            "Audio Files (*.mp3 *.wav *.flac)"
        )

        if file_path:
            self.current_file = file_path
            self.file_label.setText(f"선택된 파일: {file_path}")

    def cut_audio(self):
        if not self.current_file:
            QMessageBox.warning(self, "경고", "먼저 파일을 불러오세요.")
            return

        QMessageBox.information(self, "안내", "자르기 기능은 다음 단계에서 구현합니다.")

    def save_audio(self):
        if not self.current_file:
            QMessageBox.warning(self, "경고", "먼저 파일을 불러오세요.")
            return

        QMessageBox.information(self, "안내", "저장 기능은 다음 단계에서 구현합니다.")