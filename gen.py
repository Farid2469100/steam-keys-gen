import random

def generar_clave():
    caracteres = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    clave = ""
    for i in range(5):
        clave += random.choice(caracteres)
    clave += "-"
    for i in range(5):
        clave += random.choice(caracteres)
    clave += "-"
    for i in range(5):
        clave += random.choice(caracteres)
    return clave

def generar_claves(cantidad):
    claves = []
    for _ in range(cantidad):
        claves.append(generar_clave())
    return claves

# Ejemplo de uso:
cantidad_claves = 10
claves_generadas = generar_claves(cantidad_claves)

# Imprimir las claves generadas
for clave in claves_generadas:
    print(clave)