from telegram import Update
from telegram.ext import ContextTypes

async def mostrar_acerca(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *Acerca de este Bot*\n\n"
        "📚 *Proyecto académico* desarrollado para la materia de *Ingeniería del Conocimiento*.\n"
        "El objetivo principal es apoyar la *prevención y atención de agresiones físicas* en entornos escolares.\n\n"
        "🛠️ *¿Qué puede hacer este bot?*\n"
        "• Informar sobre qué es una agresión y sus tipos.\n"
        "• Brindar guías de prevención y recursos para docentes y padres.\n"
        "• Permitir reportar incidentes o hacer denuncias anónimas.\n"
        "• Compartir contactos de emergencia.\n"
        "• Además, responde con chistes, clima y curiosidades para hacerlo más ameno.\n\n"
        "🌐 *Tecnologías utilizadas:*\n"
        "- Python + Telegram Bot API\n"
        "- OpenWeatherMap API (para el clima)\n"
        "- JokeAPI (para chistes)\n\n"
        "👨‍💻 *Desarrollado por:*\n"
        "• Badillo Rosas Mario Antonio\n"
        "• Gonzalez Mateo Keyla Amairany\n"
        "• Garibay Gamez Alan Yael\n"
        "• Hernandez Radilla Jose Angel\n"
        "• Popoca Popoca Martha Isabel\n"
        "• Rosario Landero Lizbeth\n"
        "• Torres Gonzalez Raul\n\n"
        "✅ Gracias por utilizar este bot. ¡Juntos podemos promover entornos escolares seguros!",
        parse_mode="Markdown"
    )
