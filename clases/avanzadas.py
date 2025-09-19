import math

class Avanzadas:
    def __init__(self):
        self.num1 = 0
        self.resultado = 0
        
    def leerNumeros(self):
        while True:
            try:
                self.num1 = int(input("Número 1: "))
                break
            except Exception:
                print("Número inválido ")
                continue  
    
    def raiz(self):
        if self.num1 < 0:
            self.resultado = "No se puede calcular la raíz cuadrada de un número negativo."
        else:
            raiz = math.sqrt(self.num1)
            self.resultado = f"La raíz cuadrada de {self.num1} es {raiz}"

    def potencia(self):
        pass