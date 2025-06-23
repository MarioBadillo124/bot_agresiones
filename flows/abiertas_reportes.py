# flows/abiertas_reportes.py

import random
from telegram import Update
from telegram.ext import ContextTypes

PALABRAS_CLAVE_AGRESION = [
    "agresión", "agresion", "pelea", "violencia", "golpes", "están peleando",
    "peleando", "agredir", "empujando", "pegando", "molestando", "abusando",
    "están molestando", "lastimaron", "amenazando", "burlando", "empujón", "empujones"
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

