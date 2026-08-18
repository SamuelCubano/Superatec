# RETO 6: EL AHORCADO
# El programa elige una palabra secreta y el jugador debe adivinarla
# letra por letra antes de quedarse sin vidas (6 en total).
# Cada error dibuja una parte del ahorcado.
# EXTRA: agrega más palabras secretas a la lista.

import random


def elegir_palabra():
    palabras = [
        "python", "programacion", "computadora", "teclado", "pantalla",
        "mouse", "internet", "codigo", "algoritmo", "variable",
        "funcion", "ciclo", "condicion", "lista", "diccionario"
    ]
    return random.choice(palabras)


def dibujar_ahorcado(vidas):
    dibujos = [
        """
    +-----+
    |     |
    |
    |
    |
   _|_
""",
        """
    +-----+
    |     |
    |     O
    |
    |
   _|_
""",
        """
    +-----+
    |     |
    |     O
    |     |
    |
   _|_
""",
        """
    +-----+
    |     |
    |     O
    |    /|
    |
   _|_
""",
        """
    +-----+
    |     |
    |     O
    |    /|\\
    |
   _|_
""",
        """
    +-----+
    |     |
    |     O
    |    /|\\
    |    /
   _|_
""",
        """
    +-----+
    |     |
    |     O
    |    /|\\
    |    / \\
   _|_
"""
    ]
    return dibujos[vidas]


def jugar():
    secreta = elegir_palabra()
    letras_adivinadas = []
    vidas = 6

    print("=== EL AHORCADO ===")
    print("Adivina la palabra secreta, una letra a la vez.\n")

    while vidas > 0:
        print(dibujar_ahorcado(vidas))
        print(f"Vidas restantes: {vidas}")

        progreso = ""
        for letra in secreta:
            if letra in letras_adivinadas:
                progreso += letra + " "
            else:
                progreso += "_ "
        print("Palabra: " + progreso)

        if "_" not in progreso:
            print(f"\n¡Ganaste! La palabra era: {secreta}")
            return

        letra = input("Escribe una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Solo se acepta UNA letra. Intenta de nuevo.\n")
            continue

        if letra in letras_adivinadas:
            print("Esa letra ya la usaste. Intenta con otra.\n")
            continue

        letras_adivinadas.append(letra)

        if letra in secreta:
            print(f"¡Bien! La letra '{letra}' está en la palabra.\n")
        else:
            vidas -= 1
            print(f"¡Uy! La letra '{letra}' no está. Pierdes una vida.\n")

    print(dibujar_ahorcado(vidas))
    print(f"¡Perdiste! La palabra era: {secreta}")


jugar()