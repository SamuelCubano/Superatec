# RETO 2: ADIVINA EL NÚMERO
# El programa elige un número aleatorio entre 1 y 100.
# El jugador intenta adivinarlo y recibe pistas: "muy alto" o "muy bajo".
# Cuando lo adivine, muestra cuántos intentos usó.
# EXTRA: limita los intentos a 10 y pierde si se acaban.

import random

secreto = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input("Adivina el número (1-100): "))
    intentos += 1

    if intento < secreto:
        print("Muy bajo... subele un poco")
    elif intento > secreto:
        print("Muy alto... bajale un poco")
    else:
        print(f"Correcto en {intentos} intentos")
        break