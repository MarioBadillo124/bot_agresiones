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

# Nuevas listas para agradecimientos y despedidas
AGRADECIMIENTOS = ["gracias", "muchas gracias", "te lo agradezco", "agradecido", "agradecida"]
RESPUESTAS_AGRADECIMIENTO = [
    "¡De nada! Estoy aquí para ayudarte. 😊",
    "No hay de qué, ¡espero que la información te sea útil!",
    "¡Gracias a ti por usar el bot! Si necesitas algo más, aquí estoy.",
    "Siempre a tu disposición. Si tienes más preguntas, no dudes en preguntar."
]
DESPEDIDAS = ["adiós", "hasta luego", "nos vemos", "chao", "bye", "hasta pronto"]
RESPUESTAS_DESPEDIDA = [
    "👋 ¡Hasta luego! Recuerda que estoy aquí si necesitas ayuda.",
    "Cuídate mucho. Si ves algo preocupante, no dudes en reportarlo.",
    "¡Adiós! Espero que tengas un buen día. 😊",
    "Hasta pronto. Aquí estaré si necesitas más información."
]

async def manejar_saludos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    texto = update.message.text.lower()

    if any(s in texto for s in SALUDOS):
        await update.message.reply_text(random.choice(RESPUESTAS_SALUDO))
        return True
    
    if any(p in texto for p in PREGUNTAS_ESTADO):
        await update.message.reply_text(random.choice(RESPUESTAS_ESTADO))
        return True
    if any(a in texto for a in AGRADECIMIENTOS):
        await update.message.reply_text(random.choice(RESPUESTAS_AGRADECIMIENTO))
        return True
    if any(d in texto for d in DESPEDIDAS):
        await update.message.reply_text(random.choice(RESPUESTAS_DESPEDIDA))
        return True
    return False
