numeros = [] 


for _ in range(20):
    numero = int(input("Digite um número: "))
    numeros.append(numero)


pares = []
impares = []
Todos_numeros_digitados = [ ]

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

Todos_numeros_digitados.append(numeros)

print("Você digitou os seguintes números:",Todos_numeros_digitados)
print("Números pares:", pares)
print("Números ímpares:", impares)

