from clases.avanzadas import Avanzadas

def main():
    op = Avanzadas()

    while True:
        print("\n--- MENÚ ---")
        print("1. Raíz")
        print("2. Elevar potencia")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "3":
            print("Saliendo del programa...")
            break

        if opcion in ["1", "2"]:
            op.leerNumeros()

            if opcion == "1":
                op.raiz()
            elif opcion == "2":
                op.elevarPotencia()

            op.mostrarResultado() 
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
