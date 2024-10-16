from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)
        self.setFixedSize(QSize(400, 300))

        ## setup UI
        main_layout = QVBoxLayout()

        main_layout.addStretch()

        ## confirm button bar
        op_btn_layout = QHBoxLayout()
        op_btn_layout.addStretch()

        self.comfirm_btn = QPushButton("Comfirm")
        self.comfirm_btn.setFixedSize(QSize(100, 50))
        op_btn_layout.addWidget(self.comfirm_btn)

        self.cancel_btn = QPushButton("Cancel")
        self.cancel_btn.setFixedSize(QSize(100, 50))
        self.cancel_btn.clicked.connect(self.reject)
        op_btn_layout.addWidget(self.cancel_btn)

        main_layout.addLayout(op_btn_layout)
        self.setLayout(main_layout)