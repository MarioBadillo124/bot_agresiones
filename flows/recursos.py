from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def mostrar_recursos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    botones = [
        [InlineKeyboardButton("Guía de Prevención", url="https://ejemplo.com/guia.pdf")],
        [InlineKeyboardButton("Video Educativo", url="https://youtube.com/ejemplo")],
    ]
    teclado = InlineKeyboardMarkup(botones)
    
    await update.message.reply_text(
        "📚 *Recursos Disponibles:*\n"
        "Elige un material para verlo:",
        reply_markup=teclado,
        parse_mode="Markdown"
    )