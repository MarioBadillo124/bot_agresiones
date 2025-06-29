from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes, ConversationHandler
from datetime import datetime

ESPERANDO_DESCRIPCION, CONFIRMACION, PREGUNTAR_VOLVER_MENU = range(3)

async def iniciar_denuncia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["tiempo_denuncia"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    await update.message.reply_text(
        "✉️ *Denuncia Anónima*\n\n"
        "Por favor describe lo ocurrido (sin mencionar nombres):\n"
        "• Lugar\n• Hora aproximada\n• Qué sucedió\n\n"
        "_Ejemplo: 'En el patio a las 12:30, un alumno empujó a otro'_",
        parse_mode="Markdown"
    )
    return ESPERANDO_DESCRIPCION

async def recibir_descripcion(update: Update, context: ContextTypes.DEFAULT_TYPE):
    descripcion = update.message.text.lower()

    # Si el usuario respondió 'confirmar' tras un mensaje previo
    if descripcion.strip() in ["confirmar", "sí", "si", "yes"]:
        descripcion_guardada = context.user_data.get("descripcion", "Sin detalles previos.")
        await update.message.reply_text(
            f"⚠️ *¿Confirmas enviar esta denuncia anónima?* (Sí/No)\n\n"
            f"*Descripción:*\n{descripcion_guardada}",
            parse_mode="Markdown"
        )
        return CONFIRMACION

    # Si es la descripción inicial
    context.user_data["descripcion"] = descripcion

    if len(descripcion.split()) < 5:
        await update.message.reply_text(
            "✏️ Tu descripción es muy breve.\n"
            "¿Deseas agregar más detalles antes de enviarla? Si no, escribe 'confirmar' para enviarla así."
        )
        return ESPERANDO_DESCRIPCION

    await update.message.reply_text(
        f"⚠️ *¿Confirmas enviar esta denuncia anónima?* (Sí/No)\n\n"
        f"*Descripción:*\n{descripcion}",
        parse_mode="Markdown"
    )
    return CONFIRMACION


async def confirmar_denuncia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()
    if texto in ["sí", "si", "yes", "confirmar"]:
        # Aquí podrías guardar en una base de datos o enviar a un log
        await update.message.reply_text(
            "✅ *Denuncia anónima enviada.*\n"
            "Gracias por ayudar a que la escuela sea un lugar más seguro.\n\n"
            "🚨 *Recuerda:* Si ves que alguien corre peligro inmediato, busca a un docente o llama a emergencias (911).",
            parse_mode="Markdown"
        )

        # Preguntar si quiere hacer algo más
        await update.message.reply_text(
            "¿Deseas volver al menú principal o realizar otra denuncia?",
            reply_markup=ReplyKeyboardMarkup(
                [["Volver al menú", "Hacer otra denuncia"]],
                one_time_keyboard=True,
                resize_keyboard=True
            )
        )
        return PREGUNTAR_VOLVER_MENU
    else:
        await update.message.reply_text("✏️ Vamos a repetir el reporte desde el inicio.")
        return await iniciar_denuncia(update, context)

async def manejar_volver_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()
    from mi_bot import botones_principales

    if "volver" in texto:
        await update.message.reply_text(
            "Perfecto. Escribe /start para regresar al menú principal.",
            reply_markup=ReplyKeyboardRemove()
        )
    elif "otra" in texto:
        return await iniciar_denuncia(update, context)
    else:
        await update.message.reply_text(
            "De acuerdo. Puedes seguir escribiendo si necesitas algo más.",
            reply_markup=ReplyKeyboardRemove()
        )
    return ConversationHandler.END

async def cancelar_denuncia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚫 Operación cancelada.")
    return ConversationHandler.END
