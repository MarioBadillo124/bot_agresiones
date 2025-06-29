from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def mostrar_info_docentes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    botones = InlineKeyboardMarkup([
        [InlineKeyboardButton("📄 Protocolo PDF", url="https://www.gob.mx/cms/uploads/attachment/file/581927/Protocolo_de_Atencion_de_Violencia.pdf")],
        [InlineKeyboardButton("🎥 Video Capacitación", url="https://www.youtube.com/watch?v=UIKDdL8NR8I")],
        [InlineKeyboardButton("📝 Guía para Talleres", url="https://www.sep.gob.mx/work/models/sep1/Resource/2684/1/images/Guia_Taller_Convivencia.pdf")]
    ])
    await update.message.reply_text(
        "👩‍🏫 *Protocolo para Docentes:*\n\n"
        "1. 🚫 **Interrumpe la agresión con calma y autoridad.** Ej: \"¡Alto! Esto no está permitido.\"\n"
        "2. 🚶‍♂️ **Aísla a los involucrados en espacios distintos.**\n"
        "3. 📝 **Registra lo ocurrido escribiendo *reportar* o bien en el libro de incidencias.**\n"
        "4. 📞 **Informa a directivos y comunica a los padres o tutores.**\n"
        "5. 💬 **Da contención inicial a la víctima.**\n\n"
        "⚖️ *Recuerda:* Es tu responsabilidad legal y ética garantizar la seguridad del alumnado.\n\n"
        "Elige un recurso para reforzar tu formación:",
        reply_markup=botones,
        parse_mode="Markdown"
    )
    await update.message.reply_text(
        "💪 *Gracias por tu compromiso con un entorno seguro y respetuoso para todos los estudiantes.*",
        parse_mode="Markdown"
    )
