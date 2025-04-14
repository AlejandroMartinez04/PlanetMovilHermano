from PySide6.QtWidgets import QWidget
from view.get_back_sell import returnWindow
from pys6_msgBoxes import msg_boxes
from model.sells import insert_sell
from model.products import update_product

class return_Window(QWidget, returnWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.set_focus_on_line_edit()
        self.enviarBtn.clicked.connect(self.check_input)
        self.cancelarBtn.clicked.connect(self.close)
        
        self.userLine.returnPressed.connect(self.check_input)
        self.pwLine.returnPressed.connect(self.check_input)

    def check_inputs(self):
        name = self.titleLineEdit.text()
        amount = self.amountSpinBox.value()
        princeInt = self.priceSaleLineEdit_2.text()
        priceOut = self.priceSaleLineEdit.text()
        barcode = self.barcodeLineEdit.text()

        errors_count = 0

        if name == "":
            msg_boxes.warning_msg_box('Aviso!','El campo nombre es obligatorio')
            # print("El campo nombre es obligatorio")
            errors_count += 1
        if amount == "":
            msg_boxes.warning_msg_box('Aviso!','El campo cantidad es obligatorio')
            # print("El campo cantidad es obligatorio")
            errors_count += 1
        if princeInt == "":
            msg_boxes.warning_msg_box('Aviso!','El campo precio ingreso es obligatorio')
            # print("El campo precio ingreso es obligatorio")    
            errors_count += 1    
        if priceOut == "":
            msg_boxes.warning_msg_box('Aviso!','El campo precio venta es obligatorio')
            # print("El campo precio venta es obligatorio")    
            errors_count += 1
        if barcode == "":
            msg_boxes.warning_msg_box('Aviso!','El campo codigo de barras es obligatorio')
            # print("El campo codigo de barras es obligatorio")    
            errors_count += 1

        if errors_count == 0:
            return True

            
        
    def set_focus_on_line_edit(self):
        self.userLine.setFocus()

    def select_person_by_id(self, id):
        data = select_by_id(id)
        return data

    def open_admin_view(self):
        from controller.main_window import ListProducWindows
        window = ListProducWindows()
        
    def edit_product(self):
        name = self.titleLineEdit.text()
        amount = str(self.amountSpinBox.value())
        priceInt = self.priceSaleLineEdit_2.text()
        priceInt_without_format = int(priceInt.replace(",", ""))
        priceInt_format = self.agregar_punto_miles(priceInt_without_format)
        priceOut = self.priceSaleLineEdit.text()
        priceOut_without_format = int(priceOut.replace(",", ""))
        priceOut_format = self.agregar_punto_miles(priceOut_without_format)
        provider = self.providerLineEdit.text()

        data = [name, amount, priceInt_format, priceOut_format, provider]

        if update_product(self.codigo_barras, data) and self.check_inputs():
            msg_boxes.correct_msg_box('Correcto!','Producto actualizado con exito')
            self.parent.refresh_table_from_child_win()
            self.close()

    def agregar_punto_miles(self, valor):
        valor = int(valor)
        valor_formateado = "{:,.0f}".format(valor)
        return valor_formateado