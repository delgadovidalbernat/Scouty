import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def enviar_mensaje_chat(mensajes):
    """
    Función para enviar un historial de chat a OpenAI.
    :param mensajes: Lista de mensajes [{role: "user", content: "mensaje"}]
    """
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=mensajes
        )

        content = response.choices[0].message.content
        return content
    except Exception as e:
        print(f"Error en la llamada a OpenAI: {e}")
        return None
