from datetime import datetime
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QInputDialog, QHeaderView, QMainWindow
from view.main_windows import ListProductForm
from model.products import select_all_products, select_product_by_id, select_product_by_name, delete_product, update_qty_product, select_product_by_id_search
from model.sells import select_all_sells, insert_sell, select_sell_by_date
from pys6_msgBoxes import msg_boxes
from pys6_msgBoxes.input_box import input_msg_box, resource_path

import os
import platform

from pathlib import Path
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

class ListProducWindows(QWidget, ListProductForm):

    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.agregarButton.clicked.connect(self.open_new_product_windows)
        self.editarButton.clicked.connect(self.open_edit_product_window)
        self.gananciasButton.clicked.connect(self.open_ganancias_window)
        self.ListProductTable.cellClicked.connect(self.select_row)
        self.ListSellTable.cellClicked.connect(self.select_row_table2)
        self.removecartButton.clicked.connect(self.eliminar_fila_seleccionada)
        self.table_config2()
        self.table_config()
        self.populate_table(select_all_products())
        self.searchButton.clicked.connect(self.search_any)
        self.inicioButton.clicked.connect(lambda:self.populate_table(select_all_products()))
        self.eliminarButton.clicked.connect(self.delete_product_windows)
        self.addcartButton.clicked.connect(self.agregar_carrito_table_click)
        self.sellButton.clicked.connect(self.do_sell)
        self.clearButton.clicked.connect(self.clean_table_sells)
        self.lineEditSearch.returnPressed.connect(self.searchButton.click)
        self.pushButton.clicked.connect(self.close)
        self.escanearButton.clicked.connect(self.ver_facturas)
        self.devolverButton.clicked.connect(self.open_new_return_windows)

        self.sellButton.setDefault(True)
        self.lineEditSearch.setFocus()

    def keyPressEvent(self, event):
         condition = self.set_condition_met()
         if condition and event.key() == 16777220:
            self.sellButton.click()

    def set_condition_met(self):
        ganancia_total = self.ganancia_neta()
        ganancia_total_without_format = int(ganancia_total.replace(",", ""))
        if not self.lineEditSearch.hasFocus() and ganancia_total_without_format > 0:
            return True
        else:
            return False
        
            
    def clean_table_sells(self):
        self.ListSellTable.clearContents()
        self.ListSellTable.setRowCount(0)
        self.lineEditSell.setText(None)

    def refresh_table_from_child_win(self):
        data = select_all_products()
        self.populate_table(data)
        self.lineEditSearch.setFocus()

    def open_new_product_windows(self):
        from controller.new_product_window import NewProductWindow
        window = NewProductWindow(self)
        window.show()
        self.lineEditSearch.setFocus()
        
    def open_new_return_windows(self):
        from controller.devolucion_window import return_Window
        window = return_Window(self)
        window.show()
        self.lineEditSearch.setFocus()

    def open_edit_product_window(self): 
        from controller.edit_product_window import EditProductWindow
        selected_row = self.ListProductTable.selectedItems()
        if selected_row:
            valor_ingresado = input_msg_box("Ingresar contraseña", "Ingresa la contraseña:")
            if valor_ingresado == '0827':
                product_id = int(selected_row[4].text())
                print(product_id)
                window = EditProductWindow(self, product_id)
                window.show()
            else:
                msg_boxes.error_msg_box('Error', 'Contraseña no coincide')
                print("no Ingreso Dato")
        self.ListProductTable.clearSelection()
        self.lineEditSearch.setFocus()
                    
       
    def open_ganancias_window(self):
        from controller.ganancias_windows import GananciasWindow
        window = GananciasWindow(self)
        window.show()
        self.lineEditSearch.setFocus()

    def delete_product_windows(self):
        selected_row = self.ListProductTable.selectedItems()
        if selected_row:
            valor_ingresado = input_msg_box("Ingresar contraseña", "Ingresa la contraseña:")
            if valor_ingresado == '0827':
                product_id = selected_row[4].text()
                row = selected_row[0].row()
                if delete_product(product_id):
                    self.ListProductTable.removeRow(row)
                    msg_boxes.correct_msg_box('Correcto!','Producto eliminado con exito')
            else:
                msg_boxes.error_msg_box('Error', 'Contraseña no coincide')
        else:
            msg_boxes.warning_msg_box('Error', 'Seleccione el producto a eliminar del INVENTARIO')
        self.records_qty()
        self.lineEditSearch.setFocus()          


    def table_config(self):
        column_headers = ("Nombre", "Cantidad", "Precio ingreso", "Precio", "Codigo", "Proveedor")
        self.ListProductTable.setColumnCount(len(column_headers))
        self.ListProductTable.setHorizontalHeaderLabels(column_headers)
        self.ListProductTable.setColumnWidth(3, 80)
        self.ListProductTable.setColumnWidth(1, 40)
        self.ListProductTable.setColumnWidth(2, 60)
        self.ListProductTable.setColumnWidth(0, 317)
        self.ListProductTable.setColumnWidth(4, 30)
        self.ListProductTable.setColumnWidth(5, 60)
        self.ListProductTable.verticalHeader().hide()
        self.ListProductTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

        header = self.ListProductTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
    
    def populate_table(self, data):
        self.ListProductTable.setRowCount(len(data))
        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.ListProductTable.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
        self.records_qty()
        self.lineEditSearch.clear()
        self.lineEditSearch.setFocus()

    def table_config2(self):
        column_headers = ("Codigo","Nombre","Cantidad","Precio unitario","Precio neto")
        self.ListSellTable.setColumnCount(len(column_headers))
        self.ListSellTable.setHorizontalHeaderLabels(column_headers) 
        self.ListSellTable.setColumnWidth(3, 110)
        # self.ListSellTable.setColumnWidth(1, 228)
        self.ListSellTable.setColumnWidth(2, 70)
        self.ListSellTable.setColumnWidth(4, 110)
        self.ListSellTable.setColumnWidth(5, 110)
        self.ListSellTable.verticalHeader().hide()
        self.ListSellTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)

        header = self.ListSellTable.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        
    def populate_table2(self, data):
        current_row_count = self.ListSellTable.rowCount()
        new_row_count = current_row_count + len(data)
        self.ListSellTable.setRowCount(new_row_count)

        for index_row, row in enumerate(data):
            for index_cell, cell in enumerate(row):
                item = QTableWidgetItem(str(cell))
                self.ListSellTable.setItem(current_row_count + index_row, index_cell, item)

    def search_product_by_name(self, Nombre):
        data = select_product_by_name(Nombre)
        self.populate_table(data)     

    def search_product_by_barcode_scanner(self, Codigo_barras):
        data = select_product_by_id(Codigo_barras)
        return data
    
    def search_product_by_barcode(self, Codigo_barras):
        data = select_product_by_id_search(Codigo_barras)
        self.populate_table(data)
        return data

    def search_any(self):
        
        parameter = self.lineEditSearch.text().strip()

        if parameter == "":
            self.do_sell()
        else:

            dataCode = self.search_product_by_barcode(parameter)

            if not dataCode:
                self.search_product_by_name(parameter)
            else:
                self.search_product_by_barcode(parameter)
                self.ListProductTable.selectRow(0)
                self.agregar_carrito_table_click()
                
        self.lineEditSearch.clear()


    def records_qty(self):
        qty_rows = str(self.ListProductTable.rowCount())
        self.labelQty.setText(qty_rows)

    def select_row(self, row):
        self.ListProductTable.selectRow(row)
    
    def select_row_table2(self, row):
        self.ListSellTable.selectRow(row)

    def eliminar_fila_seleccionada(self):
        selected_row = self.ListSellTable.currentRow()
        if selected_row >= 0:
            self.ListSellTable.removeRow(selected_row)
            total = self.sum_last_column()
            self.lineEditSell.setText(total)

    def agregar_carrito_table_click(self):
        selected_items = self.ListProductTable.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            product_id = self.ListProductTable.item(row, 4).text()
            data = select_product_by_id(product_id)
            data_normal = data[0]
            name = data_normal[1]
            qty__stock = int(data_normal[2])

            while True:
                quantity = QInputDialog.getText(None, "Cantidad de productos", "Introduce la cantidad:")
                quantity_int = int(quantity[0])
                if quantity_int <= qty__stock:
                    break
                else:
                    msg_boxes.warning_msg_box('Aviso!','La cantidad es mayor que la cantidad existente. Inténtelo nuevamente.')
            
            qty = int(quantity[0])
            price = str(data_normal[4])
            if len(price) > 3:
                price_without_format = int(price.replace(",", ""))
                code = product_id
                price_neto = qty * price_without_format
                precio_neto_format = self.agregar_punto_miles(price_neto)
            else:
                code = product_id
                price = int(price)
                price_neto = qty * price
                price_neto_str = str(price_neto)
                if len(price_neto_str) > 3:
                    precio_neto_format = self.agregar_punto_miles(price_neto)
                else:
                    precio_neto_format = price_neto
            data_full = [(code, name, qty, price, precio_neto_format)]
            self.populate_table2(data_full)
        self.ListProductTable.clearSelection()
        total = self.sum_last_column()
        self.lineEditSell.setText(total)
        self.lineEditSearch.setFocus()

    def agregar_punto_miles(self, valor):
        valor = int(valor)
        valor_formateado = "{:,.0f}".format(valor)
        return valor_formateado

    def sum_last_column(self):
        total = 0
        for row in range(self.ListSellTable.rowCount()):
            item = self.ListSellTable.item(row, self.ListSellTable.columnCount() - 1)
            if item is not None:
                value_str= item.text()
                value = int(value_str.replace(",", ""))
                total += value
        total_format = self.agregar_punto_miles(total)
        return total_format

    def historial_sells(self):
        data_acumulada = ''
        for row in range(self.ListSellTable.rowCount()):
            item = self.ListSellTable.item(row, 0)
            qty = self.ListSellTable.item(row, self.ListSellTable.columnCount() - 3)
            qty = qty.text()
            name = self.ListSellTable.item(row, self.ListSellTable.columnCount() - 4)
            name = name.text()
            if item is not None:
                if "reparacion" in name:
                    # Solicitar detalles de la reparación
                    detalles = QInputDialog.getText(
                        None, 
                        "Detalles de Reparación",
                        "Ingrese los detalles de la reparación:"
                    )
                    if detalles[0]:
                        data = ('Producto: ' + name + ', cantidad: '+ qty + ', Detalles: ' + detalles[0])
                    else:
                        data = ('Producto: ' + name + ', cantidad: '+ qty)
                else:
                    data = ('Producto: ' + name + ', cantidad: '+ qty)
                data_acumulada += data + '\n'
        return data_acumulada

    def ganancia_neta(self):
        total = 0
        for row in range(self.ListSellTable.rowCount()):
            item = self.ListSellTable.item(row, 0)
            qty = self.ListSellTable.item(row, self.ListSellTable.columnCount() - 3)
            qty = int(qty.text())
            if item is not None:
                product_id = item.text()
                data = self.search_product_by_barcode_scanner(product_id)
                data__normal = data[0]
                profits = data__normal[5]
                temp_profits = int(profits) * qty
                total += temp_profits
        total_format = self.agregar_punto_miles(total)
        return total_format
    
    def productos_factura(self):
        productos = []
        for row in range(self.ListSellTable.rowCount()):
            item = self.ListSellTable.item(row, 0)
            qty = self.ListSellTable.item(row, self.ListSellTable.columnCount() - 3)
            qty = qty.text()
            name = self.ListSellTable.item(row, self.ListSellTable.columnCount() - 4)
            name = name.text()
            price = self.ListSellTable.item(row, self.ListSellTable.columnCount() - 2)
            price = price.text()
            if item is not None:
                producto = {
                    'nombre': name,
                    'cantidad': qty,
                    'precio_unitario': price
                }
                productos.append(producto)
        return productos
    
    def generar_consecutivo(self):
        archivo_consecutivo = "consecutivo.txt"
        if os.path.exists(archivo_consecutivo):
            with open(archivo_consecutivo, "r") as archivo:
                consecutivo = int(archivo.read())
        else:
            consecutivo = 1

        consecutivo_str = str(consecutivo).zfill(4)
        consecutivo += 1

        with open(archivo_consecutivo, "w") as archivo:
            archivo.write(str(consecutivo))
        return consecutivo_str
        

    
    def generar_factura_venta(self, tipo_pago, monto_total, productos_vendidos):

        while True:

            while True:
                name = QInputDialog.getText(None, "Nombre del cliente", "Escribe el nombre:")
                if name[0]: 
                    break
                msg_boxes.warning_msg_box('Aviso!', 'El nombre no puede ser vacío.')

            while True:
                document = QInputDialog.getText(None, "Documento del cliente", "Escribe el documento:")
                if document[0]:  
                    break
                msg_boxes.warning_msg_box('Aviso!', 'El documento no puede ser vacío.')

            break 

        documentos_path = Path.home() / "Documents"
        if not documentos_path.exists():
            documentos_path = Path.home() / "Documentos"

        facturas_path = documentos_path / "Facturas"
        facturas_path.mkdir(parents=True, exist_ok=True)

        fecha_actual = datetime.now()
        fecha_actual_str = fecha_actual.strftime('%Y-%m-%d %I:%M:%S %p')

        ancho_papel = 9 * cm
        alto_papel = 20 * cm
        
        nro_consecutivo = self.generar_consecutivo()
        factura_filename = f"factura_venta_{nro_consecutivo}.pdf"
        factura_path = facturas_path / factura_filename
        
        print(f"Intentando crear factura en: {factura_path}")

        pdf = SimpleDocTemplate(
            str(factura_path),
            pagesize=(ancho_papel, alto_papel),
            rightMargin=0.1*cm,
            leftMargin=0.1*cm,
            topMargin=0*cm,
            bottomMargin=0*cm
        )

        styles = getSampleStyleSheet()
        estilo_titulo = ParagraphStyle('Titulo', fontSize=18, alignment=TA_CENTER, spaceAfter=0.5*cm)
        estilo_texto = ParagraphStyle('Texto', fontSize=16, alignment=TA_LEFT, spaceAfter=0.2*cm)

        # logo_path = './assets/logo.png'
        logo_path = resource_path("assets/logo.png")
        logo = Image(str(logo_path), width=6.5*cm, height=1.5*cm)
        logo.hAlign = 'CENTER'

        elementos = [
            logo,
            Paragraph("<b>Factura de Venta</b>", estilo_titulo),
            Paragraph(f"Nro factura: {nro_consecutivo}", estilo_texto),
            Paragraph(f"Fecha: {fecha_actual_str}", estilo_texto),
            Paragraph(f"Nit: 1037651327-1", estilo_texto),
            Paragraph("Direccion: Calle 48 # 04 06 Copacabana", estilo_texto),
            Paragraph(f"Cliente: {name[0]}", estilo_texto),
            Paragraph(f"Documento: {document[0]}", estilo_texto),
            Spacer(1, 0.2*cm),
            Paragraph("<b>Productos:</b>", estilo_texto),
        ]

        estilo_nombre_producto = ParagraphStyle('NombreProducto', fontSize=16, alignment=TA_LEFT, spaceAfter=0.2*cm)

        estilo_cantidad_precio = ParagraphStyle('CantidadPrecio', fontSize=14, alignment=TA_LEFT, spaceAfter=0.5*cm)
        
        for producto in productos_vendidos:
            elementos.append(Spacer(1, 0.2*cm))
            
            nombre_producto = Paragraph(f"<b>{producto['nombre']}</b>", estilo_nombre_producto)
            elementos.append(nombre_producto)
            
            cantidad_precio = Paragraph(f"Cantidad: {producto['cantidad']} - Precio: {producto['precio_unitario']}", estilo_cantidad_precio)
            elementos.append(cantidad_precio)

        elementos.extend([
            Spacer(1, 0.2*cm),
            Paragraph(f"<b>Total:</b> {monto_total}", estilo_texto),
            Spacer(1, 0.2*cm),
            Paragraph("¡Gracias por su compra!", estilo_titulo),
            Paragraph("Presente su factura en caso de reclamos.", estilo_titulo)
        ])

        try:
            pdf.build(elementos)
            print(f"Factura generada exitosamente en: {factura_path}")
            if factura_path .exists():
                print("El archivo de factura creado en la ubicación especificada.")
                msg_boxes.correct_msg_box('Correcto!','Factura creada')
            else:
                print("Error: El archivo de factura no se creo en la ubicación especificada.")
        except Exception as e:
            print(f"Error al generar la factura: {str(e)}")
        
        self.lineEditSearch.setFocus()
        return str(factura_path)
    
    def imprimir_factura(self, factura_path):
        try:
            if platform.system() == "Windows":
                os.startfile(factura_path)
                os.stat(factura_path)
        except Exception as e:
            print(f"Error al intentar imprimir la factura: {str(e)}")
        self.lineEditSearch.setFocus()

    def ver_facturas(self):

        documentos_path = Path.home() / "Documents"
        if not documentos_path.exists():
            documentos_path = Path.home() / "Documentos"

        facturas_path = documentos_path / "Facturas"

        try:
            if platform.system() == "Windows":
                os.startfile(facturas_path)
        except Exception as e:
            print(f"Error al abrir las facturas: {str(e)}")
            
        self.lineEditSearch.setFocus()


    def do_sell(self):
        confirmacion = msg_boxes.warning_check_msg_box('Confirmar','Confirmar venta')
        if confirmacion == QMessageBox.Yes:
            fecha_actual = datetime.now()
            fecha_actual_str = fecha_actual.strftime('%Y-%m-%d %I:%M:%S %p')
            monto_total = self.sum_last_column()

            respuesta_descuento = msg_boxes.warning_check_msg_box('Aplicar descuento', '¿Desea aplicar descuento?')
            if respuesta_descuento == QMessageBox.Yes:
                porcentaje_descuento = QInputDialog.getText(None, "Porcentaje descuento", "Introduce el porcentaje de descuento:")
                porcentaje_descuento = int(porcentaje_descuento[0])
                if porcentaje_descuento:
                    porcentaje_descuento = int(porcentaje_descuento)
                    valor_descuento = int(int(monto_total.replace(",", "")) * (porcentaje_descuento/100))
                    monto_total = int(int(monto_total.replace(",", "")) - valor_descuento)
                    monto_total = self.agregar_punto_miles(monto_total)
                    self.lineEditSell.setText(monto_total)
                    ganancia_total = self.ganancia_neta()
                    ganancia_total = int(ganancia_total.replace(",", "")) - valor_descuento
                    tipo_pago = 'Efectivo'
                    detalle = str(self.historial_sells())
                    productos_vendidos = self.productos_factura()
            else:
                ganancia_total = self.ganancia_neta()
                tipo_pago = 'Efectivo'
                detalle = str(self.historial_sells())
                productos_vendidos = self.productos_factura()     
                                      
            data = (fecha_actual_str, tipo_pago, monto_total, ganancia_total, detalle)
            if monto_total > str(0):
                if confirmacion == QMessageBox.Yes:
                    insert_sell(data)
                    self.update_qty_product_form()
                    msg_boxes.correct_msg_box('Correcto!','Se realizó la venta')
                    self.clean_table_sells()
                    respuesta_imprimir = msg_boxes.warning_check_msg_box('Imprimir factura', '¿Desea imprimir la factura?')
                    if respuesta_imprimir == QMessageBox.Yes:
                        self.generar_factura_venta(self, monto_total, productos_vendidos)
            else :
                msg_boxes.warning_msg_box('Aviso!','No hay productos en el carrito')

    def update_qty_product_form(self):
        for row in range(self.ListSellTable.rowCount()):
            item = self.ListSellTable.item(row, self.ListSellTable.columnCount() - 3)
            item_id = self.ListSellTable.item(row, self.ListSellTable.columnCount() - 5)
            if item is not None:
                qty_selled = int(item.text())
                product_id = item_id.text()
                product = select_product_by_id(product_id)
                new_id = product_id
                data = product[0]
                old_stock = int(data[2])
                new_stock = old_stock - qty_selled
                update_qty_product(new_id, new_stock)
        self.populate_table(select_all_products())

    def count_products(self, item_id_arrive):
        product_count = 0
        for row in range(self.ListSellTable.rowCount()):
            item_id = self.ListSellTable.item(row, 0).text()
            item_quantity = int(self.ListSellTable.item(row, 2).text())
            if item_id == item_id_arrive:
                product_count += item_quantity
            else:
                product_count = 0
            
        return product_count
