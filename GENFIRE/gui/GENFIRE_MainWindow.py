# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GENFIRE_MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_GENFIRE_MainWindow(object):
    def setupUi(self, GENFIRE_MainWindow):
        GENFIRE_MainWindow.setObjectName(_fromUtf8("GENFIRE_MainWindow"))
        GENFIRE_MainWindow.setEnabled(True)
        GENFIRE_MainWindow.resize(807, 876)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GENFIRE_MainWindow.sizePolicy().hasHeightForWidth())
        GENFIRE_MainWindow.setSizePolicy(sizePolicy)
        self.centralWidget = QtGui.QWidget(GENFIRE_MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout_4 = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout_4.setMargin(11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.scrollArea = QtGui.QScrollArea(self.centralWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 799, 953))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setMargin(11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setMargin(11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.nameWidget = QtGui.QWidget(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameWidget.sizePolicy().hasHeightForWidth())
        self.nameWidget.setSizePolicy(sizePolicy)
        self.nameWidget.setMinimumSize(QtCore.QSize(512, 93))
        self.nameWidget.setStyleSheet(_fromUtf8("background-image: url(:/GENFIRE.png)"))
        self.nameWidget.setObjectName(_fromUtf8("nameWidget"))
        self.horizontalLayout_3.addWidget(self.nameWidget)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setMargin(11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setMargin(11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit_pj = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_pj.setObjectName(_fromUtf8("lineEdit_pj"))
        self.gridLayout.addWidget(self.lineEdit_pj, 0, 2, 1, 1)
        self.line_4 = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout.addWidget(self.line_4, 10, 0, 1, 3)
        self.lineEdit_io = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_io.setObjectName(_fromUtf8("lineEdit_io"))
        self.gridLayout.addWidget(self.lineEdit_io, 9, 2, 1, 1)
        self.line_2 = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 5, 0, 1, 3)
        self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 12, 0, 1, 1)
        self.line = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 0, 1, 3)
        self.line_3 = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 7, 0, 1, 3)
        self.label_5 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 13, 2, 1, 1)
        self.lineEdit_results = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_results.setObjectName(_fromUtf8("lineEdit_results"))
        self.gridLayout.addWidget(self.lineEdit_results, 12, 2, 1, 1)
        self.lineEdit_angle = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_angle.setObjectName(_fromUtf8("lineEdit_angle"))
        self.gridLayout.addWidget(self.lineEdit_angle, 6, 2, 1, 1)
        self.checkBox_provide_io = QtGui.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_provide_io.setObjectName(_fromUtf8("checkBox_provide_io"))
        self.gridLayout.addWidget(self.checkBox_provide_io, 8, 0, 1, 1)
        self.btn_projections = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_projections.setObjectName(_fromUtf8("btn_projections"))
        self.gridLayout.addWidget(self.btn_projections, 0, 0, 1, 1)
        self.btn_angles = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_angles.setObjectName(_fromUtf8("btn_angles"))
        self.gridLayout.addWidget(self.btn_angles, 6, 0, 1, 1)
        self.btn_support = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_support.setObjectName(_fromUtf8("btn_support"))
        self.gridLayout.addWidget(self.btn_support, 3, 0, 1, 1)
        self.lineEdit_support = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_support.setObjectName(_fromUtf8("lineEdit_support"))
        self.gridLayout.addWidget(self.lineEdit_support, 3, 2, 1, 1)
        self.btn_io = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_io.setObjectName(_fromUtf8("btn_io"))
        self.gridLayout.addWidget(self.btn_io, 9, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout.addLayout(self.horizontalLayout, 13, 0, 1, 1)
        self.checkBox_default_support = QtGui.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_default_support.setObjectName(_fromUtf8("checkBox_default_support"))
        self.gridLayout.addWidget(self.checkBox_default_support, 2, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setMargin(11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.radioButton_on = QtGui.QRadioButton(self.groupBox)
        self.radioButton_on.setObjectName(_fromUtf8("radioButton_on"))
        self.verticalLayout.addWidget(self.radioButton_on)
        self.radioButton_off = QtGui.QRadioButton(self.groupBox)
        self.radioButton_off.setObjectName(_fromUtf8("radioButton_off"))
        self.verticalLayout.addWidget(self.radioButton_off)
        self.radioButton_extension = QtGui.QRadioButton(self.groupBox)
        self.radioButton_extension.setObjectName(_fromUtf8("radioButton_extension"))
        self.verticalLayout.addWidget(self.radioButton_extension)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setMargin(11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 4, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 1)
        self.lineEdit_numIterations = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_numIterations.sizePolicy().hasHeightForWidth())
        self.lineEdit_numIterations.setSizePolicy(sizePolicy)
        self.lineEdit_numIterations.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_numIterations.setObjectName(_fromUtf8("lineEdit_numIterations"))
        self.gridLayout_2.addWidget(self.lineEdit_numIterations, 0, 1, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setMargin(11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 5, 7, 1)
        self.lineEdit_oversamplingRatio = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_oversamplingRatio.sizePolicy().hasHeightForWidth())
        self.lineEdit_oversamplingRatio.setSizePolicy(sizePolicy)
        self.lineEdit_oversamplingRatio.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_oversamplingRatio.setObjectName(_fromUtf8("lineEdit_oversamplingRatio"))
        self.gridLayout_2.addWidget(self.lineEdit_oversamplingRatio, 4, 1, 1, 1)
        self.lineEdit_interpolationCutoffDistance = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_interpolationCutoffDistance.sizePolicy().hasHeightForWidth())
        self.lineEdit_interpolationCutoffDistance.setSizePolicy(sizePolicy)
        self.lineEdit_interpolationCutoffDistance.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_interpolationCutoffDistance.setObjectName(_fromUtf8("lineEdit_interpolationCutoffDistance"))
        self.gridLayout_2.addWidget(self.lineEdit_interpolationCutoffDistance, 6, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 6, 0, 1, 1)
        self.line_5 = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout_2.addWidget(self.line_5, 0, 3, 1, 1)
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label.setWordWrap(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 4, 4, 1, 1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setMargin(11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_6 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_5.addWidget(self.label_6)
        self.checkBox_positivity_constraint = QtGui.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_positivity_constraint.setObjectName(_fromUtf8("checkBox_positivity_constraint"))
        self.verticalLayout_5.addWidget(self.checkBox_positivity_constraint)
        self.checkBox_support_constraint = QtGui.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_support_constraint.setObjectName(_fromUtf8("checkBox_support_constraint"))
        self.verticalLayout_5.addWidget(self.checkBox_support_constraint)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 1, 3, 1, 1)
        self.label_7 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setMargin(11)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.radioButton_FFT = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_FFT.setObjectName(_fromUtf8("radioButton_FFT"))
        self.verticalLayout_7.addWidget(self.radioButton_FFT)
        self.radioButton_DFT = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_DFT.setObjectName(_fromUtf8("radioButton_DFT"))
        self.verticalLayout_7.addWidget(self.radioButton_DFT)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 1, 1, 1)
        self.line_6 = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.gridLayout_2.addWidget(self.line_6, 2, 3, 1, 1)
        self.btn_displayResults = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_displayResults.setObjectName(_fromUtf8("btn_displayResults"))
        self.gridLayout_2.addWidget(self.btn_displayResults, 6, 3, 1, 1)
        self.checkBox_rfree = QtGui.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_rfree.setObjectName(_fromUtf8("checkBox_rfree"))
        self.gridLayout_2.addWidget(self.checkBox_rfree, 4, 3, 1, 1)
        self.checkBox_resCircle = QtGui.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_resCircle.setChecked(True)
        self.checkBox_resCircle.setObjectName(_fromUtf8("checkBox_resCircle"))
        self.gridLayout_2.addWidget(self.checkBox_resCircle, 2, 0, 1, 2)
        self.checkBox_multiGridding = QtGui.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_multiGridding.setChecked(True)
        self.checkBox_multiGridding.setObjectName(_fromUtf8("checkBox_multiGridding"))
        self.gridLayout_2.addWidget(self.checkBox_multiGridding, 3, 0, 1, 2)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setMargin(11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.btn_reconstruct = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_reconstruct.sizePolicy().hasHeightForWidth())
        self.btn_reconstruct.setSizePolicy(sizePolicy)
        self.btn_reconstruct.setMinimumSize(QtCore.QSize(775, 0))
        self.btn_reconstruct.setObjectName(_fromUtf8("btn_reconstruct"))
        self.horizontalLayout_4.addWidget(self.btn_reconstruct)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setMargin(11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.log = QtGui.QTextEdit(self.scrollAreaWidgetContents_2)
        self.log.setMinimumSize(QtCore.QSize(100, 0))
        self.log.setObjectName(_fromUtf8("log"))
        self.verticalLayout_2.addWidget(self.log)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        GENFIRE_MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtGui.QToolBar(GENFIRE_MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        GENFIRE_MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(GENFIRE_MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        GENFIRE_MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtGui.QMenuBar(GENFIRE_MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 807, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuTools = QtGui.QMenu(self.menuBar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuView_Volume = QtGui.QMenu(self.menuBar)
        self.menuView_Volume.setObjectName(_fromUtf8("menuView_Volume"))
        GENFIRE_MainWindow.setMenuBar(self.menuBar)
        self.action_Create_Support = QtGui.QAction(GENFIRE_MainWindow)
        self.action_Create_Support.setObjectName(_fromUtf8("action_Create_Support"))
        self.action_Volume_Slicer = QtGui.QAction(GENFIRE_MainWindow)
        self.action_Volume_Slicer.setObjectName(_fromUtf8("action_Volume_Slicer"))
        self.action_2 = QtGui.QAction(GENFIRE_MainWindow)
        self.action_2.setObjectName(_fromUtf8("action_2"))
        self.menuTools.addAction(self.action_Create_Support)
        self.menuView_Volume.addAction(self.action_Volume_Slicer)
        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuBar.addAction(self.menuView_Volume.menuAction())

        self.retranslateUi(GENFIRE_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(GENFIRE_MainWindow)
        GENFIRE_MainWindow.setTabOrder(self.lineEdit_pj, self.lineEdit_support)
        GENFIRE_MainWindow.setTabOrder(self.lineEdit_support, self.lineEdit_angle)
        GENFIRE_MainWindow.setTabOrder(self.lineEdit_angle, self.lineEdit_io)
        GENFIRE_MainWindow.setTabOrder(self.lineEdit_io, self.lineEdit_numIterations)
        GENFIRE_MainWindow.setTabOrder(self.lineEdit_numIterations, self.lineEdit_oversamplingRatio)
        GENFIRE_MainWindow.setTabOrder(self.lineEdit_oversamplingRatio, self.lineEdit_interpolationCutoffDistance)
        GENFIRE_MainWindow.setTabOrder(self.lineEdit_interpolationCutoffDistance, self.radioButton_on)
        GENFIRE_MainWindow.setTabOrder(self.radioButton_on, self.radioButton_off)
        GENFIRE_MainWindow.setTabOrder(self.radioButton_off, self.radioButton_extension)
        GENFIRE_MainWindow.setTabOrder(self.radioButton_extension, self.btn_angles)
        GENFIRE_MainWindow.setTabOrder(self.btn_angles, self.btn_io)
        GENFIRE_MainWindow.setTabOrder(self.btn_io, self.btn_projections)
        GENFIRE_MainWindow.setTabOrder(self.btn_projections, self.btn_support)

    def retranslateUi(self, GENFIRE_MainWindow):
        GENFIRE_MainWindow.setWindowTitle(_translate("GENFIRE_MainWindow", "GENFIRE", None))
        self.label_4.setText(_translate("GENFIRE_MainWindow", "Results Filename", None))
        self.label_5.setText(_translate("GENFIRE_MainWindow", "*.mrc, *.npy, or *.mat", None))
        self.checkBox_provide_io.setText(_translate("GENFIRE_MainWindow", "Provide initial object", None))
        self.btn_projections.setText(_translate("GENFIRE_MainWindow", "Select Projection File", None))
        self.btn_angles.setText(_translate("GENFIRE_MainWindow", "Select Angle File", None))
        self.btn_support.setText(_translate("GENFIRE_MainWindow", "Select Support File", None))
        self.btn_io.setText(_translate("GENFIRE_MainWindow", "Select Inital Object File", None))
        self.checkBox_default_support.setText(_translate("GENFIRE_MainWindow", "Use default support", None))
        self.groupBox.setTitle(_translate("GENFIRE_MainWindow", "Resolution Extension/Suppression", None))
        self.radioButton_on.setText(_translate("GENFIRE_MainWindow", "On", None))
        self.radioButton_off.setText(_translate("GENFIRE_MainWindow", "Off", None))
        self.radioButton_extension.setText(_translate("GENFIRE_MainWindow", "Extension Only", None))
        self.label_2.setText(_translate("GENFIRE_MainWindow", "Oversampling Ratio", None))
        self.label_3.setText(_translate("GENFIRE_MainWindow", "Interpolation Cutoff Distance (pixels)", None))
        self.label.setText(_translate("GENFIRE_MainWindow", "Number of Iterations", None))
        self.label_6.setText(_translate("GENFIRE_MainWindow", "Constraints", None))
        self.checkBox_positivity_constraint.setText(_translate("GENFIRE_MainWindow", "Positivity", None))
        self.checkBox_support_constraint.setText(_translate("GENFIRE_MainWindow", "Support", None))
        self.label_7.setText(_translate("GENFIRE_MainWindow", "Gridding Method", None))
        self.radioButton_FFT.setText(_translate("GENFIRE_MainWindow", "FFT", None))
        self.radioButton_DFT.setText(_translate("GENFIRE_MainWindow", "DFT", None))
        self.btn_displayResults.setText(_translate("GENFIRE_MainWindow", "Summarize Results", None))
        self.checkBox_rfree.setText(_translate("GENFIRE_MainWindow", "Calculate Rfree", None))
        self.checkBox_resCircle.setText(_translate("GENFIRE_MainWindow", "Enforce Resolution Circle", None))
        self.checkBox_multiGridding.setText(_translate("GENFIRE_MainWindow", "Permit Multiple Grid-Point Matches", None))
        self.btn_reconstruct.setText(_translate("GENFIRE_MainWindow", "Launch Reconstruction", None))
        self.menuTools.setTitle(_translate("GENFIRE_MainWindow", "Projection Calculator", None))
        self.menuView_Volume.setTitle(_translate("GENFIRE_MainWindow", "View Volume", None))
        self.action_Create_Support.setText(_translate("GENFIRE_MainWindow", "Launch Projection Calculator", None))
        self.action_Volume_Slicer.setText(_translate("GENFIRE_MainWindow", "Launch Volume Slicer", None))
        self.action_2.setText(_translate("GENFIRE_MainWindow", "Exit", None))

