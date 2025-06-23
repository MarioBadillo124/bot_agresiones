# flows/abiertas_reportes.py

from telegram import Update
from telegram.ext import ContextTypes

# Lista de palabras clave que indican una posible agresión o necesidad de reporte
PALABRAS_CLAVE_AGRESION = [
    "agresión", "agresion", "pelea", "violencia", "golpes", "están peleando", 
    "pegando", "están peleando", "peleando", "agredir", "empujando"
]

async def manejar_preguntas_abiertas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()

    if any(palabra in texto for palabra in PALABRAS_CLAVE_AGRESION):
        await update.message.reply_text(
            "🚨 Parece que estás describiendo una situación de agresión.\n\n"
            "👉 Si la situación es urgente, contacta inmediatamente a un docente o responsable.\n"
            "📝 Si deseas dejar constancia, puedes usar el botón 🚨 *Reportar Agresión* del menú o escribir *reportar* para iniciar el proceso."
        )
    elif "qué hago" in texto or "que hago" in texto or "ayuda" in texto:
        await update.message.reply_text(
            "📌 Si estás viendo algo preocupante, puedes reportarlo con el botón 🚨 *Reportar Agresión*.\n"
            "Estoy aquí para ayudarte. Describe lo que ocurre o selecciona una opción del menú."
        )
    else:
        await update.message.reply_text(
            "🤖 No estoy seguro de cómo responder eso. Si estás presenciando una agresión, por favor descríbelo con más detalle o usa el botón 🚨."
        )
