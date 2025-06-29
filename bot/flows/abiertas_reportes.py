# flows/abiertas_reportes.py

import random
from telegram import Update
from telegram.ext import ContextTypes
from flows.texto import quitar_acentos

PALABRAS_CLAVE_AGRESION = [
    # AGRESIÓN (y errores con z, c, repeticiones)
    "agresion", "agresion fisica", "agresion emocional", "agrezion fizica", 
    "agredir", "agrediendo", "agredieron",
    "agrecion", "agreccion", "agrecciones",  # errores frecuentes
    "agrezion", "agreziones", "agreciones", "agrezion fisica",

    # PELEAS
    "pelea", "peleas", "pelear", "peleando", "pelearon",
    "pleito", "bronca", "se pelearon", "se andan peleando",

    # SLANG golpes
    "madrazos", "trancazos", "trancasos", "se agarraron a madrazos", 
    "se agarraron a trancazos", "se agarraron", "se armaron los golpes",
    "se andan dando", "se dieron con todo", "andan de pleito", "se traen bronca",

    # GOLPES y variantes con z
    "golpes", "golpez", "golpe", "golpiar", "golpiaron", "golpeando", "golpearon",
    "golpio", "golpiando", "golpizaron", "golpizando",

    # PEGAR
    "pegan", "pegando", "pega", "pegon", "pegandole",
    "le pegaron", "lo estan pegando", "le estan pegando", "me pego",

    # EMPUJAR
    "empujar", "empujando", "empujones", "empujon", "empujaron",
    "empujoncito", "empujonesitos",

    # LASTIMAR / HERIR
    "lastimar", "lastimaron", "lastimando", "lastimado", "lastimada", "lastimo",
    "herir", "hiriendo", "herido", "herida", "lo hirieron", "la hirieron", "me hirieron",

    # VIOLENCIA
    "violencia", "violento", "violenta", "lo estan violentando", "violentiaron",

    # ABUSO
    "abuso", "abusando", "abusaron", "abusador", "abusadora", "abuson", "abusona",

    # MOLESTAR / BURLAS
    "molestar", "molestando", "molestaron", "me estan molestando", "me molestan", "me molesta",
    "burlando", "burlas", "se burlan", "burlandose", "burlarse",

    # AMENAZAS
    "amenaza", "amenazas", "amenazando", "me amenazo", "amenazo",

    # PATEAR y otros golpes
    "patear", "pateando", "patadas", "patearon", "patiaron",
    "cachetadas", "arañazos", "manotazos",

    # FRASES COMPLETAS
    "tiraron al piso", "lo empujaron", "lo tiraron", "le dieron un golpe",
    "lo estan golpeando", "estan peleando", "vi una pelea", "acabo de ver una agresion",
    "estan agrediendo a alguien", "vi que lo empujaron", "vi que le pegaron",
    "hay una pelea", "alguien esta pegando", "hay violencia", "hay una pelea en el salon"
]



RESPUESTAS_AGRESION = [
    "🚨 Parece que estás describiendo una situación de agresión. Si es urgente, avisa a un docente de inmediato. También puedes usar el botón 🚨 *Reportar Agresión*.",
    "🆘 Gracias por reportarlo. Puedes iniciar un reporte presionando el botón 🚨 o escribiendo *reportar* para dar más detalles.",
    "📍 Si viste una pelea o agresión, es importante dejar constancia. ¿Quieres iniciar un reporte? Usa el botón 🚨.",
    "✋ Si te sientes inseguro o presencias una agresión, aléjate y avisa a un adulto. Yo también puedo ayudarte a reportarlo.",
]

RESPUESTAS_QUE_HAGO = [
    "📌 Si no sabes qué hacer ante una agresión, lo primero es mantener la calma y buscar a un adulto responsable.",
    "🧠 Es buena idea reportar lo que viste para que el equipo escolar pueda actuar. Pulsa 🚨 o dime *reportar*.",
    "👁️‍🗨️ Describe lo que está pasando o pasó. Puedo ayudarte a armar un reporte formal.",
]

async def manejar_preguntas_abiertas(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    texto = quitar_acentos(update.message.text.lower())

    if any(p in texto for p in PALABRAS_CLAVE_AGRESION):
        await update.message.reply_text(random.choice(RESPUESTAS_AGRESION))
        return True
    
    elif any(p in texto for p in ["qué hago", "que hago", "q hago", "k hago", "q ago", "k ago", "que ago", "que hajo", "qe hago", "ke hago", "ayuda", "debo hacer", "cómo procedo", "que hago si veo", "qué hago si veo"]):
        await update.message.reply_text(random.choice(RESPUESTAS_QUE_HAGO))
        return True
    
    return False  # No respondió nada

