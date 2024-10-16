import json

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setWindowTitle("Settings")
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)
        self.resize(QSize(800, 600))
        self.global_settings = parent.config['global_settings']

        ## setup UI
        main_layout = QVBoxLayout()

        ## ClamAv path
        clamav_path_layout = QHBoxLayout()
        clamav_path_label = QLabel()
        clamav_path_label.setText("ClamAV path: ")
        clamav_path_label.setFont(QFont('Arial', 12))
        clamav_path_layout.addWidget(clamav_path_label)

        self.clamav_path_edit_line = QLineEdit()
        self.clamav_path_edit_line.setFont(QFont('Arial', 12))
        self.clamav_path_edit_line.setReadOnly(True)
        self.clamav_path_edit_line.setText(self.global_settings['clamav_path'])
        clamav_path_layout.addWidget(self.clamav_path_edit_line)

        self.clamav_path_choose_folder_btn = QPushButton()
        self.clamav_path_choose_folder_btn.setText("Choose folder")
        self.clamav_path_choose_folder_btn.setFont(QFont('Arial', 10))
        clamav_path_layout.addWidget(self.clamav_path_choose_folder_btn)

        main_layout.addLayout(clamav_path_layout)
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

        ## bind action
        self.bind_action()

    def bind_action(self):
        self.clamav_path_choose_folder_btn.clicked.connect(self.choose_clamav_path)
        self.comfirm_btn.clicked.connect(self.update_config)


    def choose_clamav_path(self):
        clamav_path = QFileDialog.getExistingDirectory(self, "Select ClamAV path")
        self.global_settings['clamav_path'] = clamav_path
        self.clamav_path_edit_line.setText(clamav_path)

    def update_config(self):
        reply = QMessageBox.information(self, "update settings", "Sure to update settings?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if(reply == QMessageBox.No):
            return
        self.parent.config['global_settings'] = self.global_settings
        with open('./config.json', 'w') as f:
            json.dump(self.global_settings, f)
        self.accept()
