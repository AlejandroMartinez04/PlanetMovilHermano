from .connection import query_turso

def select_by_id(id):
    query = f"SELECT * FROM Persona WHERE usuario = '{id}';"
    data = query_turso(query)
    
    
    # Verifica que data no esté vacío y que contenga el primer elemento
    if data:
        info = parse_rows(data)
        results = info[0]  # Acceder al primer elemento de la lista
        if results:
            return results # Devuelve el diccionario
        else:
            print("Error enviando datos a la base de datos")

    return None  # Si no hay resultados, devuelve None

def parse_rows(response_json):
    try:
        rows = response_json["results"][0]["response"]["result"]["rows"]
        parsed = [
            [cell["value"] for cell in row]
            for row in rows
        ]
        return parsed
    except Exception as e:
        print("Error al procesar las filas:", e)
        return []