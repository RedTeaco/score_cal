# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'designerRbUilk.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QPushButton,
                               QSizePolicy, QStatusBar, QVBoxLayout, QFileDialog,
                               QWidget, QLabel, QSpinBox, QSpacerItem, QListWidget, QListWidgetItem)
from src import pdfexec


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(737, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 741, 591))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pdfLoad = QPushButton(self.horizontalLayoutWidget)
        self.pdfLoad.setObjectName(u"pdfLoad")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pdfLoad.sizePolicy().hasHeightForWidth())
        self.pdfLoad.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pdfLoad)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.term = QSpinBox(self.horizontalLayoutWidget)
        self.term.setObjectName(u"term")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.term.sizePolicy().hasHeightForWidth())
        self.term.setSizePolicy(sizePolicy1)
        self.term.setMinimumSize(QSize(60, 0))
        self.term.setBaseSize(QSize(0, 0))
        self.term.setMinimum(2021)
        self.term.setMaximum(9999)

        self.horizontalLayout_2.addWidget(self.term)

        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.listWidget = QListWidget(self.horizontalLayoutWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout.addWidget(self.listWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"课程加权平均分计算", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u5e74\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u79cb\u5b63\u5b66\u671f", None))
        self.pdfLoad.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9PDF...", None))
        self.pdfLoad.clicked.connect(self.get_pdf)

    # retranslateUi

    def get_pdf(self):
        file_paths, _ = QFileDialog.getOpenFileNames(
            self.centralwidget,
            "请选择pdf文件",
            '',
            "PDF文件 (*.pdf)"
        )
        print(file_paths)
        self.show(pdfexec.main(file_paths, self.term.value()))

    def show(self, ls: list[dict]):
        for d in ls:
            a = QListWidgetItem(self.listWidget)
            text = ''.join(
                [d.get('name'), "的课程加权平均分为:", str(d.get('G21'))])
            print(text)
            a.setText(QCoreApplication.translate('MainWindow', text, None))
            self.listWidget.addItem(a)


def gui():
    import sys

    app = QApplication(sys.argv)
    win = QMainWindow()
    gui = Ui_MainWindow()
    gui.setupUi(win)
    win.show()
    app.exec()
if __name__ == '__main__':
    gui()
