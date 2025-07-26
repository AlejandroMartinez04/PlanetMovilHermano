import os
import requests
import sys
from dotenv import load_dotenv

def resource_path(relative_path):
    """Devuelve la ruta absoluta de un recurso, empaquetado o no."""
    try:
        base_path = sys._MEIPASS  # Cuando está empaquetado
    except AttributeError:
        base_path = os.path.abspath(".")  # En desarrollo
    return os.path.join(base_path, relative_path)

env_path = resource_path(".env")

# Cargar variables de entorno
load_dotenv(dotenv_path=env_path)

TURSO_DB_AUTH_TOKEN = os.getenv("TURSO_DB_AUTH_TOKEN")
TURSO_DB_URL = os.getenv("TURSO_DB_URL")

def query_turso(query):
    headers = {
        "Authorization": f"Bearer {TURSO_DB_AUTH_TOKEN}",
        "Content-Type": "application/json"
    }
    
    body = {
            "requests": [
                {
                "type": "execute",
                "stmt": {
                    "sql": query,
                }
                }
            ]
        }

    
    try:
        response = requests.post(TURSO_DB_URL, headers=headers, json=body)
        if response.status_code == 200:
            print("Conexión a la base de datos exitosa", response.status_code)
            return response.json()  # Devuelve el resultado de la consulta
        else:
            print("Error en la consulta:", response.status_code, response.text)
            return None
    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud:", e)
        return None   

def query_turso2(query, data):
    headers = {
        "Authorization": f"Bearer {TURSO_DB_AUTH_TOKEN}",
        "Content-Type": "application/json"
    }
    
    body = {
            "requests": [
                {
                    "type": "execute",
                    "stmt": {
                        "sql": query,
                        "args": format_turso_args(data)
                    }
                }
            ]
        }
    
    try:
        response = requests.post(TURSO_DB_URL, headers=headers, json=body)
        if response.status_code == 200:
            result = response.json()
            results = result.get("results", [])

            if results and results[0].get("type") == "ok":
                print("Inserción a la base de datos exitosa", response.status_code)
                return True
            elif results and results[0].get("type") == "error":
                error_info = results[0].get("error", {})
                print("Error en la consulta SQL:", error_info.get("message", "Error desconocido"))
                return False
            else:
                print("Respuesta inesperada:", result)
                return False
        else:
            print("Error en la consulta:", response.status_code, response.text)
            return False
    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud:", e)
        return False
    

def format_turso_args(args):
    formatted = []
    for val in args:
        if isinstance(val, int):
            formatted.append({"type": "integer", "value": str(val)})
        elif isinstance(val, float):
            formatted.append({"type": "real", "value": str(val)})
        else:
            formatted.append({"type": "text", "value": str(val)})
    return formatted

