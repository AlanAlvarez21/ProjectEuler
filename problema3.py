def encontrar_primos(limite):
    # Crear una lista de números desde 0 hasta el límite
    numeros = [True] * (limite + 1)
    numeros[0] = numeros[1] = False  # 0 y 1 no son primos

    for num in range(2, int(limite ** 0.5) + 1):
        if numeros[num]:
            for multiple in range(num * num, limite + 1, num):
                numeros[multiple] = False

    # Crear la lista de números primos encontrados
    primos = [num for num in range(2, limite + 1) if numeros[num]]
    return primos

def factor_primo_mayor(lista_primos, numero):
    lista_factores_primos = []
    for i in lista_primos: 
        if numero % i == 0:
            lista_factores_primos.append(i)
    print(lista_factores_primos[-1])

factor_primo_mayor(encontrar_primos(10000000), 600851475143)
