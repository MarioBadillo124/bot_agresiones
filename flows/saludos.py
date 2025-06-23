# flows/saludos.py

import random
from telegram import Update
from telegram.ext import ContextTypes

# Lista de saludos y respuestas
SALUDOS = ["hola", "buenos días", "buenas tardes", "buenas", "hey", "holi", "saludos", "que tal", "holaaa"]

RESPUESTAS_SALUDO = [
    "👋 ¡Hola! Bienvenido al bot de prevención de agresiones. ¿En qué puedo ayudarte?",
    "😊 ¡Hola! Estoy aquí para ayudarte a reportar o informarte sobre agresiones en escuelas.",
    "¡Hola! Puedes escribirme cosas como 'quiero reportar algo' o usar los botones del menú 👇",
    "Hola 👋 ¿Has visto algo preocupante? Puedo ayudarte a reportarlo o darte recursos."
]

PREGUNTAS_ESTADO = ["cómo estás", "como estas", "cómo te encuentras", "todo bien", "que haces"]

RESPUESTAS_ESTADO = [
    "😊 Estoy bien, gracias por preguntar. ¿Tú cómo estás?",
    "Estoy aquí para ayudarte con lo que necesites sobre situaciones escolares.",
    "Muy bien, ¡gracias! Listo para ayudarte si viste algo preocupante.",
    "💪 Estoy funcionando bien. ¿Te gustaría reportar algo o necesitas información?"
]

async def manejar_saludos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    texto = update.message.text.lower()

    if any(s in texto for s in SALUDOS):
        await update.message.reply_text(random.choice(RESPUESTAS_SALUDO))
        return True
    
    if any(p in texto for p in PREGUNTAS_ESTADO):
        await update.message.reply_text(random.choice(RESPUESTAS_ESTADO))
        return True

    return False
