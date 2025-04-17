# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'get_back_sell.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import os
import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class get_back_sell(object):
    def setupUi(self, returnWindow):
        if not returnWindow.objectName():
            returnWindow.setObjectName(u"returnWindow")
        returnWindow.resize(320, 400)
        returnWindow.setMinimumSize(QSize(320, 400))
        returnWindow.setTabletTracking(False)
        self.label = QLabel(returnWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 291, 31))
        self.label.setFrameShape(QFrame.Shape.Box)
        self.label_2 = QLabel(returnWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 131, 21))
        self.titleLineEdit = QLineEdit(returnWindow)
        self.titleLineEdit.setObjectName(u"titleLineEdit")
        self.titleLineEdit.setGeometry(QRect(30, 90, 131, 22))
        self.label_3 = QLabel(returnWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 122, 71, 21))
        self.amountSpinBox = QSpinBox(returnWindow)
        self.amountSpinBox.setObjectName(u"amountSpinBox")
        self.amountSpinBox.setGeometry(QRect(30, 150, 88, 31))
        self.amountSpinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.amountSpinBox.setMaximum(1000)
        
        
        self.label_7 = QLabel(returnWindow)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 200, 141, 21))
        self.priceDevolutionSellLineEdit = QLineEdit(returnWindow)
        self.priceDevolutionSellLineEdit.setObjectName(u"priceDevolutionSellLineEdit")
        self.priceDevolutionSellLineEdit.setGeometry(QRect(30, 230, 151, 22))
        self.label_8 = QLabel(returnWindow)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 260, 141, 21))
        self.priceDevolutionSellLineEdit_2 = QLineEdit(returnWindow)
        self.priceDevolutionSellLineEdit_2.setObjectName(u"priceDevolutionSellLineEdit_2")
        self.priceDevolutionSellLineEdit_2.setGeometry(QRect(30, 290, 261, 22))
        
        self.AddDevolutionButton = QPushButton(returnWindow)
        self.AddDevolutionButton.setObjectName(u"AddDevolutionButton")
        self.AddDevolutionButton.setGeometry(QRect(160, 340, 111, 31))
        self.AddDevolutionButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.AddDevolutionButton.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.AddDevolutionButton.setText(u"GUARDAR")
        
        def resource_path(relative_path):
            """Obtener la ruta absoluta a un recurso, funciona para ejecutables y scripts."""
            try:
                # PyInstaller crea una carpeta temporal y almacena el path en _MEIPASS
                base_path = sys._MEIPASS
            except Exception:
                base_path = os.path.abspath(".")
            return os.path.join(base_path, relative_path)
        
        icon_path1 = resource_path("assets/newicons/icons8-enviar-48.png")
        icon = QIcon()
        icon.addFile(icon_path1, QSize(), QIcon.Normal, QIcon.Off)
        self.AddDevolutionButton.setIcon(icon)
        self.AddDevolutionButton.setFlat(False)
        
        self.cancelDevolutionButton = QPushButton(returnWindow)
        self.cancelDevolutionButton.setObjectName(u"cancelDevolutionButton")
        self.cancelDevolutionButton.setGeometry(QRect(40, 340, 111, 31))
        self.cancelDevolutionButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cancelDevolutionButton.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.cancelDevolutionButton.setText(u"CANCELAR")
        
        icon_path2 = resource_path("assets/newicons/icons8-cancelar-48.png")
        icon = QIcon()
        icon.addFile(icon_path2, QSize(), QIcon.Normal, QIcon.Off)
        self.cancelDevolutionButton.setIcon(icon)
        self.cancelDevolutionButton.setFlat(False)
        
        

        self.retranslateUi(returnWindow)

        QMetaObject.connectSlotsByName(returnWindow)
    # setupUi

    def retranslateUi(self, returnWindow):
        returnWindow.setWindowTitle(QCoreApplication.translate("returnWindow", u"Devolucion venta", None))
        self.label.setStyleSheet(QCoreApplication.translate("returnWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label.setText(QCoreApplication.translate("returnWindow", u"<html><head/><body><p align=\"center\">DEVOLUCION VENTA</p></body></html>", None))
        self.label_2.setStyleSheet(QCoreApplication.translate("returnWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_2.setText(QCoreApplication.translate("returnWindow", u"<html><head/><body><p>C\u00f3digo producto</p></body></html>", None))
        self.titleLineEdit.setStyleSheet(QCoreApplication.translate("returnWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_3.setStyleSheet(QCoreApplication.translate("returnWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_3.setText(QCoreApplication.translate("returnWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Cantidad</span></p></body></html>", None))
        self.amountSpinBox.setStyleSheet(QCoreApplication.translate("returnWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_7.setStyleSheet(QCoreApplication.translate("returnWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_7.setText(QCoreApplication.translate("returnWindow", u"<html><head/><body><p>Valor devoluci\u00f3n</p></body></html>", None))
        self.priceDevolutionSellLineEdit.setStyleSheet(QCoreApplication.translate("returnWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_8.setStyleSheet(QCoreApplication.translate("returnWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_8.setText(QCoreApplication.translate("returnWindow", u"<html><head/><body><p>Detalle devoluci\u00f3n</p></body></html>", None))
        self.priceDevolutionSellLineEdit_2.setStyleSheet(QCoreApplication.translate("returnWindow", u"font: 700 11pt \"Segoe UI\";", None))
    # retranslateUi

