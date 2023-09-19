# Questão 05 - Faça um programa que leia 20 números inteiros e armazene-os num vetor. Armazene os numeros pares no vetor Par e os numeros impares no vetor Ímpar. Imprima três vetores.

# vetores 
numeros = []
par = []
ímpar = []

for i in range(20):
    numero = int(input(f"Adicione o {i+1}º numero: "))
    numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0: 
       par.append(numeros)
    else:
       ímpar.append(numero)

print("numeros digitados:", numeros)
print("numeros pares:", par)
print("numeros impares:", ímpar)       

