inteiros = []
pares = []
impares = []

for _ in range(20):
    numeros = int(input("Digite um número inteiro: "))
    inteiros.append(numeros)

    if numeros % 2 == 0:
        pares.append(numeros)
    else:
        impares.append(numeros)

print("Números digitados:", inteiros)
print("Números pares:", pares)
print("Números ímpares:",impares)