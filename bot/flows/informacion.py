# flows/informacion.py

from telegram import Update
from telegram.ext import ContextTypes

async def manejar_consultas_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    texto = update.message.text.lower()

    if any(p in texto for p in [
        "qué es una agresión", "que es una agresion", "qué es agresion", "que es agresión",
        "violencia escolar", "bullying que es", "acoso escolar que es", "definicion agresion"
    ]):
        await update.message.reply_text(
            "📌 *¿Qué es una agresión física?*\n\n"
            "Es cualquier acto intencional que cause daño físico a otra persona. "
            "Incluye golpes, empujones, patadas, arañazos o cualquier otro contacto violento. "
            "También puede referirse a *bullying*, cuando ocurre repetidamente en un entorno escolar.",
            parse_mode="Markdown"
        )
        return True

    elif any(p in texto for p in [
        "tipos de agresion", "tipos de agresión", "formas de agresión", "clases de agresion",
        "tipos de violencia", "tipos bullying"
    ]):
        await update.message.reply_text(
            "📌 *Tipos de agresión:*\n\n"
            "1. *Física:* Golpes, empujones, patadas.\n"
            "2. *Verbal:* Insultos, burlas, amenazas.\n"
            "3. *Psicológica:* Manipulación, aislamiento, intimidación.\n"
            "4. *Cibernética:* Acoso en redes sociales o mensajes.\n"
            "5. *Sexual:* Conductas o comentarios inapropiados.\n"
            "6. *Bullying indirecto:* Rumores o exclusión social.",
            parse_mode="Markdown"
        )
        return True

    elif any(p in texto for p in [
        "prevencion", "prevenir", "cómo evitar", "como evitar", "evitar agresiones",
        "estrategias prevencion", "evitar bullying"
    ]):
        await update.message.reply_text(
            "🛡️ *Prevención de agresiones y bullying:*\n\n"
            "✅ Fomentar el respeto y la empatía.\n"
            "✅ Supervisar los espacios comunes en la escuela.\n"
            "✅ Educar en manejo de emociones y resolución pacífica.\n"
            "✅ Contar con canales claros para reportar agresiones.",
            parse_mode="Markdown"
        )
        return True

    elif any(p in texto for p in [
        "qué hacer si soy testigo", "que hago si veo", "fui testigo", "vi una agresion",
        "vi un golpe", "presencie una pelea", "presencie agresion"
    ]):
        await update.message.reply_text(
            "👀 *¿Qué hacer si eres testigo?*\n\n"
            "1. Mantén la calma y evalúa si hay peligro inmediato.\n"
            "2. Busca ayuda de un docente o adulto responsable.\n"
            "3. No grabes ni compartas imágenes del incidente.\n"
            "4. Apoya a la víctima y anímala a buscar ayuda.\n"
            "5. Reporta lo sucedido a través del bot o con autoridades escolares.",
            parse_mode="Markdown"
        )
        return True

    elif any(p in texto for p in [
        "ley", "articulo", "artículo", "código penal", "codigo penal", "legal", 
        "sanciones", "leyes escolares", "normas", "reglamento escolar"
    ]):
        await update.message.reply_text(
            "⚖️ *Aspectos legales y sanciones:*\n\n"
            "Las agresiones físicas pueden estar sujetas a sanciones según:\n"
            "- *Artículos 6° y 7°* de la Ley General de los Derechos de Niñas, Niños y Adolescentes.\n"
            "- *Código Penal del estado*, para lesiones graves o amenazas.\n"
            "- Reglamento interno de la escuela, que puede derivar en suspensiones o expulsiones.",
            parse_mode="Markdown"
        )
        return True

    elif any(p in texto for p in [
        "terapia", "emocional", "psicologo", "psicóloga", "apoyo emocional", "consejo",
        "orientacion", "como sentirme mejor", "ayuda emocional", "ansiedad", "estres"
    ]):
        await update.message.reply_text(
            "💡 *Consejos de apoyo emocional:*\n\n"
            "- Habla con alguien de confianza sobre lo que sientes.\n"
            "- Escribe tus emociones para entenderlas mejor.\n"
            "- Haz ejercicios de respiración o actividades que disfrutes.\n"
            "- Si persisten el estrés o ansiedad, acude a un psicólogo escolar o centro de salud.",
            parse_mode="Markdown"
        )
        return True

    elif any(p in texto for p in [
        "mi hijo sufre bullying", "mi hijo lo golpean", "como ayudar a mi hijo", 
        "mi hijo tiene miedo", "problemas en la escuela"
    ]):
        await update.message.reply_text(
            "👨‍👩‍👧 *Si eres padre o tutor:*\n\n"
            "- Escucha con calma y sin juzgar lo que tu hijo cuenta.\n"
            "- Asegúrale que no está solo y que juntos buscarán una solución.\n"
            "- Comunica la situación a los docentes o directivos.\n"
            "- Considera apoyo psicológico si notas cambios emocionales fuertes.",
            parse_mode="Markdown"
        )
        return True

    # Si no encontró coincidencias
    return False
