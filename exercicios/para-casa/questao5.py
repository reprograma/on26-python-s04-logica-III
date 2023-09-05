''' 
Crie um programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor Par e os números impares no vetor Ímpar. Imprima os três valores.
'''
# Estabelecendo vetores para armazenar
numeros = []
numeros_par = []
numeros_impar = []

# Leitura dos 20 números inseridos e diferenciação entre par e ímpar 
for i in range(20):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)
    if numero % 2 == 0:
        numeros_par.append(numero)
    else:
        numeros_impar.append(numero)

# Impressão dos três vetores
print("Números digitados:", numeros)
print("Números pares:", numeros_par)
print("Números ímpares:", numeros_impar)
