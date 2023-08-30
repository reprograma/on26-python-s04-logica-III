numeros = []
par = []
impar = []

for i in range(20):
    numero = int(input(f"DIGITE O {i+1}º NUMERO (inteiro): "))
    numeros.append(numero)

    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print("Números digitados:", numeros)
print("Números pares:", par)
print("Números ímpares:", impar)








