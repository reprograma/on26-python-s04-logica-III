# Faça um Programa que leia 20 números inteiros e armazene-os num vetor
# Armazene os números pares no vetor PAR
# Os números IMPARES no vetor impar
# Imprima os três vetores

Numeros_inteiros = []
Numeros_pares = []
Numeros_impares = []

for Vetor in range(20):
    Vetor = int(input("Digite um número inteiro 20x: "))
    Numeros_inteiros.append(Vetor)
    
    if Vetor % 2 == 0:
        Numeros_pares.append(Vetor)
    else:
        Numeros_impares.append(Vetor)

print("Nº Inteiros: ", Numeros_inteiros)
print("Nº Pares: ", Numeros_pares)
print("Nº Impares: ", Numeros_impares)