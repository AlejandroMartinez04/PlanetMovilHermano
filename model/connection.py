# import sqlite3
# from sqlite3 import Error

# def create_connection():

#     try:
#         conn = sqlite3.connect('databaseProducts.db')
#         return conn
#     except Error as e:
#         print("Error connecting to db: " + str(e))


### ------------------para db en la nube ------------------------#####

import os
import requests
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener la URL y el token de autenticación
TURSO_DB_URL = os.getenv("TURSO_DB_URL")
TURSO_DB_AUTH_TOKEN = os.getenv("TURSO_DB_AUTH_TOKEN")

def create_connection():
    return TURSO_DB_URL, TURSO_DB_AUTH_TOKEN

def query_turso(query):
    headers = {
        "Authorization": f"Bearer {TURSO_DB_AUTH_TOKEN}",
        "Content-Type": "application/json"
    }
    
    # Estructura correcta del cuerpo de la solicitud
    body = {
        "statements": [
            {
                "q": query
            }
        ]
    }
    
    response = requests.post(TURSO_DB_URL, headers=headers, json=body)
    
    if response.status_code == 200:
        return response.json()  # Devuelve el resultado de la consulta
    else:
        print("Error en la consulta:", response.status_code, response.text)
        return None    

def query_turso2(query, data):
    headers = {
        "Authorization": f"Bearer {TURSO_DB_AUTH_TOKEN}",
        "Content-Type": "application/json"
    }
    
    # Estructura correcta del cuerpo de la solicitud
    body = {
        "statements": [
            {
                "q": query,
                "params": data  # Agregar los argumentos de la consulta aquí
            }
        ]
    }
    
    response = requests.post(TURSO_DB_URL, headers=headers, json=body)
    
    if response.status_code == 200:
        return response.json()  # Devuelve el resultado de la consulta
    else:
        print("Error en la consulta:", response.status_code, response.text)
        return None