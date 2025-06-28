from datetime import datetime
from telegram import Update

def registrar_mensaje(update: Update):
    """Registra el mensaje del usuario con fecha y hora en un archivo .txt"""
    texto = update.message.text
    usuario = update.message.from_user.username or update.message.from_user.first_name
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    registro = f"[{fecha_hora}] {usuario}: {texto}\n"

    with open("mensajes_usuarios.txt", "a", encoding="utf-8") as f:
        f.write(registro)
