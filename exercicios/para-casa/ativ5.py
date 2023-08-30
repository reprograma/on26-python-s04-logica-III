numeros = []
pares = []
impares = []

for i in range(20):
    num = int(input(f'Digite o {i+1}º número: '))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print('Vetor de números:', numeros)
print('Vetor de números pares:', pares)
print('Vetor de números ímpares:', impares)