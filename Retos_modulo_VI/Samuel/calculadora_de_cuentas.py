def calcular_division_cuenta():
    print("=== CALCULADORA DE CUENTAS Y PROPINAS ===")
    
    # 1. Solicitar datos al usuario
    try:
        total_cuenta = float(input("Ingrese el monto total de la cuenta ($): "))
        porcentaje_propina = int(input("¿Qué porcentaje de propina desea dejar? (ej. 10, 15, 20): "))
        personas = int(input("¿Entre cuántas personas se va a dividir la cuenta?: "))
        
        # Validar que los valores sean lógicos
        if total_cuenta <= 0 or personas <= 0:
            print("❌ Error: El monto y el número de personas deben ser mayores a cero.")
            return

        # 2. Realizar los cálculos
        monto_propina = total_cuenta * (porcentaje_propina / 100)
        total_con_propina = total_cuenta + monto_propina
        pago_por_persona = total_con_propina / personas
        
        # 3. Mostrar el resumen formateado
        print("\n" + "="*35)
        print("         RESUMEN DE PAGO")
        print("="*35)
        print(f"• Consumo base:      ${total_cuenta:.2f}")
        print(f"• Propina ({porcentaje_propina}%):   ${monto_propina:.2f}")
        print(f"• Total a pagar:     ${total_con_propina:.2f}")
        print(f"• Total por persona: ${pago_por_persona:.2f}")
        print("="*35)

    except ValueError:
        print("❌ Error: Por favor, ingrese únicamente valores numéricos válidos.")

# Ejecutar la función
calcular_division_cuenta()