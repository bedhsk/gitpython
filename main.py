# Función para realizar potencia de un número
def potencia(x):
    return x * x

# Función principal del programa
def run():
    print("\tPOTENCIA DE UN NÚMERO")
    n1 = int(input("Ingresa el número a potenciar: "))
    print("El resultado de la potenciación  es: " + str(potencia(n1)))

if __name__ == "__main__":
    run()
