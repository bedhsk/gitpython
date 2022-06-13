# Función para realizar divisiones
def divide(x, y):
    return x / y

# Función principal del programa
def run():
    print("\tDIVISIÓN DE DOS NÚMEROS")
    n1 = int(input("Ingresa el primer número a dividir: "))
    n2 = int(input("Ingresa el segundo número a dividir: "))
    print("El resultado de la devisión es: " + str(divide(n1, n2)))

if __name__ == "__main__":
    run()
