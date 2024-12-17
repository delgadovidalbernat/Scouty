from apenai_chat import enviar_mensaje_chat
from api import obtener_token


def main():
    print("Obteniendo token de acceso...")
    token = obtener_token()
    if not token:
        print("Error: No se pudo obtener el token.")
        return
    print(f"Token obtenido: {token[:10]}... (truncado)")

    print("\nInteracción con OpenAI:")
    historial_chat = [
        {"role": "system", "content": "Eres un asistente útil."},
        {"role": "user", "content": "Hola, ¿cómo estás?"}
    ]

    respuesta = enviar_mensaje_chat(historial_chat)
    print(f"Respuesta de OpenAI: {respuesta}")

if __name__ == "__main__":
    main()
