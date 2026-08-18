# RETO 8: PIEDRA, PAPEL O TIJERA
# Juega contra la máquina el clásico piedra, papel o tijera.
# REGLAS: la piedra vence a la tijera, la tijera vence al papel,
#         el papel vence a la piedra.
# El juego va por rondas y se lleva el marcador de victorias, derrotas
# y empates. Al final pregunta si quieres jugar otra ronda.
# EXTRA: haz que el juego termine cuando alguien llegue a 5 victorias.

import random


def opcion_maquina():
    return random.choice(["piedra", "papel", "tijera"])


def opcion_jugador():
    while True:
        eleccion = input("Elige: piedra, papel o tijera: ").lower()
        if eleccion in ["piedra", "papel", "tijera"]:
            return eleccion
        print("Opción no válida. Escribe piedra, papel o tijera.")


def quien_gana(jugador, maquina):
    reglas = {
        "piedra": "tijera",
        "papel": "piedra",
        "tijera": "papel",
    }
    if jugador == maquina:
        return "empate"
    if reglas[jugador] == maquina:
        return "jugador"
    return "maquina"


def mostrar_marcador(victorias, derrotas, empates):
    print("\n=== MARCADOR ===")
    print(f"Tú: {victorias} victorias | Máquina: {derrotas} | Empates: {empates}")


def sentirse_jugador():
    while True:
        respuesta = input("\n¿Jugar otra ronda? (s/n): ").lower()
        if respuesta in ["s", "si", "sí"]:
            return True
        if respuesta in ["n", "no"]:
            return False
        print("Responde 's' o 'n'.")


def jugar():
    victorias = 0
    derrotas = 0
    empates = 0

    print("=== PIEDRA, PAPEL O TIJERA ===")

    while True:
        jugador = opcion_jugador()
        maquina = opcion_maquina()

        print(f"\nTú elegiste: {jugador}")
        print(f"La máquina eligió: {maquina}")

        resultado = quien_gana(jugador, maquina)

        if resultado == "empate":
            print("¡Empate!")
            empates += 1
        elif resultado == "jugador":
            print("¡Ganaste esta ronda!")
            victorias += 1
        else:
            print("Perdiste esta ronda...")
            derrotas += 1

        mostrar_marcador(victorias, derrotas, empates)

        if not sentirse_jugador():
            print("\n¡Gracias por jugar!")
            break


jugar()