from telegram import Update
from telegram.ext import ContextTypes

async def mostrar_info_docentes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👩‍🏫 *Protocolo para Docentes:*\n\n"
        "1. **Interrumpir la agresión**\n"
        "2. **Aislar a los involucrados**\n"
        "3. **Reportar en el libro de incidencias**\n\n"
        "[Descargar protocolo completo](https://ejemplo.com/protocolo.pdf)",
        parse_mode="Markdown"
    )