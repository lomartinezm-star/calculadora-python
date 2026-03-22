import operaciones
import historial

while True:
    print("\n--- CALCULADORA ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raíz")
    print("7. Historial")
    print("8. Salir")

    op = input("Opción: ")

    if op == "8":
        print("Saliendo...")
        break

    elif op == "7":
        historial.mostrar()
        continue

    a = float(input("Número 1: "))
    
    if op != "6":  # raíz solo usa un número
        b = float(input("Número 2: "))

    if op == "1":
        r = operaciones.sumar(a, b)
    elif op == "2":
        r = operaciones.restar(a, b)
    elif op == "3":
        r = operaciones.multiplicar(a, b)
    elif op == "4":
        r = operaciones.dividir(a, b)
    elif op == "5":
        r = operaciones.potencia(a, b)
    elif op == "6":
        r = operaciones.raiz(a)
    else:
        print("Opción inválida")
        continue

    print("Resultado:", r)
    historial.guardar(f"Resultado: {r}")
    