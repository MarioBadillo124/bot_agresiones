from telegram import Update
from telegram.ext import ContextTypes

async def mostrar_acerca(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *Acerca de este Bot:*\n\n"
<<<<<<< HEAD
        "Propocito: Proyecto de la materia de Ingenieria del conocimiento\n"
=======
        "Proposito: Proyecto de la materia de Ingenieria del conocimiento\n"
>>>>>>> reportar
        "Creado para reportar agresiones en horarios de receso.\n\n"
        "Integrantes: ",
        parse_mode="Markdown"
    )