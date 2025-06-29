from telegram import Update
from telegram.ext import ContextTypes

async def mostrar_info_docentes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👩‍🏫 *Protocolo para Docentes:*\n\n"
        "1. **Interrumpir la agresión**\n"
        "2. **Aislar a los involucrados**\n"
        "3. **Reportar en el libro de incidencias**\n\n"
        "[Ver protocolo completo](https://escuelalibredeviolencia.sep.gob.mx/storage/recursos/Gu%C3%ADa%20did%C3%A1ctica%20acoso%20escolar/OeEqBwe67L-TODAS_Y_TODOS_CONTRA_EL_ACOSO_ESCOLAR_DIGITAL_27_AGOSTO.pdf)\n"
        "[¿Cómo detectar violencia en las escuelas?](https://www.youtube.com/watch?v=NG2McgF4lvM)",
        parse_mode="Markdown"
    )