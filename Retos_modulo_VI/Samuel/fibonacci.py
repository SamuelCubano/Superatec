# RETO 4: SECUENCIA DE FIBONACCI
# La secuencia de Fibonacci empieza con 0 y 1, y cada número siguiente
# es la suma de los dos anteriores: 0, 1, 1, 2, 3, 5, 8, 13...
# Pide al usuario cuántos números quiere ver y muéstralos en una línea.
# Ejemplo (8 términos): 0 1 1 2 3 5 8 13

n = int(input("¿Cuántos números de Fibonacci quieres ver?: "))

a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()