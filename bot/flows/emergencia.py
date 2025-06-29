from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

async def mostrar_emergencia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    teclado = ReplyKeyboardMarkup(
        [[KeyboardButton("📍 Enviar mi ubicación", request_location=True)]],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await update.message.reply_text(
        "🆘 *Contactos de Emergencia:*\n\n"
        "• Policía Escolar: 555-1234\n"
        "• Director/a: 555-5678\n"
        "• Emergencias: 911\n\n"
        "✅ *Qué hacer mientras esperas ayuda:*\n"
        "- Aléjate del peligro si es posible.\n"
        "- Busca a un docente o adulto responsable.\n"
        "- No te enfrentes solo.\n\n"
        "🚨 *¡No guardes silencio!*\n"
        "Puedes enviar tu ubicación para que sepan dónde estás.",
        reply_markup=teclado,
        parse_mode="Markdown"
    )
