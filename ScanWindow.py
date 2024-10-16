import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ScanWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle("Settings before scan")
        self.resize(QSize(800, 400))
        self.parent = parent

        ## setup UI
        main_layout = QVBoxLayout()

        ## choose Directory
        directory_layout = QHBoxLayout()

        label = QLabel("Directory:")
        label.setFont(QFont("Arial", 12))
        directory_layout.addWidget(label)

        choose_directory_btn = QPushButton("Choose Directory")
        choose_directory_btn.setFont(QFont("Arial", 10))
        choose_directory_btn.setFixedSize(QSize(180, 40))
        choose_directory_btn.clicked.connect(self.choose_folder)
        directory_layout.addWidget(choose_directory_btn)

        self.line_edit = QLineEdit()
        self.line_edit.setReadOnly(True)
        self.line_edit.setFont(QFont("Arial", 10))
        self.line_edit.setFixedSize(QSize(400, 40))
        directory_layout.addWidget(self.line_edit)

        directory_layout.addStretch()
        main_layout.addLayout(directory_layout)

        main_layout.addStretch()

        ## Start Btn
        start_btn_layout = QHBoxLayout()

        start_btn = QPushButton("Start")
        start_btn.setFont(QFont("Arial", 12))
        start_btn.setFixedSize(QSize(150, 60))
        start_btn.clicked.connect(self.start_scan)
        start_btn_layout.addWidget(start_btn)

        main_layout.addLayout(start_btn_layout)

        self.setLayout(main_layout)


    def start_scan(self):
        if(self.parent.config['scan_config']['folder_path'] != ''):
            self.accept()
            return
        # No folder is chosen
        QMessageBox.warning(self, "Warning", "Scan folder should not be empty",QMessageBox.Ok, QMessageBox.Ok)




    def closeEvent(self, e):
        self.reject()

    def choose_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        self.parent.config['scan_config']['folder_path'] = folder_path
        self.line_edit.setText(folder_path)