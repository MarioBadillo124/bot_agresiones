import requests
from datetime import datetime
import random
from telegram import Update
from telegram.ext import ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext
# --- Configuración de APIs ---
OPENWEATHER_API_KEY = "92f1b6e1392ebde583d2fa69d697d14b"  # Regístrate en https://openweathermap.org/api

# --- Funciones Utilitarias ---
def obtener_fecha_hora():
    """Devuelve fecha y hora actual formateada"""
    ahora = datetime.now()
    return {
        "fecha": ahora.strftime("%d/%m/%Y"),
        "hora": ahora.strftime("%H:%M:%S"),
        "dia_semana": ahora.strftime("%A").capitalize()  # Ej: "Lunes"
    }

# --- Funciones con APIs ---
def obtener_clima(ciudad="TuCiudad"):
    """Obtiene clima actual usando OpenWeatherMap"""
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={OPENWEATHER_API_KEY}&units=metric&lang=es"
        data = requests.get(url).json()
        clima = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        return f"🌤️ *Clima en {ciudad}:* {clima}, {temp}°C"
    except:
        return "⚠️ No pude obtener el clima. Intenta más tarde."

def obtener_chiste():
    """Obtiene un chiste aleatorio de JokeAPI"""
    try:
        respuesta = requests.get("https://v2.jokeapi.dev/joke/Any?lang=es").json()
        if respuesta["type"] == "single":
            return f"😄 *Chiste:*\n{respuesta['joke']}"
        else:
            return f"😄 *Chiste:*\n{respuesta['setup']}\n...\n{respuesta['delivery']}"
    except:
        chistes_locales = [
            "¿Qué hace un libro de matemáticas en la fiesta?\n¡Resolver problemas sociales!",
            "¿Cómo se llama el campeón de buceo de la escuela?\n*El subcampeón*, porque el primero nunca volvió."
        ]
        return f"😄 *Chiste:*\n{random.choice(chistes_locales)}"

# --- Respuestas Predefinidas ---
RESPUESTAS = {
    "clima": obtener_clima(),
    "chiste": obtener_chiste(),
    "hora": f"🕒 *Hora actual:* {obtener_fecha_hora()['hora']}",
    "fecha": f"📅 *Fecha:* {obtener_fecha_hora()['dia_semana']}, {obtener_fecha_hora()['fecha']}",
    "ayuda": (
        "ℹ️ *Puedes preguntarme:*\n\n"
        "- *Clima*: \"¿Qué clima hace?\"\n"
        "- *Chistes*: \"Cuéntame un chiste\"\n"
        "- *Hora*: \"¿Qué hora es?\"\n"
        "- *Fecha*: \"¿Qué día es hoy?\""
    )
}

# --- Manejador Principal ---
async def manejar_otras_preguntas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()
    
    if any(palabra in texto for palabra in ["clima", "tiempo", "temperatura"]):
        ciudad = "Chimalhuacán"  # Puedes personalizar la ciudad
        await update.message.reply_text(obtener_clima(ciudad), parse_mode="Markdown")
    
    elif any(palabra in texto for palabra in ["chiste", "broma", "reír"]):
        await update.message.reply_text(obtener_chiste(), parse_mode="Markdown")
    
    elif any(palabra in texto for palabra in ["hora", "horario"]):
        await update.message.reply_text(RESPUESTAS["hora"], parse_mode="Markdown")
    
    elif any(palabra in texto for palabra in ["fecha", "día", "calendario"]):
        await update.message.reply_text(RESPUESTAS["fecha"], parse_mode="Markdown")
    
    elif "ayuda" in texto:
        await update.message.reply_text(RESPUESTAS["ayuda"], parse_mode="Markdown")
    
    else:
        await update.message.reply_text(
            "❌ No entendí. Prueba con:\n"
            "- \"¿Qué clima hace?\"\n"
            "- \"Cuéntame un chiste\"",
            parse_mode="Markdown"
        )
        
    

def informacion(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("¿Qué es una agresión física?", callback_data='info_1')],
        [InlineKeyboardButton("Tipos de agresión", callback_data='info_2')],
        [InlineKeyboardButton("Consecuencias", callback_data='info_3')],
        [InlineKeyboardButton("Prevención", callback_data='info_4')],
        [InlineKeyboardButton("¿Qué hacer si soy testigo?", callback_data='info_5')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Selecciona un tema para más información:', reply_markup=reply_markup)

def mostrar_info(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    contenido = {
        'info_1': "📌 *¿Qué es una agresión física?*\n\nEs cualquier acto que cause daño físico, como empujones, golpes o patadas.",
        'info_2': "📌 *Tipos de agresión:*\n\n- Física\n- Verbal\n- Psicológica\n- Cibernética",
        'info_3': "📌 *Consecuencias:*\n\nLa víctima puede sufrir ansiedad, miedo, bajo rendimiento escolar y aislamiento.",
        'info_4': "📌 *Prevención:*\n\n- Fomentar el respeto\n- Supervisión constante\n- Intervención temprana",
        'info_5': "📌 *¿Qué hacer si soy testigo?*\n\n- Informar a un adulto\n- No quedarse callado\n- Ayudar si es seguro hacerlo",
    }

    query.edit_message_text(text=contenido.get(query.data, "Tema no encontrado."), parse_mode='Markdown')
