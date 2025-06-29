
from telegram import Update,ReplyKeyboardMarkup,ReplyKeyboardRemove

from telegram.ext import ContextTypes, ConversationHandler, MessageHandler, filters
from utils import procesar_texto
#from telegram import ReplyKeyboardMarkup

# Definimos los estados como constantes
PREGUNTAR_LUGAR, PREGUNTAR_HORA, PREGUNTAR_DESCRIPCION, CONFIRMAR_REPORTE, PREGUNTAR_VOLVER_MENU = range(5)

async def iniciar_reporte(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Inicia el flujo de reporte."""
    await update.message.reply_text(
        "📍 *¿Dónde ocurrió la agresión?*\n"
        "Ejemplos: _'Patio norte', 'Baños de primaria', 'Salón 5A'_",
        parse_mode="Markdown"
    )
    return PREGUNTAR_LUGAR

async def manejar_lugar(update: Update, context: ContextTypes.DEFAULT_TYPE):

    """Procesa la respuesta del lugar."""

    texto = update.message.text
    lugar = procesar_texto(texto, ["patio", "canchas", "baños", "salón", "comedor"])
    
    if lugar:
        context.user_data["lugar"] = lugar
        await update.message.reply_text(
            "⏰ *¿A qué hora ocurrió?*\nFormato: _'12:30 PM', 'Hace 10 minutos'_",
            parse_mode="Markdown"
        )
        return PREGUNTAR_HORA
    else:
        await update.message.reply_text(
            "❌ No reconozco ese lugar. Intenta con: _'patio', 'baños', 'salón'_",
            parse_mode="Markdown"
        )
        return PREGUNTAR_LUGAR  # Repite el estado actual

async def manejar_hora(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Procesa la respuesta de la hora."""
    context.user_data["hora"] = update.message.text
    await update.message.reply_text(
        "📝 *Describe lo ocurrido:*\nMenciona quiénes estaban involucrados y qué pasó.",
        parse_mode="Markdown"
    )
    return PREGUNTAR_DESCRIPCION

async def manejar_descripcion(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Procesa la descripción y pide confirmación."""
    context.user_data["descripcion"] = update.message.text
    resumen = (
        "📋 *Resumen del Reporte:*\n\n"
        f"📍 Lugar: {context.user_data['lugar']}\n"
        f"⏰ Hora: {context.user_data['hora']}\n"
        f"📝 Descripción: {update.message.text}\n\n"
        "¿Confirmas que esta información es correcta? (Sí/No)"
    )
    await update.message.reply_text(resumen, parse_mode="Markdown")
    return CONFIRMAR_REPORTE

async def confirmar_reporte(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Procesa la confirmación final."""
    if update.message.text.lower() in ["sí", "si", "yes"]:
        # Aquí puedes guardar en base de datos
        await update.message.reply_text(

            "✅ *Reporte enviado correctamente.*\nEl equipo escolar tomará acción.")
        # Preguntar si desea volver al menú
        await update.message.reply_text(
            "¿Deseas volver al menú principal?",
            reply_markup=ReplyKeyboardMarkup(
                [["Sí, volver al menú", "No, continuar"]],
                one_time_keyboard=True,
                resize_keyboard=True
            )
        )
        return PREGUNTAR_VOLVER_MENU
    else:
        await update.message.reply_text("✏️ Vamos a empezar de nuevo.")
        return await iniciar_reporte(update, context)

async def manejar_agradecimiento(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "¡Gracias por tu reporte! ¿Deseas volver al menú principal?",
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
    await update.message.reply_text("❌ Reporte cancelado.")
    return ConversationHandler.END

async def confirmar_agradecimiento(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    texto = update.message.text.lower()
    if texto == ["sí","Sí", "si", "yes"]:
        from ..mi_bot import botones_principales  # importa desde el archivo raíz
        await update.message.reply_text(
            "Regresando al menú principal...",
            reply_markup=ReplyKeyboardMarkup(botones_principales, resize_keyboard=True)
        )
    else:
        await update.message.reply_text("Entendido. Puedes escribirme cuando lo necesites.")
    return ConversationHandler.END

