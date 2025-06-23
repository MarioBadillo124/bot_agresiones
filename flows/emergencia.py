from telegram import Update
from telegram.ext import ContextTypes

async def mostrar_emergencia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🆘 *Contactos de Emergencia:*\n\n"
        "• Policía Escolar: 555-1234\n"
        "• Director/a: 555-5678\n"
        "• Emergencias: 911\n\n"
        "Envía tu ubicación para ayuda rápida.",
        parse_mode="Markdown"
    )