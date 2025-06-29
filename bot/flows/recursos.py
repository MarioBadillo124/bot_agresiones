from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def mostrar_recursos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    botones = [
        [InlineKeyboardButton("🎥 ¿Qué es el bullying? (Video)", url="https://www.youtube.com/watch?v=6jF71Z_dyxo")],
        [InlineKeyboardButton("🎥 Cómo prevenir agresiones (Video)", url="https://www.youtube.com/watch?v=nTRZIMfprBI")],
        [InlineKeyboardButton("📄 Guía PDF para padres y docentes", url="https://www.sep.gob.mx/work/models/sep1/Resource/7304/5/images/ViolenciaEscolar.pdf")]
    ]
    teclado = InlineKeyboardMarkup(botones)
    
    await update.message.reply_text(
        "📚 *Recursos educativos disponibles:*\n\n"
        "✅ Videos explicativos sobre bullying y cómo actuar.\n"
        "✅ Guías descargables para docentes y padres.\n\n"
        "Elige el recurso que quieras ver:",
        reply_markup=teclado,
        parse_mode="Markdown"
    )
