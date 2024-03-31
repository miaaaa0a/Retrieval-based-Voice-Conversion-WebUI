# Form implementation generated from reading ui file '.\rvc ui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(622, 729)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(622, 729))
        MainWindow.setMaximumSize(QtCore.QSize(622, 729))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 621, 681))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.PreventContextMenu)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 591, 171))
        self.groupBox.setObjectName("groupBox")
        self.inferAudio = QtWidgets.QLineEdit(parent=self.groupBox)
        self.inferAudio.setGeometry(QtCore.QRect(10, 40, 531, 20))
        self.inferAudio.setObjectName("inferAudio")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 571, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 571, 16))
        self.label_2.setObjectName("label_2")
        self.modelInfer = QtWidgets.QComboBox(parent=self.groupBox)
        self.modelInfer.setGeometry(QtCore.QRect(10, 90, 571, 22))
        self.modelInfer.setObjectName("modelInfer")
        self.indexRateSlider = QtWidgets.QSlider(parent=self.groupBox)
        self.indexRateSlider.setGeometry(QtCore.QRect(10, 140, 511, 22))
        self.indexRateSlider.setMaximum(100)
        self.indexRateSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.indexRateSlider.setObjectName("indexRateSlider")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 571, 16))
        self.label_3.setObjectName("label_3")
        self.inferAudioBtn = QtWidgets.QToolButton(parent=self.groupBox)
        self.inferAudioBtn.setGeometry(QtCore.QRect(550, 40, 31, 19))
        self.inferAudioBtn.setObjectName("inferAudioBtn")
        self.indexRatioVal = QtWidgets.QLineEdit(parent=self.groupBox)
        self.indexRatioVal.setGeometry(QtCore.QRect(530, 140, 51, 20))
        self.indexRatioVal.setReadOnly(True)
        self.indexRatioVal.setObjectName("indexRatioVal")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 190, 601, 341))
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBox = QtWidgets.QCheckBox(parent=self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(10, 20, 311, 17))
        self.checkBox.setObjectName("checkBox")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 311, 16))
        self.label_4.setObjectName("label_4")
        self.f0Choice = QtWidgets.QComboBox(parent=self.groupBox_2)
        self.f0Choice.setGeometry(QtCore.QRect(10, 110, 301, 22))
        self.f0Choice.setObjectName("f0Choice")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 311, 16))
        self.label_5.setObjectName("label_5")
        self.hybridF0Label = QtWidgets.QLabel(parent=self.groupBox_2)
        self.hybridF0Label.setEnabled(True)
        self.hybridF0Label.setGeometry(QtCore.QRect(330, 20, 251, 16))
        self.hybridF0Label.setObjectName("hybridF0Label")
        self.hybridF0Choices = QtWidgets.QListWidget(parent=self.groupBox_2)
        self.hybridF0Choices.setEnabled(True)
        self.hybridF0Choices.setGeometry(QtCore.QRect(330, 40, 256, 91))
        self.hybridF0Choices.setAlternatingRowColors(True)
        self.hybridF0Choices.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        self.hybridF0Choices.setObjectName("hybridF0Choices")
        self.minFreqSlider = QtWidgets.QSlider(parent=self.groupBox_2)
        self.minFreqSlider.setGeometry(QtCore.QRect(10, 160, 511, 22))
        self.minFreqSlider.setMaximum(16000)
        self.minFreqSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.minFreqSlider.setObjectName("minFreqSlider")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 140, 571, 16))
        self.label_7.setObjectName("label_7")
        self.minFreqSpinBox = QtWidgets.QSpinBox(parent=self.groupBox_2)
        self.minFreqSpinBox.setGeometry(QtCore.QRect(531, 160, 51, 22))
        self.minFreqSpinBox.setMaximum(16000)
        self.minFreqSpinBox.setObjectName("minFreqSpinBox")
        self.maxFreqSpinBox = QtWidgets.QSpinBox(parent=self.groupBox_2)
        self.maxFreqSpinBox.setGeometry(QtCore.QRect(531, 210, 51, 22))
        self.maxFreqSpinBox.setMaximum(16000)
        self.maxFreqSpinBox.setObjectName("maxFreqSpinBox")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(10, 190, 571, 16))
        self.label_8.setObjectName("label_8")
        self.maxFreqSlider = QtWidgets.QSlider(parent=self.groupBox_2)
        self.maxFreqSlider.setGeometry(QtCore.QRect(10, 210, 511, 22))
        self.maxFreqSlider.setMaximum(16000)
        self.maxFreqSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.maxFreqSlider.setObjectName("maxFreqSlider")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(10, 240, 571, 16))
        self.label_9.setObjectName("label_9")
        self.protectSlider = QtWidgets.QSlider(parent=self.groupBox_2)
        self.protectSlider.setGeometry(QtCore.QRect(10, 260, 511, 22))
        self.protectSlider.setMaximum(100)
        self.protectSlider.setSingleStep(1)
        self.protectSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.protectSlider.setObjectName("protectSlider")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(10, 290, 571, 16))
        self.label_10.setObjectName("label_10")
        self.volRatioSlider = QtWidgets.QSlider(parent=self.groupBox_2)
        self.volRatioSlider.setGeometry(QtCore.QRect(10, 310, 511, 22))
        self.volRatioSlider.setMaximum(100)
        self.volRatioSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.volRatioSlider.setObjectName("volRatioSlider")
        self.indexInfer = QtWidgets.QComboBox(parent=self.groupBox_2)
        self.indexInfer.setGeometry(QtCore.QRect(10, 60, 301, 22))
        self.indexInfer.setObjectName("indexInfer")
        self.protectVal = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.protectVal.setGeometry(QtCore.QRect(530, 260, 51, 20))
        self.protectVal.setReadOnly(True)
        self.protectVal.setObjectName("protectVal")
        self.volRatioVal = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.volRatioVal.setGeometry(QtCore.QRect(530, 310, 51, 20))
        self.volRatioVal.setReadOnly(True)
        self.volRatioVal.setObjectName("volRatioVal")
        self.inferBtn = QtWidgets.QPushButton(parent=self.tab)
        self.inferBtn.setGeometry(QtCore.QRect(10, 542, 601, 61))
        self.inferBtn.setObjectName("inferBtn")
        self.progressBar = QtWidgets.QProgressBar(parent=self.tab)
        self.progressBar.setGeometry(QtCore.QRect(10, 610, 601, 41))
        self.progressBar.setProperty("value", 33)
        self.progressBar.setTextVisible(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.Direction.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.label_11 = QtWidgets.QLabel(parent=self.tab)
        self.label_11.setGeometry(QtCore.QRect(10, 610, 601, 41))
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 601, 151))
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.groupBox_3)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 20, 281, 121))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(10, 20, 261, 16))
        self.label_12.setObjectName("label_12")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 40, 261, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_13 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_13.setGeometry(QtCore.QRect(10, 70, 261, 16))
        self.label_13.setObjectName("label_13")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 90, 221, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.toolButton = QtWidgets.QToolButton(parent=self.groupBox_4)
        self.toolButton.setGeometry(QtCore.QRect(244, 90, 31, 20))
        self.toolButton.setObjectName("toolButton")
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.groupBox_3)
        self.groupBox_5.setGeometry(QtCore.QRect(310, 20, 281, 121))
        self.groupBox_5.setObjectName("groupBox_5")
        self.checkBox_2 = QtWidgets.QCheckBox(parent=self.groupBox_5)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 20, 261, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.label_15 = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label_15.setGeometry(QtCore.QRect(10, 40, 261, 16))
        self.label_15.setObjectName("label_15")
        self.radioButton_3 = QtWidgets.QRadioButton(parent=self.groupBox_5)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 60, 261, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(parent=self.groupBox_5)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 80, 261, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(parent=self.groupBox_5)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 100, 261, 17))
        self.radioButton_5.setObjectName("radioButton_5")
        self.groupBox_6 = QtWidgets.QGroupBox(parent=self.tab_2)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 170, 601, 311))
        self.groupBox_6.setObjectName("groupBox_6")
        self.pushButton = QtWidgets.QPushButton(parent=self.groupBox_6)
        self.pushButton.setGeometry(QtCore.QRect(320, 30, 271, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.groupBox_6)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 80, 271, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_17 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_17.setGeometry(QtCore.QRect(10, 20, 301, 16))
        self.label_17.setObjectName("label_17")
        self.listWidget_2 = QtWidgets.QListWidget(parent=self.groupBox_6)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 90, 301, 81))
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.label_16 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_16.setGeometry(QtCore.QRect(10, 70, 301, 16))
        self.label_16.setObjectName("label_16")
        self.comboBox_3 = QtWidgets.QComboBox(parent=self.groupBox_6)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 40, 301, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.groupBox_6)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 130, 271, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.textBrowser_2 = QtWidgets.QTextBrowser(parent=self.groupBox_6)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 200, 581, 101))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_18 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_18.setGeometry(QtCore.QRect(10, 180, 581, 16))
        self.label_18.setObjectName("label_18")
        self.groupBox_7 = QtWidgets.QGroupBox(parent=self.tab_2)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 480, 601, 161))
        self.groupBox_7.setObjectName("groupBox_7")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.groupBox_7)
        self.textBrowser.setGeometry(QtCore.QRect(10, 40, 291, 111))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.groupBox_7)
        self.pushButton_5.setGeometry(QtCore.QRect(310, 40, 281, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.groupBox_7)
        self.pushButton_6.setGeometry(QtCore.QRect(310, 72, 281, 71))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_19 = QtWidgets.QLabel(parent=self.groupBox_7)
        self.label_19.setGeometry(QtCore.QRect(10, 20, 581, 16))
        self.label_19.setObjectName("label_19")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_8 = QtWidgets.QGroupBox(parent=self.tab_3)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 140, 601, 501))
        self.groupBox_8.setObjectName("groupBox_8")
        self.groupBox_10 = QtWidgets.QGroupBox(parent=self.groupBox_8)
        self.groupBox_10.setGeometry(QtCore.QRect(10, 20, 581, 171))
        self.groupBox_10.setObjectName("groupBox_10")
        self.label_20 = QtWidgets.QLabel(parent=self.groupBox_10)
        self.label_20.setGeometry(QtCore.QRect(10, 20, 561, 16))
        self.label_20.setObjectName("label_20")
        self.toolButton_5 = QtWidgets.QToolButton(parent=self.groupBox_10)
        self.toolButton_5.setGeometry(QtCore.QRect(254, 40, 31, 20))
        self.toolButton_5.setObjectName("toolButton_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.groupBox_10)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 40, 231, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_21 = QtWidgets.QLabel(parent=self.groupBox_10)
        self.label_21.setGeometry(QtCore.QRect(300, 20, 271, 16))
        self.label_21.setObjectName("label_21")
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=self.groupBox_10)
        self.lineEdit_7.setGeometry(QtCore.QRect(300, 40, 231, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.toolButton_6 = QtWidgets.QToolButton(parent=self.groupBox_10)
        self.toolButton_6.setGeometry(QtCore.QRect(544, 40, 31, 20))
        self.toolButton_6.setObjectName("toolButton_6")
        self.label_22 = QtWidgets.QLabel(parent=self.groupBox_10)
        self.label_22.setGeometry(QtCore.QRect(10, 70, 561, 16))
        self.label_22.setObjectName("label_22")
        self.horizontalSlider_6 = QtWidgets.QSlider(parent=self.groupBox_10)
        self.horizontalSlider_6.setGeometry(QtCore.QRect(10, 90, 511, 22))
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_6.setObjectName("horizontalSlider_6")
        self.spinBox_6 = QtWidgets.QSpinBox(parent=self.groupBox_10)
        self.spinBox_6.setGeometry(QtCore.QRect(530, 90, 42, 22))
        self.spinBox_6.setMaximum(100)
        self.spinBox_6.setObjectName("spinBox_6")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.groupBox_10)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 120, 561, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.groupBox_11 = QtWidgets.QGroupBox(parent=self.groupBox_8)
        self.groupBox_11.setGeometry(QtCore.QRect(10, 200, 581, 291))
        self.groupBox_11.setObjectName("groupBox_11")
        self.toolButton_7 = QtWidgets.QToolButton(parent=self.groupBox_11)
        self.toolButton_7.setGeometry(QtCore.QRect(544, 40, 31, 20))
        self.toolButton_7.setObjectName("toolButton_7")
        self.label_23 = QtWidgets.QLabel(parent=self.groupBox_11)
        self.label_23.setGeometry(QtCore.QRect(10, 20, 561, 16))
        self.label_23.setObjectName("label_23")
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.groupBox_11)
        self.lineEdit_8.setGeometry(QtCore.QRect(10, 40, 521, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.groupBox_11)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 70, 561, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.textBrowser_3 = QtWidgets.QTextBrowser(parent=self.groupBox_11)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 140, 561, 141))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_24 = QtWidgets.QLabel(parent=self.groupBox_11)
        self.label_24.setGeometry(QtCore.QRect(10, 120, 561, 16))
        self.label_24.setObjectName("label_24")
        self.groupBox_9 = QtWidgets.QGroupBox(parent=self.tab_3)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 10, 601, 121))
        self.groupBox_9.setObjectName("groupBox_9")
        self.label_14 = QtWidgets.QLabel(parent=self.groupBox_9)
        self.label_14.setGeometry(QtCore.QRect(10, 20, 581, 16))
        self.label_14.setObjectName("label_14")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.groupBox_9)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 40, 541, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.toolButton_4 = QtWidgets.QToolButton(parent=self.groupBox_9)
        self.toolButton_4.setGeometry(QtCore.QRect(564, 40, 31, 20))
        self.toolButton_4.setObjectName("toolButton_4")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.groupBox_9)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 70, 581, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 622, 25))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(parent=self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(parent=MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.minFreqSlider.sliderMoved['int'].connect(self.minFreqSpinBox.setValue) # type: ignore
        self.minFreqSpinBox.valueChanged['int'].connect(self.minFreqSlider.setValue) # type: ignore
        self.maxFreqSlider.sliderMoved['int'].connect(self.maxFreqSpinBox.setValue) # type: ignore
        self.maxFreqSpinBox.valueChanged['int'].connect(self.maxFreqSlider.setValue) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QT RVC Fork by miaaaa0a"))
        self.groupBox.setTitle(_translate("MainWindow", "Basic Settings"))
        self.label.setText(_translate("MainWindow", "Pick an audio for inference"))
        self.label_2.setText(_translate("MainWindow", "Pick a model for inference"))
        self.label_3.setText(_translate("MainWindow", "Index rate"))
        self.inferAudioBtn.setText(_translate("MainWindow", "..."))
        self.groupBox_2.setTitle(_translate("MainWindow", "Advanced Settings"))
        self.checkBox.setText(_translate("MainWindow", "Disable index file"))
        self.label_4.setText(_translate("MainWindow", "Pick index file manually"))
        self.label_5.setText(_translate("MainWindow", "F0 algorithm"))
        self.hybridF0Label.setText(_translate("MainWindow", "Pick algorithms for hybrid F0"))
        self.label_7.setText(_translate("MainWindow", "Minimal frequency"))
        self.label_8.setText(_translate("MainWindow", "Maximal frequency"))
        self.label_9.setText(_translate("MainWindow", "Protect voiceless consonants"))
        self.label_10.setText(_translate("MainWindow", "Input/output volume ratio"))
        self.inferBtn.setText(_translate("MainWindow", "Begin inference"))
        self.label_11.setText(_translate("MainWindow", "Processing: 1/3 window"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Inference"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Training settings"))
        self.groupBox_4.setTitle(_translate("MainWindow", "General settings"))
        self.label_12.setText(_translate("MainWindow", "Model name"))
        self.label_13.setText(_translate("MainWindow", "Dataset path"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.groupBox_5.setTitle(_translate("MainWindow", "Model Architecture"))
        self.checkBox_2.setText(_translate("MainWindow", "Will the model have pitch guidance?"))
        self.label_15.setText(_translate("MainWindow", "Pretrained model"))
        self.radioButton_3.setText(_translate("MainWindow", "32k"))
        self.radioButton_4.setText(_translate("MainWindow", "40k"))
        self.radioButton_5.setText(_translate("MainWindow", "48k"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Dataset preprocessing"))
        self.pushButton.setText(_translate("MainWindow", "Chop up dataset"))
        self.pushButton_2.setText(_translate("MainWindow", "Extract speech features"))
        self.label_17.setText(_translate("MainWindow", "F0 algorithm"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MainWindow", "harvest"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("MainWindow", "crepe"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("MainWindow", "mangio-crepe"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("MainWindow", "rmvpe"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.label_16.setText(_translate("MainWindow", "Pick algorithms for hybrid F0"))
        self.pushButton_4.setText(_translate("MainWindow", "Extract F0 pitch curves"))
        self.label_18.setText(_translate("MainWindow", "Output"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Training process"))
        self.pushButton_5.setText(_translate("MainWindow", "Train index"))
        self.pushButton_6.setText(_translate("MainWindow", "Start training"))
        self.label_19.setText(_translate("MainWindow", "Output"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Training"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Model shenanigans"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Merge two models"))
        self.label_20.setText(_translate("MainWindow", "Path to model A"))
        self.toolButton_5.setText(_translate("MainWindow", "..."))
        self.label_21.setText(_translate("MainWindow", "Path to model B"))
        self.toolButton_6.setText(_translate("MainWindow", "..."))
        self.label_22.setText(_translate("MainWindow", "Model A/B ratio"))
        self.pushButton_8.setText(_translate("MainWindow", "Merge"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Read model information"))
        self.toolButton_7.setText(_translate("MainWindow", "..."))
        self.label_23.setText(_translate("MainWindow", "Path to model"))
        self.pushButton_9.setText(_translate("MainWindow", "Read"))
        self.label_24.setText(_translate("MainWindow", "Output"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Export to ONNX"))
        self.label_14.setText(_translate("MainWindow", "Path to model"))
        self.toolButton_4.setText(_translate("MainWindow", "..."))
        self.pushButton_7.setText(_translate("MainWindow", "Export"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Miscellanious"))
        self.menuAbout.setTitle(_translate("MainWindow", "File"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
