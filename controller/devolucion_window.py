from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from view.get_back_sell import get_back_sell
from pys6_msgBoxes import msg_boxes
from model.sells import insert_sell
from model.products import select_product_by_id, update_qty_product
from datetime import datetime

class return_Window(QWidget, get_back_sell):

    def __init__(self, parent = None):
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.parent = parent
        
        self.AddDevolutionButton.clicked.connect(self.insert_devolution)
        self.cancelDevolutionButton.clicked.connect(self.close)

    def check_inputs(self):
        codeProduct = self.titleLineEdit.text()
        qty = self.amountSpinBox.value()
        valueReturn = self.priceDevolutionSellLineEdit.text()
        description = self.priceDevolutionSellLineEdit_2.text()

        errors_count = 0

        if codeProduct == "":
            msg_boxes.warning_msg_box('Aviso!','El codigo producto es obligatorio')
            # print("El campo nombre es obligatorio")
            errors_count += 1
        if qty == "":
            msg_boxes.warning_msg_box('Aviso!','La cantidad es obligatoria')
            # print("El campo cantidad es obligatorio")
            errors_count += 1
        if valueReturn == "":
            msg_boxes.warning_msg_box('Aviso!','El valor de la devolucion es obligatorio')
            # print("El campo precio ingreso es obligatorio")    
            errors_count += 1    
        if description == "":
            msg_boxes.warning_msg_box('Aviso!','La descripcion es obligatoria')
            # print("El campo precio venta es obligatorio")    
            errors_count += 1

        if errors_count == 0:
            return True
        
    def insert_devolution(self):
        
        fecha_actual = datetime.now()
        fecha_actual_str = fecha_actual.strftime('%Y-%m-%d %I:%M:%S %p')
        
        if self.check_inputs():
            codeProduct = self.titleLineEdit.text()
            qty = str(self.amountSpinBox.value())
            valueReturn = str("-" + self.priceDevolutionSellLineEdit.text())
            description = str(self.priceDevolutionSellLineEdit_2.text()+" (Devolución)")
            payType = "efectivo"
            profits = 0
            
            product = select_product_by_id(codeProduct)
            data = product[0]
            profitsBacks = int(data[5])
            profits = profitsBacks * -1
            
            print("El valor de la devolucion en ganancia es: ", profits)

            data = (fecha_actual_str, payType, valueReturn, profits, description)

            if insert_sell(data):
                
                product = select_product_by_id(codeProduct)
                data = product[0]
                old_stock = int(data[2])
                new_stock = old_stock + int(qty)
                update_qty_product(codeProduct, new_stock)
                
                msg_boxes.correct_msg_box('Correcto!','Devolucion registrada con exito')
                self.parent.refresh_table_from_child_win()
                self.close()
        
    def set_focus_on_barcode(self):
        self.barcodeLineEdit.setFocus()

    # def select_person_by_id(self, id):
    #     data = select_by_id(id)
    #     return data

    def agregar_punto_miles(self, valor):
        valor = int(valor)
        valor_formateado = "{:,.0f}".format(valor)
        return valor_formateado