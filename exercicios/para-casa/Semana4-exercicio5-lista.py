# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os 
# números IMPARES no vetor impar. Imprima os três vetores.

# O programa tem que armazernar os 20 números, armazenar os pares e armazenar os impares. Imprimir os três valores
# Que leia 20 numeros inteiros = consegue entender 20 números inteiros aleatórios que forem inserido (?)

#Separar pares de impares

def pares_impares (listas):
    pares = []
    impares = []
    for valor in listas:
        if valor % 2 == 0:
         pares.append(valor)
    else:
        impares.append(valor)
    return pares, impares

numeros_inteiros = []
for n in range (20): #usei n só por frescura kk
    numeros = int(input(f"Digite o {n+1}º inteiro: "))
    numeros_inteiros.append(numeros)
pares, impares = pares_impares(numeros_inteiros)

#imprimindo as variáveis:

print("Os números digitados: ", numeros_inteiros)
print("Os números pares: ", pares)
print("Os números impares: ", impares)
