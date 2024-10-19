import json
import os.path
import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ScanWindow import ScanWindow
from SettingsWindow import SettingsWindow

APP_NAME = 'Clamav Interface'
VERSION = 'v0.1'

class ClamInterface(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ## setupUI
        self.setWindowTitle(f"{APP_NAME} - {VERSION}")
        self.resize(800, 600)

        # main_layout
        self.main_layout = QVBoxLayout()

        # function_bar
        self.function_bar = QHBoxLayout()

        # 扫描按钮
        self.scan_btn = QPushButton()
        self.scan_btn.setIcon(QIcon('./icons/scan.svg'))
        self.scan_btn.setIconSize(QSize(36, 36))
        self.scan_btn.setToolTip('Scan for virus')
        self.scan_btn.setFixedSize(QSize(64, 64))
        self.function_bar.addWidget(self.scan_btn)

        # 更新病毒库按钮
        self.update_btn = QPushButton()
        self.update_btn.setIcon(QIcon('./icons/update.svg'))
        self.update_btn.setIconSize(QSize(36, 36))
        self.update_btn.setToolTip('Update virus database')
        self.update_btn.setFixedSize(QSize(64, 64))
        self.function_bar.addWidget(self.update_btn)

        # 清除输出按钮
        self.clear_btn = QPushButton()
        self.clear_btn.setIcon(QIcon('./icons/clear.svg'))
        self.clear_btn.setIconSize(QSize(36, 36))
        self.clear_btn.setToolTip('Clear output message')
        self.clear_btn.setFixedSize(QSize(64, 64))
        self.function_bar.addWidget(self.clear_btn)

        # 菜单功能分割线
        hline = QFrame()
        hline.setFrameShape(QFrame.VLine)
        hline.setFrameShadow(QFrame.Sunken)
        self.function_bar.addWidget(hline)

        # 设置
        self.setting_btn = QPushButton()
        self.setting_btn.setIcon(QIcon('./icons/settings.svg'))
        self.setting_btn.setIconSize(QSize(36, 36))
        self.setting_btn.setToolTip('Settings')
        self.setting_btn.setFixedSize(QSize(64, 64))
        self.function_bar.addWidget(self.setting_btn)

        # 检查可用性
        self.check_btn = QPushButton()
        self.check_btn.setIcon(QIcon('./icons/check.svg'))
        self.check_btn.setIconSize(QSize(36, 36))
        self.check_btn.setToolTip('Check availability')
        self.check_btn.setFixedSize(QSize(64, 64))
        self.function_bar.addWidget(self.check_btn)

        self.function_bar.addStretch()  # end function bar

        self.main_layout.addLayout(self.function_bar)

        # 内容反馈区域
        self.content_display = QTextBrowser(self)
        self.content_display.setMinimumSize(QSize(800,600))
        self.main_layout.addWidget(self.content_display)


        # self.main_layout.addStretch()   # end main_layout
        self.setLayout(self.main_layout)

        ## end setup UI
        ## bind action
        self.bind_action()

        ## running state variables
        self.info_text = ""     # shown in self.context_display
        # global config: should be like:
        self.config = {
            'scan_config': {
                'folder_path': '',
                'generate_log_file': True,
                'customized_params:': '',
            }
        }
        with open('./config.json', 'r') as f:
            self.config["global_settings"] = json.load(f)


    def bind_action(self):
        self.update_btn.clicked.connect(self.update_virus_database)
        self.clear_btn.clicked.connect(self.clear_output)
        self.setting_btn.clicked.connect(self.edit_settings)
        self.scan_btn.clicked.connect(self.begin_scan)
        self.check_btn.clicked.connect(self.check_availability)



    # action functions below
    def begin_scan(self):
        scan_window = ScanWindow(parent=self)

        if scan_window.exec_() != QDialog.Accepted:
            return

        self.scan_process = QProcess()
        self.scan_process.readyReadStandardOutput.connect(lambda: self.display_info(
            bytes(self.scan_process.readAllStandardOutput()).decode('utf-8')
        ))

        # construct commands
        args = []

        args.append("-r")
        args.append(self.config['scan_config']['folder_path'])
        start_msg = "[ClamAV Interface] Ready to scan folder {} , this may take a while...\n".format(
            self.config['scan_config']['folder_path']
        )
        finished_msg = "[ClamAV Interface] Finished scanning!\n"

        if(self.config['scan_config']['generate_log_file']):
            log_file = "{}/{}.log".format(
                self.config['scan_config']['folder_path'],
                time.time()
            )
            args.append("-l")
            args.append(log_file)
            start_msg += "[ClamAV Interface] Your log file will be placed at {}.\n".format(log_file)
            finished_msg += "[ClamAV Interface] Your log file is placed at {}.\n".format(log_file)

        # customized params
        if(self.config['scan_config']['customized_params']) != '':
            param_list = self.config['scan_config']['customized_params'].split()
            for param in param_list:
                args.append(param)

        # bind action and start
        self.scan_process.started.connect(lambda: self.display_info(start_msg))
        self.scan_process.finished.connect(lambda: self.display_info(finished_msg, partition=True))
        self.scan_process.start(
            "{}/clamscan".format(self.config['global_settings']['clamav_path']),
            args
        )


    def update_virus_database(self):
        self.update_process = QProcess()
        self.update_process.readyReadStandardOutput.connect(lambda: self.display_info(
            bytes(self.update_process.readAllStandardOutput()).decode('utf-8')
        ))
        self.update_process.started.connect(lambda: self.display_info(
            "[ClamAv Interface] Updating your database, info will be shown below...\n"
        ))
        self.update_process.finished.connect(lambda: self.display_info(
            "[ClamAv Interface] Updating database finished!\n", partition=True
        ))
        self.update_process.start("{}/freshclam".format(self.config['global_settings']['clamav_path']))


    def edit_settings(self):
        settingsWindow = SettingsWindow(self)
        settingsWindow.exec_()


    def check_availability(self):
        available = False
        if os.path.exists(self.config['global_settings']['clamav_path']):
            if os.path.isfile(os.path.join(self.config['global_settings']['clamav_path'], "clamscan")):
                available = True
        if(available):
            msg = "[ClamAv Interface] ClamAv is available!\n"
        else:
            msg = "[ClamAv Interface] ClamAv is not available!\n"
        self.display_info(msg, partition=True)

    # common util functions
    def display_info(self, data, partition=False):
        self.info_text += data
        if(partition):
            self.info_text += "\n\n"
        self.content_display.setText(self.info_text)
        self.content_display.moveCursor(QTextCursor.End)

    def clear_output(self):
        self.info_text = ''
        self.content_display.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = ClamInterface()
    mainWindow.setFont(QFont('Arial', 12))
    mainWindow.show()
    app.exec_()
