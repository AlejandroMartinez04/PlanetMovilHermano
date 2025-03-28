import sqlite3 
from sqlite3 import Error
from .connection import query_turso, query_turso2

def select_all_products():
    query = "SELECT Nombre, Cantidad, Precio_ingreso, Precio, Id_producto, Proveedor FROM ProductsV2"
    data = query_turso(query)
    
    # Verifica que data no esté vacío y que contenga el primer elemento
    if data and isinstance(data, list) and len(data) > 0 and 'results' in data[0]:
        results = data[0]['results']  # Acceder al primer elemento de la lista
        
        # Verifica que haya filas en los resultados
        if results['rows']:
            return results['rows']  # Devuelve las filas directamente como una lista de listas

    return []  # Si no hay resultados, devuelve una lista vacía


def select_product_by_id(Id_producto):
    query = f"SELECT Id_producto, Nombre, Cantidad, Precio_ingreso, Precio, Ganancia FROM ProductsV2 WHERE Id_producto = '{Id_producto}'"
    data = query_turso(query)
    # Verifica que data no esté vacío y que contenga el primer elemento
    if data and isinstance(data, list) and len(data) > 0 and 'results' in data[0]:
        results = data[0]['results']  # Acceder al primer elemento de la lista
        
        # Verifica que haya filas en los resultados
        if results['rows']:
            return results['rows']  # Devuelve las filas directamente como una lista de listas

    return []  # Si no hay resultados, devuelve una lista vacía


def select_product_by_id_search(Id_producto):
    query = f"SELECT Nombre, Cantidad, Precio_ingreso, Precio, Id_producto, Proveedor FROM ProductsV2 WHERE Id_producto = '{Id_producto}'"
    data = query_turso(query)
    
    # Verifica que data no esté vacío y que contenga el primer elemento
    if data and isinstance(data, list) and len(data) > 0 and 'results' in data[0]:
        results = data[0]['results']  # Acceder al primer elemento de la lista
        
        # Verifica que haya filas en los resultados
        if results['rows']:
            return results['rows']  # Devuelve las filas directamente como una lista de listas

    return []  # Si no hay resultados, devuelve una lista vacía

def select_product_by_name(nombre):
    query = f"SELECT Nombre, Cantidad, Precio_ingreso, Precio, Id_producto, Proveedor FROM ProductsV2 WHERE Nombre LIKE '%{nombre}%'"
    data = query_turso(query)
    
    # Verifica que data no esté vacío y que contenga el primer elemento
    if data and isinstance(data, list) and len(data) > 0 and 'results' in data[0]:
        results = data[0]['results']  # Acceder al primer elemento de la lista
        
        # Verifica que haya filas en los resultados
        if results['rows']:
            return results['rows']  # Devuelve las filas directamente como una lista de listas

    return []  # Si no hay resultados, devuelve una lista vacía

def insert_product(data):
    sql = f""" INSERT INTO ProductsV2 (Id_producto, Nombre, Cantidad, Precio_ingreso, Precio, Ganancia, Proveedor) 
    VALUES(?,?,?,?,?,?,?)"""

    try:
        # Ejecutar la consulta usando la función de turso
        insert_success = query_turso2(sql, data)
        if insert_success:
            print("Producto insertado correctamente.")
            return True
        else:
            print("Error al insertar el producto.")
    except Error as e:
        print("Error inserting product: " + str(e))
        return False  # Devolver False en caso de error
    
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
        # Ejecutar la consulta usando la función de turso
        insert_success = query_turso2(sql, data)
        if insert_success:
            print("Producto actualizado correctamente.")
            return True
        else:
            print("Error al actualizar el producto.")
    except Error as e:
        print("Error Updating product: " + str(e))
        return False  # Devolver False en caso de error
    
def update_qty_product(Id_producto, data):
    sql = f""" UPDATE ProductsV2 SET 
                                Cantidad = {data}
                WHERE Id_producto = {Id_producto}"""
    
    try:
        # Ejecutar la consulta usando la función de turso
        insert_success = query_turso(sql)
        if insert_success:
            print("Producto actualizado correctamente.")
            return True
        else:
            print("Error al actualizar el producto.")
    except Error as e:
        print("Error Updating product: " + str(e))
        return False  # Devolver False en caso de error