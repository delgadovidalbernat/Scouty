import json

import requests


def login(config_file):
    # Cargar credenciales desde el fichero de configuración
    try:
        with open(config_file, "r") as file:
            config = json.load(file)
            username = config["username"]
            password = config["password"]
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        print(f"Error al leer el archivo de configuración: {e}")
        return None

    # Configura el endpoint y los datos
    url = "https://scout.circutor.com/api/v2/user/login"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = {
        "username": username,
        "password": password
    }

    # Realizar la solicitud POST
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "OK":
                token = data["data"]["token"]
                print("Token Bearer obtenido con éxito:")
                print(f"Bearer {token}")
                return token
            else:
                print("Error en la respuesta del servidor:", data)
        else:
            print(f"Error en la solicitud: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error en la conexión: {e}")

    return None
