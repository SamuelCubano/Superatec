# RETO 5: FIZZBUZZ
# Clásico de las entrevistas de programación.
# Recorre los números del 1 al 100 y:
#   - Si el número es múltiplo de 3, imprime "Fizz"
#   - Si es múltiplo de 5, imprime "Buzz"
#   - Si es múltiplo de ambos (3 y 5), imprime "FizzBuzz"
#   - Si no es ninguno, imprime el número
# PISTA: revisa la condición de FizzBuzz PRIMERO, antes que las demás.

for numero in range(1, 101):
    if numero % 15 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)