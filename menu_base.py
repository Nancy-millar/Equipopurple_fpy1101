def datos_jhaimar():
    print("mi nombre es Jhaimar Altuve y tengo 25 años")
          
def datos_gretta():
    print("mi nombre es gretta ceballos y tengo 18 años")
    
def datos_nancy():
        print("Mi nombre es Nancy Millar y tengo 27 años")



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
        datos_nancy()
    elif op == "2":
        datos_gretta()  
    elif op == "3":
        datos_jhaimar()
    else:
        print(" Opción inválida.")
