from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def mostrar_recursos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 *Recursos Disponibles:*\n"
        "[• Actividades para fomentar el respeto](https://www.storybook-app.com/es/actividades/actividades-para-trabajar-el-respeto-en-ninos)\n"
        "[• Información para padres y docentes](https://www.areahumana.es/bullying-escolar-acoso-escolar/)\n"
        "[• Prevención](https://www.youtube.com/watch?v=NG2McgF4lvM)\n"
        "[• Guía de Prevención](https://www.sanidad.gob.es/areas/promocionPrevencion/prevencionViolencia/infanciaAdolescencia/docs/Infografia_CoViNNA_promocion_buen_trato.pdf)\n"
        "[• Descargar protocolo completo](https://escuelalibredeviolencia.sep.gob.mx/storage/recursos/Gu%C3%ADa%20sintetica/6tsNF31FeZ-G_GUIA_SINTETICA_ACOSO.pdf)",
        parse_mode="Markdown"
    )