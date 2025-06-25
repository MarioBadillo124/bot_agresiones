from telegram import Update,ReplyKeyboardMarkup,ReplyKeyboardRemove
from telegram.ext import ContextTypes, ConversationHandler

# Estados del flujo
ESPERANDO_DESCRIPCION, CONFIRMACION, PREGUNTAR_VOLVER_MENU = range(3)

async def iniciar_denuncia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Inicia el flujo de denuncia anónima"""
    await update.message.reply_text(
        "✉️ *Denuncia Anónima*\n\n"
        "Por favor, describe lo ocurrido (sin mencionar nombres):\n"
        "• Lugar\n• Hora aproximada\n• Hechos\n\n"
        "Ejemplo: _'En el patio a las 12:30, un alumno empujó a otro'_",
        parse_mode="Markdown"
    )
    return ESPERANDO_DESCRIPCION

async def recibir_descripcion(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Guarda la descripción y pide confirmación"""
    context.user_data["descripcion"] = update.message.text
    await update.message.reply_text(
        "⚠️ *¿Confirmas enviar esta denuncia anónima?* (Sí/No)\n\n"
        f"*Descripción:*\n{update.message.text}",
        parse_mode="Markdown"
    )
    return CONFIRMACION

async def confirmar_denuncia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Procesa la confirmación"""
    if update.message.text.lower() in ["sí", "si", "yes"]:
        # Aquí podrías guardar en una base de datos
        await update.message.reply_text(
            "✅ *Denuncia anónima enviada.*\n"
            "Nadie verá tu identidad. Gracias por tu ayuda. *\n"
            "¿Deseas volver al menú principal?",
            reply_markup=ReplyKeyboardMarkup(
            [["Sí","sí", "si", "yes", "No", "no"]],
            one_time_keyboard=True,
            resize_keyboard=True
        )
        )
    return PREGUNTAR_VOLVER_MENU

async def manejar_volver_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja la decisión de volver al menú principal."""
    from mi_bot import botones_principales  # Importación local para evitar circularidad
    
    texto = update.message.text.lower()
    
    if any(p in texto for p in ["sí", "si", "volver"]):
        # Primero enviamos el mensaje de confirmación
        await update.message.reply_text(
            "Por favor esribe /start para reiniciar el bot.",
            reply_markup=ReplyKeyboardRemove()  # Limpiamos teclado actual
        )
        
    else:
        await update.message.reply_text(
            "De acuerdo. Puedes continuar con lo que necesites.",
            reply_markup=ReplyKeyboardRemove()
        )
    
    return ConversationHandler.END

async def cancelar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚫 Operación cancelada.")
    return ConversationHandler.END