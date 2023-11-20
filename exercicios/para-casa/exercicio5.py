# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
# Imprima os três vetores. 

lista_numeros = []
contagem = 0

while contagem < 20:
    numeros = int(input("Informe um número inteiro:"))
    contagem += 1
    lista_numeros.append(numeros)
print(lista_numeros)

lista_pares = [numero for numero in lista_numeros if numero % 2 == 0]
print(lista_pares)

lista_impares = [numero for numero in lista_numeros if numero % 2 != 0]
print(lista_impares)