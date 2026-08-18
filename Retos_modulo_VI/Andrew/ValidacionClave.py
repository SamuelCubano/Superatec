# Crear una validacion de clave, pedir al usuario una clave, luego pedir que la confirme, si la clave no es igual,
# a la escrita anteriormente, entonces debe salir un mensaje que diga que la clave no es la correta, y si lo es,
# que imprima puedes pasar.

Clave = input("¿Cuál es tu clave?: ")

while True:
    
    Confirmacion = input("Repite la clave, por favor: ")

    if Confirmacion == Clave:
        print("Puedes pasar 😎")
        break

    else:
        print("La clave es incorrecta, por favor intenta de nuevo...")