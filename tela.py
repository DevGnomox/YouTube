from PyQt6 import QtCore, QtWidgets
import getpass
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QFont
import logging


class Ui_Dialog(object):
    def setupUi(self, Dialog):

        self.log = logging.getLogger(__name__)
        self.log.debug("Tela iniciada")
        
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(450, 500)
        Dialog.setMinimumSize(QtCore.QSize(450, 500))
        Dialog.setMaximumSize(QtCore.QSize(450, 500))
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 450, 500))
        self.tabWidget.setMinimumSize(QtCore.QSize(450, 500))
        self.tabWidget.setMaximumSize(QtCore.QSize(450, 500))
        self.tabWidget.setIconSize(QtCore.QSize(17, 17))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(20, 190, 141, 20))
        self.checkBox.setObjectName("checkBox")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.tab)
        self.buttonBox.setGeometry(QtCore.QRect(260, 430, 164, 32))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(10, 440, 245, 16))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setGeometry(QtCore.QRect(10, 260, 421, 161))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 419, 159))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 419, 159))
        self.listWidget.setObjectName("listWidget")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        font = QFont()
        font.setPointSize(16)
        self.label_yt_text2 = QtWidgets.QLabel(self.tab)
        self.label_yt_text2.setGeometry(QtCore.QRect(200, -40, 225, 111))
        self.label_yt_text2.setObjectName("label_yt_text")
        self.label_yt_text2.setFont(font)


        self.label_yt2 = QtWidgets.QLabel(self.tab)
        self.label_yt2.setGeometry(QtCore.QRect(60, -10, 311, 155))
        self.label_yt2.setObjectName("label_yt")

        self.comboBox_music = QtWidgets.QComboBox(self.tab)
        self.comboBox_music.setGeometry(QtCore.QRect(173, 130, 251, 26))
        self.comboBox_music.setObjectName("comboBox_music")
        self.comboBox_music.addItem("")
        self.comboBox_music.addItem("")
        self.comboBox_music.addItem("")
        self.comboBox_music.addItem("")


        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(20, 160, 401, 21))
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 240, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 111, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 190, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(150, 230, 271, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(90, 230, 60, 20))
        self.label_8.setObjectName("label_8")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")


        font = QFont()
        font.setPointSize(16)
        self.label_yt_text = QtWidgets.QLabel(self.tab_2)
        self.label_yt_text.setGeometry(QtCore.QRect(200, -40, 225, 111))
        self.label_yt_text.setObjectName("label_yt_text")
        self.label_yt_text.setFont(font)

        
        self.label_yt = QtWidgets.QLabel(self.tab_2)
        self.label_yt.setGeometry(QtCore.QRect(90, 35, 251, 91))
        self.label_yt.setObjectName("label_yt")

        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 111, 16))
        self.label_3.setObjectName("label_3")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 190, 141, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 260, 421, 161))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 419, 159))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")

        self.listWidget_2 = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        self.listWidget_2.setGeometry(QtCore.QRect(0, 0, 419, 159))
        self.listWidget_2.setObjectName("listWidget_2")

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(10, 240, 60, 16))
        self.label_4.setObjectName("label_4")
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(self.tab_2)
        self.buttonBox_2.setGeometry(QtCore.QRect(260, 430, 164, 32))
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox_2.setObjectName("buttonBox_2")
        self.progressBar_2 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_2.setGeometry(QtCore.QRect(10, 440, 245, 16))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(310, 190, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(150, 230, 271, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(90, 230, 60, 20))
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 160, 401, 21))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")

        font = QFont()
        font.setPointSize(20)
        self.label_termos = QtWidgets.QLabel(self.tab_3)
        self.label_termos.setGeometry(QtCore.QRect(140, -30, 225, 111))
        self.label_termos.setObjectName("label_yt_text")
        self.label_termos.setFont(font)

        self.scrollArea_3 = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea_3.setGeometry(QtCore.QRect(10, 50, 421, 371))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 421, 371))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")

        self.listWidget_3 = QtWidgets.QListWidget(self.scrollAreaWidgetContents_3)
        self.listWidget_3.setGeometry(QtCore.QRect(0, 0, 420, 370))
        self.listWidget_3.setObjectName("listWidget_3")

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)


        self.buttonBox_3 = QtWidgets.QDialogButtonBox(self.tab_3)
        self.buttonBox_3.setGeometry(QtCore.QRect(260, 430, 164, 32))
        self.buttonBox_3.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox_3.setObjectName("buttonBox_3")

        self.download_button = QPushButton("Baixar Termos de Serviço", self.tab_3)
        self.download_button.setGeometry(5, 430, 200, 32)
        self.download_button.clicked.connect(self.download_terms_of_service)



        self.tabWidget.addTab(self.tab_3, "")



        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")

        font = QFont()
        font.setPointSize(20)
        self.label_config = QtWidgets.QLabel(self.tab_4)
        self.label_config.setGeometry(QtCore.QRect(140, -30, 225, 111))
        self.label_config.setObjectName("label_config")
        self.label_config.setFont(font)

        self.groupBox = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 120, 80))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName("groupBox")

        self.radioButton_tema = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_tema.setGeometry(QtCore.QRect(10, 30, 100, 20))
        self.radioButton_tema.setObjectName("radioButton_tema")

        self.radioButton_tema2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_tema2.setGeometry(QtCore.QRect(10, 50, 100, 20))
        self.radioButton_tema2.setObjectName("radioButton_tema2")

        self.buttonBox_4 = QtWidgets.QDialogButtonBox(self.tab_4)
        self.buttonBox_4.setGeometry(QtCore.QRect(260, 430, 164, 32))
        self.buttonBox_4.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox_4.setObjectName("buttonBox_4")

        self.checkBox_4 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_4.setGeometry(QtCore.QRect(150, 100, 211, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_4.setChecked(True)

        self.tabWidget.addTab(self.tab_4, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):

        usuario = getpass.getuser()
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Gnomox"))
        self.checkBox.setText(_translate("Dialog", "Termos de Serviço"))
        self.label.setText(_translate("Dialog", "Log"))
        self.label_2.setText(_translate("Dialog", "Link do YouTube"))
        self.pushButton_2.setText(_translate("Dialog", "Salvar em..."))
        self.label_7.setText(_translate("Dialog", f"/Users/{usuario}/Desktop"))
        self.label_5.setText(_translate("Dialog", f"/Users/{usuario}/Desktop"))
        self.label_yt_text.setText(_translate("Dialog", ""))
        self.label_yt_text2.setText(_translate("Dialog", ""))
        self.label_8.setText(_translate("Dialog", "Destino:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Musica"))
        self.label_3.setText(_translate("Dialog", "Link do YouTube"))
        self.checkBox_2.setText(_translate("Dialog", "Termos de Serviço"))
        self.checkBox_4.setText(_translate("Dialog", "Notificações ativadas"))
        self.label_4.setText(_translate("Dialog", "Log"))
        self.pushButton.setText(_translate("Dialog", "Salvar em..."))
        self.label_6.setText(_translate("Dialog", "Destino:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Video"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Termos"))
        self.label_termos.setText(_translate("Dialog", "TERMOS DE USO"))
        self.comboBox_music.setItemText(0, _translate("Dialog", "Qualidade Padrão (128 kbps)"))
        self.comboBox_music.setItemText(1, _translate("Dialog", "Qualidade Media (192 kbps)"))
        self.comboBox_music.setItemText(2, _translate("Dialog", "Alta Qualidade (256 kbps)"))
        self.comboBox_music.setItemText(3, _translate("Dialog", "Qualidade Máxima (320 kbps)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Config"))
        self.groupBox.setTitle(_translate("Dialog", "Tema"))
        self.radioButton_tema.setText(_translate("Dialog", "Escuro"))
        self.radioButton_tema2.setText(_translate("Dialog", "Claro"))
        self.label_config.setText(_translate("Dialog", "Configurações"))

