# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'employee_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class ListProductFormEmployee(object):
    def setupUi(self, ListProductForm):
        if not ListProductForm.objectName():
            ListProductForm.setObjectName(u"ListProductForm")
        ListProductForm.resize(1384, 703)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ListProductForm.sizePolicy().hasHeightForWidth())
        ListProductForm.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"./assets/newicons/icons8-tienda-online-48.png", QSize(), QIcon.Normal, QIcon.Off)
        ListProductForm.setWindowIcon(icon)
        ListProductForm.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: #0069c0;\n"
"}")
        self.gridLayout_4 = QGridLayout(ListProductForm)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_12 = QLabel(ListProductForm)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setLayoutDirection(Qt.LeftToRight)
        self.label_12.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_12.setTextFormat(Qt.MarkdownText)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_12, 4, 3, 1, 1)

        self.ListSellTable = QTableWidget(ListProductForm)
        self.ListSellTable.setObjectName(u"ListSellTable")
        self.ListSellTable.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.ListSellTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout_4.addWidget(self.ListSellTable, 5, 3, 1, 1)

        self.label_11 = QLabel(ListProductForm)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setLayoutDirection(Qt.LeftToRight)
        self.label_11.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_11.setTextFormat(Qt.MarkdownText)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_11, 4, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.label_8 = QLabel(ListProductForm)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.frame = QFrame(ListProductForm)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.labelQty = QLabel(self.frame)
        self.labelQty.setObjectName(u"labelQty")
        self.labelQty.setGeometry(QRect(0, 10, 144, 17))
        sizePolicy.setHeightForWidth(self.labelQty.sizePolicy().hasHeightForWidth())
        self.labelQty.setSizePolicy(sizePolicy)
        self.labelQty.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")

        self.horizontalLayout_6.addWidget(self.frame)


        self.gridLayout_4.addLayout(self.horizontalLayout_6, 6, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_2 = QFrame(ListProductForm)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_2)

        self.label_9 = QLabel(ListProductForm)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")

        self.horizontalLayout_5.addWidget(self.label_9)

        self.lineEditSell = QLineEdit(ListProductForm)
        self.lineEditSell.setObjectName(u"lineEditSell")
        self.lineEditSell.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEditSell.sizePolicy().hasHeightForWidth())
        self.lineEditSell.setSizePolicy(sizePolicy)
        self.lineEditSell.setMaximumSize(QSize(150, 30))
        self.lineEditSell.setFocusPolicy(Qt.NoFocus)
        self.lineEditSell.setStyleSheet(u"font: 700 24pt \"Segoe UI\";")
        self.lineEditSell.setFrame(False)
        self.lineEditSell.setDragEnabled(False)
        self.lineEditSell.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.lineEditSell)

        self.sellButton = QPushButton(ListProductForm)
        self.sellButton.setObjectName(u"sellButton")
        self.sellButton.setMinimumSize(QSize(0, 40))
        self.sellButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.sellButton.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        icon1 = QIcon()
        icon1.addFile(u"./assets/newicons/icons8-dinero-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sellButton.setIcon(icon1)
        self.sellButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.sellButton)

        self.clearButton = QPushButton(ListProductForm)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setMinimumSize(QSize(0, 40))
        self.clearButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.clearButton.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        icon2 = QIcon()
        icon2.addFile(u"./assets/newicons/icons8-limpiar-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clearButton.setIcon(icon2)
        self.clearButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.clearButton)


        self.gridLayout_4.addLayout(self.horizontalLayout_5, 6, 3, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.addcartButton = QPushButton(ListProductForm)
        self.addcartButton.setObjectName(u"addcartButton")
        self.addcartButton.setMinimumSize(QSize(0, 70))
        self.addcartButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addcartButton.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        icon3 = QIcon()
        icon3.addFile(u"./assets/newicons/icons8-agregar-a-carrito-de-compras-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addcartButton.setIcon(icon3)
        self.addcartButton.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.addcartButton)

        self.removecartButton = QPushButton(ListProductForm)
        self.removecartButton.setObjectName(u"removecartButton")
        self.removecartButton.setMinimumSize(QSize(0, 70))
        self.removecartButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.removecartButton.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        icon4 = QIcon()
        icon4.addFile(u"./assets/newicons/icons8-vaciar-carro-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.removecartButton.setIcon(icon4)
        self.removecartButton.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.removecartButton)


        self.gridLayout_4.addLayout(self.verticalLayout_2, 5, 1, 1, 1)

        self.label_10 = QLabel(ListProductForm)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_10, 7, 3, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 15, 0, 15)
        self.label = QLabel(ListProductForm)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEditSearch = QLineEdit(ListProductForm)
        self.lineEditSearch.setObjectName(u"lineEditSearch")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEditSearch.sizePolicy().hasHeightForWidth())
        self.lineEditSearch.setSizePolicy(sizePolicy2)
        self.lineEditSearch.setMaximumSize(QSize(300, 16777215))
        self.lineEditSearch.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")

        self.horizontalLayout_2.addWidget(self.lineEditSearch)

        self.searchButton = QPushButton(ListProductForm)
        self.searchButton.setObjectName(u"searchButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy3)
        self.searchButton.setMinimumSize(QSize(0, 30))
        self.searchButton.setMaximumSize(QSize(30, 16777215))
        self.searchButton.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        icon5 = QIcon()
        icon5.addFile(u"./assets/newicons/icons8-b\u00fasqueda-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon5)

        self.horizontalLayout_2.addWidget(self.searchButton)

        self.frame_3 = QFrame(ListProductForm)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_3)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.ListProductTable = QTableWidget(ListProductForm)
        self.ListProductTable.setObjectName(u"ListProductTable")
        self.ListProductTable.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.ListProductTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout_4.addWidget(self.ListProductTable, 5, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.inicioButton = QPushButton(ListProductForm)
        self.inicioButton.setObjectName(u"inicioButton")
        self.inicioButton.setEnabled(True)
        sizePolicy.setHeightForWidth(self.inicioButton.sizePolicy().hasHeightForWidth())
        self.inicioButton.setSizePolicy(sizePolicy)
        self.inicioButton.setMinimumSize(QSize(0, 80))
        self.inicioButton.setMaximumSize(QSize(150, 16777215))
        self.inicioButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.inicioButton.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        icon6 = QIcon()
        icon6.addFile(u"./assets/newicons/icons8-libro-abierto-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.inicioButton.setIcon(icon6)
        self.inicioButton.setIconSize(QSize(50, 50))
        self.inicioButton.setAutoDefault(False)
        self.inicioButton.setFlat(True)

        self.verticalLayout.addWidget(self.inicioButton)

        self.label_2 = QLabel(ListProductForm)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetFixedSize)
        self.escanearButton = QPushButton(ListProductForm)
        self.escanearButton.setObjectName(u"escanearButton")
        self.escanearButton.setEnabled(True)
        sizePolicy.setHeightForWidth(self.escanearButton.sizePolicy().hasHeightForWidth())
        self.escanearButton.setSizePolicy(sizePolicy)
        self.escanearButton.setMinimumSize(QSize(0, 80))
        self.escanearButton.setMaximumSize(QSize(150, 16777215))
        self.escanearButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.escanearButton.setAutoFillBackground(False)
        self.escanearButton.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.escanearButton.setInputMethodHints(Qt.ImhNone)
        icon7 = QIcon()
        icon7.addFile(u"./assets/newicons/icons8-esc\u00e1ner-de-c\u00f3digo-de-barras-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.escanearButton.setIcon(icon7)
        self.escanearButton.setIconSize(QSize(50, 50))
        self.escanearButton.setAutoDefault(False)
        self.escanearButton.setFlat(True)

        self.verticalLayout_3.addWidget(self.escanearButton)

        self.label_6 = QLabel(ListProductForm)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_6)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetFixedSize)

        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetFixedSize)

        self.horizontalLayout.addLayout(self.verticalLayout_5)


        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_4.setContentsMargins(350, -1, -1, -1)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetFixedSize)

        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout_7.setContentsMargins(100, -1, -1, -1)
        self.salirButton = QPushButton(ListProductForm)
        self.salirButton.setObjectName(u"salirButton")
        self.salirButton.setEnabled(True)
        sizePolicy.setHeightForWidth(self.salirButton.sizePolicy().hasHeightForWidth())
        self.salirButton.setSizePolicy(sizePolicy)
        self.salirButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.salirButton.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        icon8 = QIcon()
        icon8.addFile(u"./assets/newicons/icons8-salida-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.salirButton.setIcon(icon8)
        self.salirButton.setIconSize(QSize(50, 50))
        self.salirButton.setFlat(True)

        self.verticalLayout_7.addWidget(self.salirButton)

        self.label_3 = QLabel(ListProductForm)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")

        self.verticalLayout_7.addWidget(self.label_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)


        self.gridLayout_4.addLayout(self.horizontalLayout_4, 0, 3, 1, 1)


        self.retranslateUi(ListProductForm)

        self.inicioButton.setDefault(False)
        self.escanearButton.setDefault(False)


        QMetaObject.connectSlotsByName(ListProductForm)
    # setupUi

    def retranslateUi(self, ListProductForm):
        ListProductForm.setWindowTitle(QCoreApplication.translate("ListProductForm", u"Lista de productos", None))
        self.label_12.setText(QCoreApplication.translate("ListProductForm", u"Tabla venta", None))
        self.label_11.setText(QCoreApplication.translate("ListProductForm", u"Tabla productos", None))
        self.label_8.setText(QCoreApplication.translate("ListProductForm", u"Cantidad de productos:", None))
        self.frame.setStyleSheet(QCoreApplication.translate("ListProductForm", u"font: 700 11pt \"Segoe UI\";", None))
        self.labelQty.setText(QCoreApplication.translate("ListProductForm", u"#", None))
        self.frame_2.setStyleSheet(QCoreApplication.translate("ListProductForm", u"font: 700 11pt \"Segoe UI\";", None))
        self.label_9.setText(QCoreApplication.translate("ListProductForm", u"Total:", None))
        self.sellButton.setText(QCoreApplication.translate("ListProductForm", u"VENDER", None))
        self.clearButton.setText(QCoreApplication.translate("ListProductForm", u"VACIAR", None))
        self.addcartButton.setText("")
        self.removecartButton.setText("")
        self.label_10.setText(QCoreApplication.translate("ListProductForm", u"Copyright \u00a9 2023 AlejandroMartinez", None))
        self.label.setText(QCoreApplication.translate("ListProductForm", u"Busca productos por nombre  \u00f3 codigo:", None))
        self.searchButton.setText("")
        self.frame_3.setStyleSheet(QCoreApplication.translate("ListProductForm", u"font: 700 11pt \"Segoe UI\";", None))
        self.inicioButton.setText("")
        self.label_2.setText(QCoreApplication.translate("ListProductForm", u"  INICIO", None))
        self.escanearButton.setText("")
        self.label_6.setText(QCoreApplication.translate("ListProductForm", u" ESCANER", None))
        self.salirButton.setText("")
        self.label_3.setText(QCoreApplication.translate("ListProductForm", u"  SALIR", None))
    # retranslateUi

