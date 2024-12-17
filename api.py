import os

import requests
from dotenv import load_dotenv

load_dotenv()

def obtener_token():
    url = "https://scout.circutor.com/api/v2/user/login"
    payload = {
        "username": os.getenv("USERNAME"),
        "password": os.getenv("PASSWORD")
    }
    headers = {"Content-Type": "application/json", "accept": "application/json"}
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["data"]["token"] if data.get("status") == "OK" else None
    except Exception as e:
        print(f"Error al obtener el token: {e}")
        return None
