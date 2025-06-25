def procesar_texto(texto, opciones):
    texto = texto.lower()
    for opcion in opciones:
        if opcion in texto:
            return opcion
    return None