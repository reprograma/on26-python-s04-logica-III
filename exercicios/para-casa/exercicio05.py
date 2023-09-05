numeros = []
par = []
impar = []

for valor in range(20):
    numero = int(input("Digite 20 números em sequência: "))
    numeros.append(numero)

    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)


print(numeros)
print(par)
print(impar)