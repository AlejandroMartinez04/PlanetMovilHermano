import sqlite3 
from sqlite3 import Error
from .connection import query_turso, query_turso2
from .people import parse_rows

def select_all_products_employee():
    query = "SELECT Nombre, Cantidad, Precio, Id_producto, Proveedor FROM ProductsV2"
    data = query_turso(query)
    data = parse_rows(data)  # Parsear los datos obtenidos
    
    # Verifica que data no esté vacío y que contenga el primer elemento
    if data:
        return data # Devuelve las filas directamente como una lista de listas
    else:
        return []  # Si no hay resultados, devuelve una lista vacía

def select_all_products():
    query = "SELECT Nombre, Cantidad, Precio_ingreso, Precio, Id_producto, Proveedor FROM ProductsV2"
    data = query_turso(query)
    data = parse_rows(data)  # Parsear los datos obtenidos
    
    # Verifica que data no esté vacío y que contenga el primer elemento
    if data:
        return data # Devuelve las filas directamente como una lista de listas
    else:
        return []


def select_product_by_id(Id_producto):
    query = f"SELECT Id_producto, Nombre, Cantidad, Precio_ingreso, Precio, Ganancia FROM ProductsV2 WHERE Id_producto = '{Id_producto}'"
    data = query_turso(query)
    data = parse_rows(data)  # Parsear los datos obtenidos
    
    # Verifica que data no esté vacío y que contenga el primer elemento
    if data:
        return data # Devuelve las filas directamente como una lista de listas
    else:
        return []

def select_product_by_id_employee(Id_producto):
    query = f"SELECT Nombre, Cantidad, Precio, Id_producto, Ganancia FROM ProductsV2 WHERE Id_producto = '{Id_producto}'"
    data = query_turso(query)
    data = parse_rows(data)  # Parsear los datos obtenidos
    
    # Verifica que data no esté vacío y que contenga el primer elemento
    if data:
        return data # Devuelve las filas directamente como una lista de listas
    else:
        return []


def select_product_by_id_search(Id_producto):
    query = f"SELECT Nombre, Cantidad, Precio_ingreso, Precio, Id_producto, Proveedor FROM ProductsV2 WHERE Id_producto = {Id_producto}"
    data = query_turso(query)
    data = parse_rows(data)  # Parsear los datos obtenidos
    
    # Verifica que data no esté vacío y que contenga el primer elemento
    if data:
        return data # Devuelve las filas directamente como una lista de listas
    else:
        return []

def select_product_by_name(nombre):
    query = f"SELECT Nombre, Cantidad, Precio_ingreso, Precio, Id_producto, Proveedor FROM ProductsV2 WHERE Nombre LIKE '%{nombre}%'"
    data = query_turso(query)
    data = parse_rows(data)  # Parsear los datos obtenidos
    
    # Verifica que data no esté vacío y que contenga el primer elemento
    if data:
        return data # Devuelve las filas directamente como una lista de listas
    else:
        return []

def select_product_by_name_employee(nombre):
    query = f"SELECT Nombre, Cantidad, Precio, Id_producto, Proveedor FROM ProductsV2 WHERE Nombre LIKE '%{nombre}%'"
    data = query_turso(query)
    data = parse_rows(data)  # Parsear los datos obtenidos
    
    # Verifica que data no esté vacío y que contenga el primer elemento
    if data:
        return data # Devuelve las filas directamente como una lista de listas
    else:
        return []

def insert_product(data):
    sql = f""" INSERT INTO ProductsV2 (Id_producto, Nombre, Cantidad, Precio_ingreso, Precio, Ganancia, Proveedor) 
    VALUES(?,?,?,?,?,?,?)"""

    try:
        insert_success = query_turso2(sql, data)
        if insert_success:
            print("Producto insertado correctamente.")
            return True
        else:
            print("Error al insertar el producto.")
    except Error as e:
        print("Error inserting product: " + str(e))
        return False  
    
def delete_product(Id_producto):
    sql = f"DELETE FROM ProductsV2 WHERE Id_producto = '{Id_producto}'"
   
    try:
        delete_success = query_turso(sql)
        if delete_success:
            print("Producto eliminado correctamente.")
            return True
        else:
            print("Error al eliminar el producto.")
    except Error as e:
        print("Error removing product:" + str(e))
        return False

def update_product(Id_producto, data):
    sql = f""" UPDATE ProductsV2 SET 
                                Nombre = ?, 
                                Cantidad = ?, 
                                Precio_ingreso = ?,
                                Precio = ?,
                                Proveedor = ? 
                WHERE Id_producto = {Id_producto}"""
    
    try:
        insert_success = query_turso2(sql, data)
        if insert_success:
            print("Producto actualizado correctamente.")
            return True
        else:
            print("Error al actualizar el producto.")
    except Error as e:
        print("Error Updating product: " + str(e))
        return False 
    
def update_qty_product(Id_producto, data):
    sql = f""" UPDATE ProductsV2 SET 
                                Cantidad = {data}
                WHERE Id_producto = {Id_producto}"""
    
    try:
        insert_success = query_turso(sql)
        if insert_success:
            print("Producto actualizado correctamente.")
            return True
        else:
            print("Error al actualizar el producto.")
    except Error as e:
        print("Error Updating product: " + str(e))
        return False
    
