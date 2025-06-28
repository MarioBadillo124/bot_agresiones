# flows/abiertas_reportes.py

import random
from telegram import Update
from telegram.ext import ContextTypes

PALABRAS_CLAVE_AGRESION = [
    # Verbos comunes relacionados con agresión física o emocional
    "agresión", "agresion", "agredir", "agrediendo", "agredieron",
    "pelea", "peleas", "pelear", "peleando", "pelearon",
    "golpes", "golpe", "golpear", "golpeando", "golpearon",
    "pegan", "pegando","pega", "le pegaron", "lo están pegando", "le están pegando",
    "empujar", "empujando", "empujones", "empujón", "empujaron",
    "lastimar", "lastimaron", "lastimando", "lo lastimaron",
    "herir", "hiriendo", "herido", "herida",
    "violencia", "violento", "violenta", "lo están violentando",
    "abuso", "abusando", "abusaron", "abusador", "abusadora",
    "molestar", "molestando", "molestaron", "están molestando",
    "burlando", "burlas", "se burlan", "me están molestando",
    "amenaza", "amenazas", "amenazando", "me amenazó",
    "patear", "pateando", "patadas", "cachetadas", "arañazos", "manotazos",
    "tiraron al piso", "lo empujaron", "le dieron un golpe", "le pegaron", "me pegó",

    # Frases comunes o expresiones completas
    "lo están golpeando", "están peleando", "vi una pelea", "acabo de ver una agresión",
    "están agrediendo a alguien", "vi que lo empujaron", "vi que le pegaron", "hay una pelea",
    "alguien está pegando", "hay violencia", "hay una pelea en el salón"
]


RESPUESTAS_AGRESION = [
    "🚨 Parece que estás describiendo una situación de agresión. Si es urgente, avisa a un docente de inmediato. También puedes usar el botón 🚨 *Reportar Agresión*.",
    "🆘 Gracias por reportarlo. Puedes iniciar un reporte presionando el botón 🚨 o escribiendo *reportar* para dar más detalles.",
    "📍 Si viste una pelea o agresión, es importante dejar constancia. ¿Quieres iniciar un reporte? Usa el botón 🚨.",
    "✋ Si te sientes inseguro o presencias una agresión, aléjate y avisa a un adulto. Yo también puedo ayudarte a reportarlo.",
]

RESPUESTAS_QUE_HAGO = [
    "📌 Si no sabes qué hacer ante una agresión, lo primero es mantener la calma y buscar a un adulto responsable.",
    "🧠 Es buena idea reportar lo que viste para que el equipo escolar pueda actuar. Pulsa 🚨 o dime *reportar*.",
    "👁️‍🗨️ Describe lo que está pasando o pasó. Puedo ayudarte a armar un reporte formal.",
]

async def manejar_preguntas_abiertas(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    texto = update.message.text.lower()

    if any(p in texto for p in PALABRAS_CLAVE_AGRESION):
        await update.message.reply_text(random.choice(RESPUESTAS_AGRESION))
        return True
    
    elif any(p in texto for p in ["qué hago", "que hago", "ayuda", "debo hacer", "cómo procedo", "que hago si veo", "qué hago si veo"]):
        await update.message.reply_text(random.choice(RESPUESTAS_QUE_HAGO))
        return True
    
    return False  # No respondió nada

