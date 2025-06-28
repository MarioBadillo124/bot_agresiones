from telegram import Update
from telegram.ext import ContextTypes

# Lista ampliada de palabras clave relacionadas con preguntas de información
PALABRAS_CLAVE_INFO = [
    "qué es una agresión", "que es una agresion", "tipos de agresión", "tipos de agresion",
    "consecuencias", "prevención", "prevenir", "testigo", "fui testigo", "vi una agresión",
    "información", "info", "agresión física", "violencia escolar", "leyes", "sanciones",
    "artículos legales", "consejo", "terapia", "psicología", "emocional", "apoyo emocional"
]

# Diccionario con respuestas
info_responses = {
    "qué es una agresión": (
        "📌 *¿Qué es una agresión física?*\n\n"
        "Es cualquier acto intencional que cause daño físico a otra persona. "
        "Incluye golpes, empujones, patadas, arañazos o cualquier otro contacto físico violento."
    ),
    "tipos de agresión": (
        "📌 *Tipos de agresión:*\n\n"
        "1. *Física:* Golpes, empujones, etc.\n"
        "2. *Verbal:* Insultos, burlas, amenazas\n"
        "3. *Psicológica:* Manipulación, exclusión\n"
        "4. *Cibernética:* Acoso por redes sociales"
    ),
    "consecuencias": (
        "📌 *Consecuencias de la agresión:*\n\n"
        "🔹 Para la víctima:\n- Daño físico\n- Ansiedad\n- Baja autoestima\n"
        "🔹 Para el agresor:\n- Problemas disciplinarios\n- Posibles consecuencias legales"
    ),
    "prevención": (
        "📌 *Prevención de agresiones:*\n\n"
        "✅ Fomentar el respeto mutuo\n"
        "✅ Educación emocional\n"
        "✅ Canales de denuncia accesibles\n"
        "✅ Supervisión en áreas comunes"
    ),
    "qué hacer si soy testigo": (
        "📌 *¿Qué hacer si soy testigo?*\n\n"
        "1. Mantén la calma\n"
        "2. Busca ayuda de un adulto\n"
        "3. No grabes ni compartas imágenes\n"
        "4. Ofrece apoyo a la víctima\n"
        "5. Reporta el incidente"
    ),
    "artículos legales": (
        "⚖️ *Aspectos legales:*\n\n"
        "Las agresiones en entornos escolares pueden estar sujetas a sanciones conforme a:\n"
        "- Artículo 6° y 7° de la Ley General de los Derechos de Niñas, Niños y Adolescentes\n"
        "- Código Penal del estado, en caso de agresiones físicas graves\n"
        "- Reglamento interno de la escuela"
    ),
    "consejo o terapia": (
        "💡 *Consejos de apoyo emocional:*\n\n"
        "- Habla con alguien de confianza\n"
        "- Respira profundamente y escribe cómo te sientes\n"
        "- Puedes acudir con el orientador escolar o psicólogo\n"
        "- Recuerda que pedir ayuda es valiente"
    )
}

# Manejador principal de consultas informativas
async def manejar_consultas_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()

    for clave, respuesta in info_responses.items():
        if clave in texto:
            await update.message.reply_text(respuesta, parse_mode="Markdown")
            return True  # Se encontró coincidencia

    for palabra in PALABRAS_CLAVE_INFO:
        if palabra in texto:
            await update.message.reply_text(
                "ℹ️ *¿Buscas información sobre agresiones?*\n\n"
                "Puedes preguntarme cosas como:\n"
                "- ¿Qué es una agresión?\n"
                "- Tipos de agresión\n"
                "- Cómo prevenir agresiones\n"
                "- Qué hacer si soy testigo\n"
                "- Qué leyes aplican\n"
                "- Cómo obtener ayuda emocional",
                parse_mode="Markdown"
            )
            return True

    return False  # No encontró coincidencia
