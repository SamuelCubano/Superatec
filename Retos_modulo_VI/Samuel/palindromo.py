# RETO 1: PALÍNDROMO
# Un palíndromo es una palabra o frase que se lee igual de atrás hacia adelante.
# Ejemplos: "reconocer", "anita lava la tina", "somos".
# Pide al usuario una palabra y dile si es o no un palíndromo.
# PISTA: Python puede invertir un texto con texto[::-1]

palabra = input("Escribe una palabra: ").lower().replace(" ", "")

if palabra == palabra[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")