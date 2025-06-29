from telegram import Update
from telegram.ext import ContextTypes

async def mostrar_acerca(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *Acerca de este Bot:*\n\n"
        "Proposito: Proyecto de la materia de Ingenieria del conocimiento\n"
        "Este bot fue creado para apoyar la prevención de agresiones en entornos escolares.\n"
        "Proporciona orientación, recursos e información útil.\n\n"
        "👨‍💻 Desarrollado por estudiantes comprometidos con la convivencia escolar.\n"
        "Integrantes: \n"
        " Badillo Rosas Mario Antonio\n"
        "• Gonzalez Mateo Keyla Amairany\n" 
        "• Garibay Gamez Alan Yael\n"
        "• Hernandez Radilla Jose Angel\n" 
        "• Popoca Popoca Martha Isabel\n"
        "• Rosario Landero Lizbeth\n"
        "• Torres Gonzalez Raul\n",
        parse_mode="Markdown"
    )