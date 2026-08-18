# Registro de estudiantes

# Entrada de datos

Nombre = input("¿Cómo te llamas?: ")

Edad = int(input("¿Qué edad tienes?: "))

Doble = Edad * 2  # Operación aritmética simple

Promedio = float(input("¿Cuál es tu promedio?: "))

Inscrito = input("¿Estás inscrito? (si / no): ").strip().lower()

Verdadero = Inscrito == "si"  # Comparación lógica

Materias = input("Escribe las materias separadas por coma: ")
List_Materias = [materia.strip() for materia in Materias.split(",")]  # Lista a partir de texto
Cantidad = len(List_Materias)

# Espaciado visual

print("\n-- RESUMEN --\n")

# Mostrar resultados

print(f"Nombre: {Nombre}")
print(f"Edad: {Edad}")
print(f"Promedio: {Promedio}")
print(f"¿Inscrito?: {Inscrito}")
print(f"Materias inscritas: {List_Materias}")
print(f"Total de materias: {Cantidad}")
print(f"Edad x2: {Doble}")

# Evaluación con condicional

if Promedio > 1.90:
    print("Estudiante Excelente")
else:
    print("Lo siento, sigue esforzándote")
