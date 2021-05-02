from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QMessageBox
from PyQt5.uic import loadUi
import os
import subprocess
import sys


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)

    def loginfunction(self):
        msg = QMessageBox()  # mesaj kutusu oluşturmak için
        py_filepath = 'Turkish_Dropdown.py'  # dosya konumunu burada veriyoruz
        email = self.email.text()  #
        password = self.password.text()  #

        if email == "emre":  # eğer kullanıcı emre ise Otoyol seçim sayfasını açıyor
            msg.setText('Sistem Açılıyor Lütfen Bekleyiniz.....')
            msg.exec_()
            print("Başarı ile Giriş Yaptınız Kullanıcı Adınız: ", email, "Ve Şifreniz:", password)

            args = '"%s" "%s" "%s"' % (sys.executable,  # command
                                       py_filepath,  # argv[0]
                                       os.path.basename(py_filepath))  # argv[1]

            proc = subprocess.run(args)
            sys.exit(app.exec_())  # kapatama kodu
            quit(app.exec_)

        else:
            msg.setText('Yanlış şifre Veya Kullanıcı Adı Lütfen Tekrar Deneyiniz')
            msg.exec_()

    def gotocreate(self):
        createacc = CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc, self).__init__()
        loadUi("createacc.ui", self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)

    def createaccfunction(self):
        msg = QMessageBox()
        email = self.email.text()
        if email == ""  :
            msg = QMessageBox()  # mesaj kutusu oluşturmak için
            msg.setText('Kullanıcı Adı Kısmı boş lütfen tekrar deneyiniz')
            msg.exec_()
        else:
            if self.password.text() == self.confirmpass.text():
                password = self.password.text()
                print("Başarı ile hesabınız oluşturuldu Kullanıcı Adınız : ", email, "Ve Şifreniz: ", password)
                msg.setText('Başarı ile hesabınız oluşturuldu')
                msg.exec_()
                login = Login()
                widget.addWidget(login)
                widget.setCurrentIndex(widget.currentIndex() + 1)
            else:
                print("Şifreleriniz Eşleşmiyor Lütfen Tekrar Deneyiniz.")
                msg.setText('Şifreleriniz Eşleşmiyor Lütfen Tekrar Deneyiniz')
                msg.exec_()

app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
app.exec_()
