import math

class Avanzadas:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.resultado = 0

    def leerNumeros(self):
        self.num1 = int(input("Número 1: "))
        self.num2 = int(input("Número 2: "))

    def raiz(self):
        if self.num1 >= 0:
            self.resultado = math.sqrt(self.num1)
        else:
            print("No se puede calcular la raíz de un número negativo.")

    def elevarPotencia(self):
        self.resultado = self.num1 ** self.num2

    def mostrarResultado(self):
        print(f"El resultado es: {self.resultado}")
