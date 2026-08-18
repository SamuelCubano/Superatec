# RETO 7: CIFRADO CÉSAR
# Julio César enviaba mensajes secretos desplazando cada letra del alfabeto
# un número fijo de posiciones. Por ejemplo, con desplazamiento 3:
#   "hola" -> "krod"   (la 'o' retrocede hasta el final del alfabeto)
# Crea un programa con menú para CIFRAR o DESCIFRAR un mensaje.
# NOTA: solo se mueven las letras; espacios, números y signos no cambian.
# PISTA: usa ord() y chr() para convertir letras en números y viceversa.

def cifrar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            base = ord("a") if caracter.islower() else ord("A")
            posicion = (ord(caracter) - base + desplazamiento) % 26
            resultado += chr(base + posicion)
        else:
            resultado += caracter
    return resultado


def descifrar(texto, desplazamiento):
    return cifrar(texto, -desplazamiento)


def mostrar_menu():
    print("\n=== CIFRADO CÉSAR ===")
    print("1. Cifrar un mensaje")
    print("2. Descifrar un mensaje")
    print("3. Salir")


def pedir_mensaje():
    return input("Escribe el mensaje: ")


def pedir_desplazamiento():
    while True:
        try:
            valor = int(input("Desplazamiento (1-25): "))
            if 1 <= valor <= 25:
                return valor
            print("Debe ser un número entre 1 y 25.")
        except ValueError:
            print("Debe ser un número entero.")


def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mensaje = pedir_mensaje()
            desplazamiento = pedir_desplazamiento()
            print(f"Mensaje cifrado: {cifrar(mensaje, desplazamiento)}")

        elif opcion == "2":
            mensaje = pedir_mensaje()
            desplazamiento = pedir_desplazamiento()
            print(f"Mensaje descifrado: {descifrar(mensaje, desplazamiento)}")

        elif opcion == "3":
            print("¡Hasta la próxima!")
            break

        else:
            print("Opción no válida. Elige 1, 2 o 3.")


ejecutar()