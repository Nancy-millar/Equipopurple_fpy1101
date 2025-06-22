def datos_gretta():
    print("mi nombre es gretta ceballos y tengo 18 años")

# Menú base del programa
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Función de integrante 1")
    print("2. Función de integrante 2")
    print("3. Función de integrante 3")
    print("0. Salir")
    op = input("Seleccione opción: ")

    if op == "0":
        print("Programa finalizado.")
        break
    elif op == "1":
        pass
    elif op == "2":
        datos_gretta  
    elif op == "3":
        pass # Aquí se llamará a la función del integrante 3
    else:
        print(" Opción inválida.")
