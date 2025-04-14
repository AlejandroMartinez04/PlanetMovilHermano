# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'get_back_sell.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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
    def setupUi(self, newProductWindow):
        if not newProductWindow.objectName():
            newProductWindow.setObjectName(u"newProductWindow")
        newProductWindow.resize(320, 458)
        newProductWindow.setMinimumSize(QSize(320, 400))
        newProductWindow.setTabletTracking(False)
        self.label = QLabel(newProductWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 291, 31))
        self.label.setFrameShape(QFrame.Shape.Box)
        self.label_2 = QLabel(newProductWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 120, 131, 21))
        self.titleLineEdit = QLineEdit(newProductWindow)
        self.titleLineEdit.setObjectName(u"titleLineEdit")
        self.titleLineEdit.setGeometry(QRect(30, 150, 131, 22))
        self.label_3 = QLabel(newProductWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 182, 71, 21))
        self.amountSpinBox = QSpinBox(newProductWindow)
        self.amountSpinBox.setObjectName(u"amountSpinBox")
        self.amountSpinBox.setGeometry(QRect(30, 210, 88, 31))
        self.amountSpinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.amountSpinBox.setMaximum(1000)
        self.AddDevolutionButton = QPushButton(newProductWindow)
        self.AddDevolutionButton.setObjectName(u"AddDevolutionButton")
        self.AddDevolutionButton.setGeometry(QRect(160, 400, 111, 31))
        self.AddDevolutionButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.AddDevolutionButton.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.AddDevolutionButton.setText(u"GUARDAR")
        icon = QIcon()
        icon.addFile(u"../assets/newicons/icons8-enviar-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.AddDevolutionButton.setIcon(icon)
        self.AddDevolutionButton.setFlat(False)
        self.cancelDevolutionButton = QPushButton(newProductWindow)
        self.cancelDevolutionButton.setObjectName(u"cancelDevolutionButton")
        self.cancelDevolutionButton.setGeometry(QRect(40, 400, 111, 31))
        self.cancelDevolutionButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cancelDevolutionButton.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.cancelDevolutionButton.setText(u"CANCELAR")
        icon1 = QIcon()
        icon1.addFile(u"../assets/newicons/icons8-cancelar-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cancelDevolutionButton.setIcon(icon1)
        self.cancelDevolutionButton.setFlat(False)
        self.label_7 = QLabel(newProductWindow)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 250, 141, 21))
        self.priceDevolutionSellLineEdit = QLineEdit(newProductWindow)
        self.priceDevolutionSellLineEdit.setObjectName(u"priceDevolutionSellLineEdit")
        self.priceDevolutionSellLineEdit.setGeometry(QRect(30, 280, 151, 22))
        self.barcodeLineEdit = QLineEdit(newProductWindow)
        self.barcodeLineEdit.setObjectName(u"barcodeLineEdit")
        self.barcodeLineEdit.setGeometry(QRect(30, 90, 101, 22))
        self.label_4 = QLabel(newProductWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 60, 111, 21))
        self.label_8 = QLabel(newProductWindow)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 320, 141, 21))
        self.priceDevolutionSellLineEdit_2 = QLineEdit(newProductWindow)
        self.priceDevolutionSellLineEdit_2.setObjectName(u"priceDevolutionSellLineEdit_2")
        self.priceDevolutionSellLineEdit_2.setGeometry(QRect(30, 350, 261, 22))

        self.retranslateUi(newProductWindow)

        QMetaObject.connectSlotsByName(newProductWindow)
    # setupUi

    def retranslateUi(self, newProductWindow):
        newProductWindow.setWindowTitle(QCoreApplication.translate("newProductWindow", u"Devolucion venta", None))
        self.label.setStyleSheet(QCoreApplication.translate("newProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label.setText(QCoreApplication.translate("newProductWindow", u"<html><head/><body><p align=\"center\">DEVOLUCION VENTA</p></body></html>", None))
        self.label_2.setStyleSheet(QCoreApplication.translate("newProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_2.setText(QCoreApplication.translate("newProductWindow", u"<html><head/><body><p>C\u00f3digo producto</p></body></html>", None))
        self.titleLineEdit.setStyleSheet(QCoreApplication.translate("newProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_3.setStyleSheet(QCoreApplication.translate("newProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_3.setText(QCoreApplication.translate("newProductWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Cantidad</span></p></body></html>", None))
        self.amountSpinBox.setStyleSheet(QCoreApplication.translate("newProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_7.setStyleSheet(QCoreApplication.translate("newProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_7.setText(QCoreApplication.translate("newProductWindow", u"<html><head/><body><p>Valor devoluci\u00f3n</p></body></html>", None))
        self.priceDevolutionSellLineEdit.setStyleSheet(QCoreApplication.translate("newProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.barcodeLineEdit.setStyleSheet(QCoreApplication.translate("newProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_4.setStyleSheet(QCoreApplication.translate("newProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_4.setText(QCoreApplication.translate("newProductWindow", u"<html><head/><body><p>C\u00f3digo venta</p></body></html>", None))
        self.label_8.setStyleSheet(QCoreApplication.translate("newProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_8.setText(QCoreApplication.translate("newProductWindow", u"<html><head/><body><p>Detalle devoluci\u00f3n</p></body></html>", None))
        self.priceDevolutionSellLineEdit_2.setStyleSheet(QCoreApplication.translate("newProductWindow", u"font: 700 11pt \"Segoe UI\";", None))
    # retranslateUi

