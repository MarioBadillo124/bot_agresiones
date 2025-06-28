from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    ConversationHandler
)
from flows.reportar import (
    iniciar_reporte,
    manejar_lugar,
    manejar_hora,
    manejar_descripcion,
    confirmar_reporte,
    manejar_volver_menu,
    confirmar_agradecimiento,

    cancelar as cancelar_reporte,
    PREGUNTAR_LUGAR,
    PREGUNTAR_HORA,
    PREGUNTAR_DESCRIPCION,
    CONFIRMAR_REPORTE,
    PREGUNTAR_VOLVER_MENU
)
from flows.denuncia import (
    iniciar_denuncia, 
    recibir_descripcion, 
    confirmar_denuncia,
    manejar_volver_menu,
    cancelar as cancelar_denuncia,
    ESPERANDO_DESCRIPCION, 
    CONFIRMACION,
    PREGUNTAR_VOLVER_MENU
)


#Información

from telegram.ext import CommandHandler, CallbackQueryHandler

from flows.recursos import mostrar_recursos
from flows.emergencia import mostrar_emergencia
from flows.docentes import mostrar_info_docentes
from flows.acerca import mostrar_acerca
from flows.otras import manejar_otras_preguntas
from flows.abiertas_reportes import manejar_preguntas_abiertas
from flows.saludos import manejar_saludos, SALUDOS
from flows.registro_mensajes import registrar_mensaje
from flows.keywords_agresion import PALABRAS_CLAVE_AGRESION
from flows.informacion import manejar_consultas_info

from flows.recursos import mostrar_recursos
from flows.emergencia import mostrar_emergencia
from flows.docentes import mostrar_info_docentes
from flows.acerca import mostrar_acerca


TOKEN = "7957581596:AAHhS_M3yr7bzQtQ8UurwpdbQkbcuf1IAeA"

botones_principales = [
    ["🚨 Reportar Agresión", "📢 Denuncia Anónima"],
    ["📚 Recursos Educativos", "🆘 SOS Emergencia"],
    ["🏫 Info para Docentes", "ℹ️ Acerca del Bot"],
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    teclado = ReplyKeyboardMarkup(botones_principales, resize_keyboard=True)
    await update.message.reply_text(
        "👋 ¡Hola! Bienvenido al *Bot de Prevención de Agresiones en Escuelas*.\n\n"
        "🔍 Puedes preguntarme sobre:\n"
        "- ¿Qué es una agresión?\n"
        "- Tipos de agresión\n"
        "- Cómo prevenir agresiones\n"
        "- Qué hacer si soy testigo\n\n"
        "O usa los botones para:\n"
        "🚨 *Reportar una agresión*\n"
        "📢 *Enviar una denuncia anónima*\n"
        "📚 *Consultar recursos educativos*\n"
        "🆘 *Pedir ayuda urgente*",
        reply_markup=teclado,
        parse_mode="Markdown"
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    registrar_mensaje(update)
    texto = update.message.text.lower()

  
    if any(palabra in texto for palabra in ["recursos educativos","recursos", "educativos", "educacion", "material", "aprendizaje"]):
        await mostrar_recursos(update, context)
    elif any(p in texto for p in ["SOS Emergencia","sos", "emergencia", "ayuda", "urgente"]):
        await mostrar_emergencia(update, context)
    elif any(p in texto for p in ["Info para Docentes","info docente", "docente", "docentes", "información docente", "informacion docente", "profesores", "maestros"]):
        await mostrar_info_docentes(update, context)
    elif any(p in texto for p in ["acerca del bot", "acerca", "quién eres", "quien eres", "información del bot", "informacion del bot","bot","sobre ti"]):

        await mostrar_acerca(update, context)
    elif "reportar" in texto:
        await iniciar_reporte(update, context)
    else:
        contiene_saludo = any(s in texto for s in SALUDOS)
        contiene_agresion = any(a in texto for a in PALABRAS_CLAVE_AGRESION)

        if contiene_saludo and contiene_agresion:
            await update.message.reply_text(
                "👋 ¡Hola! Gracias por escribir.\n\n"
                "🚨 Detecté que mencionaste una posible agresión.\n"
                "🔔 Si es urgente, avisa a un docente ahora mismo.\n"
                "📝 También puedes usar el botón 🚨 *Reportar Agresión* o escribir *reportar* para iniciar.",
                parse_mode="Markdown"
            )
            return

        respondio_abierta = await manejar_preguntas_abiertas(update, context)
        if respondio_abierta:
            return

        respondio_saludo = await manejar_saludos(update, context)
        if respondio_saludo:
            return

        respondio_info = await manejar_consultas_info(update, context)
        if not respondio_info:
            await manejar_otras_preguntas(update, context)

def main():
    app = Application.builder().token(TOKEN).build()

    reporte_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex("^🚨 Reportar Agresión$"), iniciar_reporte)],
        states={
            PREGUNTAR_LUGAR: [MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_lugar)],
            PREGUNTAR_HORA: [MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_hora)],
            PREGUNTAR_DESCRIPCION: [MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_descripcion)],
            CONFIRMAR_REPORTE: [MessageHandler(filters.TEXT & ~filters.COMMAND, confirmar_reporte)],

            PREGUNTAR_VOLVER_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_volver_menu)],
        },
        fallbacks=[CommandHandler("cancelar", cancelar_reporte)],
        allow_reentry=True
    )

    denuncia_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex("^📢 Denuncia Anónima$"), iniciar_denuncia)],
        states={
            ESPERANDO_DESCRIPCION: [MessageHandler(filters.TEXT & ~filters.COMMAND, recibir_descripcion)],
            CONFIRMACION: [MessageHandler(filters.TEXT & ~filters.COMMAND, confirmar_denuncia)],
            PREGUNTAR_VOLVER_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_volver_menu)],
        },
        fallbacks=[CommandHandler("cancelar", cancelar_denuncia)],
    )

    app.add_handler(reporte_handler)
    app.add_handler(denuncia_handler)
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == "__main__":
    main()
