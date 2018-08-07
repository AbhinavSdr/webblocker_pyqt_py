from PyQt5.QtWidgets import QPushButton, QLabel, QVBoxLayout, QApplication, QWidget, QLineEdit, QHBoxLayout, QMessageBox
import sys
import os
import shutil


class Blocker():

    def __init__(self):
        self.host_path = ("H:\\PythonTester\\hosts")

    def block(self, website):
        redirect = "127.0.0.1"
        if '.' in website:
            with open("H:\\PythonTester\\hosts", "r+") as f:
                content = f.read()
                if website in content:
                    print('Website already added')
                else:
                    f.write(redirect + ' ' + website + '\n')
                    print('Website added to host file')
        else:
            print('error')
            #pass

    def url_del(self, website):
        with open(self.host_path, "r+") as f:
            content = f.readlines()
            f.seek(0)
            for line in content:
                if website not in line:
                    f.write(line)
            f.truncate()
            print('URL Removed')

    def backup(self):
        path = self.host_path
        to = os.getcwd()
        shutil.copy(path, to)
        print('Backup Complete')

class Blocker_ui(QWidget):

    def __init__(self):
        super().__init__()

        self.core = Blocker()
        self.init_ui()

    def init_ui(self):
        self.l1 = QLabel('Enter Website: ')
        self.le = QLineEdit()
        self.b1 = QPushButton('Add Website')
        self.b2 = QPushButton('Remove Website')
        self.b3 = QPushButton('Backup')

        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(self.l1)
        hbox_1.addWidget(self.le)

        hbox_2 = QHBoxLayout()
        hbox_2.addWidget(self.b1)
        hbox_2.addWidget(self.b2)
        hbox_2.addWidget(self.b3)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)

        self.setLayout(vbox)

        self.b1.clicked.connect(lambda: self.b1_click())
        self.b2.clicked.connect(lambda: self.b2_click())
        self.b3.clicked.connect(lambda: self.b3_click())

        self.setWindowTitle('Website Blocker')
        self.show()

    def b1_click(self):
        self.core.block(self.le.text())
        QMessageBox.about(self, "Website Blocker", "Website added to hosts file")

    def b2_click(self):
        self.core.url_del(self.le.text())
        QMessageBox.about(self, "Website Blocker", "Website removed from hosts file")

    def b3_click(self):
        self.core.backup()
        QMessageBox.about(self, "Website Blocker", "Hosts file backed up")


def main():
    app = QApplication(sys.argv)
    win_1 = Blocker_ui()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
