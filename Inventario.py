# Lista de Objetos para un mini juego de RPG

Jugador = input("Cual es tu nombre de jugador?: ")

Inventario = input("Escribe tus objetos separados por coma: ")
Lista_Objetos = [objeto.strip() for objeto in Inventario.split(",")]  # Lista a partir de texto

while True:
    print("\n --INVENTARIO-- \n")
    print("1. Añadir Objeto")
    print("2. Usar Objeto")
    print("3. Ver Inventario")
    print("4. Salir")

    opcion = int(input("Elige una opcion (1 a 4): "))

    if opcion == 1:

        Nuevo_Objeto = input("Agrega un nuevo objeto: ")

        if Nuevo_Objeto in Lista_Objetos:
            print(f"{Nuevo_Objeto} ya está en el inventario")
        else:
            Lista_Objetos.append(Nuevo_Objeto)
            print(f"{Nuevo_Objeto} añadido al inventario")

    elif opcion == 2:

        Objeto_Usado = input("Que objeto quieres usar?: ")

        if Objeto_Usado in Lista_Objetos:
            Lista_Objetos.remove(Objeto_Usado)
            print(f"Usaste {Objeto_Usado}")
        else:
            print(f"{Objeto_Usado} no está en el inventario")

    elif opcion == 3:
        print(f"\n Tu inventario actual es: {Lista_Objetos} \n")

    elif opcion == 4:
        print(f"Saliendo del sistema... Hasta la próxima mi amigo {Jugador}!")
        break

    else:
        print("Opción inválida, intenta de nuevo.")