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
    cancelar as cancelar_reporte,
    PREGUNTAR_LUGAR,
    PREGUNTAR_HORA,
    PREGUNTAR_DESCRIPCION,
    CONFIRMAR_REPORTE
)
from flows.denuncia import (
    iniciar_denuncia, 
    recibir_descripcion, 
    confirmar_denuncia, 
    cancelar as cancelar_denuncia,
    ESPERANDO_DESCRIPCION, 
    CONFIRMACION
)
from flows.recursos import mostrar_recursos
from flows.emergencia import mostrar_emergencia
from flows.docentes import mostrar_info_docentes
from flows.acerca import mostrar_acerca
from flows.otras import manejar_otras_preguntas

TOKEN = "7957581596:AAHhS_M3yr7bzQtQ8UurwpdbQkbcuf1IAeA"

botones_principales = [
    ["🚨 Reportar Agresión", "📢 Denuncia Anónima"],
    ["📚 Recursos Educativos", "🆘 SOS Emergencia"],
    ["🏫 Info para Docentes", "ℹ️ Acerca del Bot"],
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    teclado = ReplyKeyboardMarkup(botones_principales, resize_keyboard=True)
    await update.message.reply_text(
        "¡Bienvenido al Bot de Prevención de Agresiones! Elige una opción:",
        reply_markup=teclado
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text
    
    if texto == "📚 Recursos Educativos":
        await mostrar_recursos(update, context)
    elif texto == "🆘 SOS Emergencia":
        await mostrar_emergencia(update, context)
    elif texto == "🏫 Info para Docentes":
        await mostrar_info_docentes(update, context)
    elif texto == "ℹ️ Acerca del Bot":
        await mostrar_acerca(update, context)
    else:
        await manejar_otras_preguntas(update, context)

def main():
    app = Application.builder().token(TOKEN).build()
    
    # Handler para REPORTES
    reporte_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex("^🚨 Reportar Agresión$"), iniciar_reporte)],
        states={
            PREGUNTAR_LUGAR: [MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_lugar)],
            PREGUNTAR_HORA: [MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_hora)],
            PREGUNTAR_DESCRIPCION: [MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_descripcion)],
            CONFIRMAR_REPORTE: [MessageHandler(filters.TEXT & ~filters.COMMAND, confirmar_reporte)],
        },
        fallbacks=[CommandHandler("cancelar", cancelar_reporte)],
        allow_reentry=True
    )
    
    # Handler para DENUNCIAS
    denuncia_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex("^📢 Denuncia Anónima$"), iniciar_denuncia)],
        states={
            ESPERANDO_DESCRIPCION: [MessageHandler(filters.TEXT & ~filters.COMMAND, recibir_descripcion)],
            CONFIRMACION: [MessageHandler(filters.TEXT & ~filters.COMMAND, confirmar_denuncia)],
        },
        fallbacks=[CommandHandler("cancelar", cancelar_denuncia)],
    )
    
    # Registra todos los handlers
    app.add_handler(reporte_handler)
    app.add_handler(denuncia_handler)
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    app.run_polling()

if __name__ == "__main__":
    main()
    