# RETO 3: CONTADOR DE VOCALES
# Pide al usuario una frase y cuenta cuántas veces aparece cada vocal (a, e, i, o, u).
# Muestra el resultado así:
#   a: 3
#   e: 1
#   i: 0
#   o: 2
#   u: 4
# EXTRA: también cuenta las consonantes.

frase = input("Escribe una frase: ").lower()
vocales = "aeiou"

for vocal in vocales:
    cantidad = frase.count(vocal)
    print(f"{vocal}: {cantidad}")