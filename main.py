def multiplica(x, y):
    return x * y

def run():
    print("\tMULTIPLICACIÓN DE DOS NÚMEROS")
    n1 = int(input("Ingresa el primer número a multiplicar: "))
    n2 = int(input("Ingresa el segundo número a multiplicar: "))
    print("El resultado de la multiplicación es: " + str(multiplica(n1, n2)))

if __name__ == "__main__":
    run()