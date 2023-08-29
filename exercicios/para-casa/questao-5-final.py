#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
#Imprima os três vetores.

n = int(input('Vamos fazer uma lista com 20 números inteiros sequenciais. Qual será o primeiro número inteiro da lista? ')) 
n2 = n + 20
lista_completa = []
for numero in range(n,n2,1):
    lista_completa.append(numero)
print(f'Temos a nossa lista com todos os vinte números: {lista_completa}')

lista_completa_pares = []
for par in range(n,n2,1):
    if par % 2 == 0:
        lista_completa_pares.append(par)
print(f'Temos a nossa lista de números pares: {lista_completa_pares}')


lista_completa_impares = []
for impar in range(n,n2,1):
    if impar % 2 != 0:
        lista_completa_impares.append(impar)
print(f'Temos a nossa lista de números ímpares: {lista_completa_impares}')  

print(2*'-----------------------------------------------------------')
print(2*'-----------------------------------------------------------')


lista = range(1,20,1)

lista_completa = list(lista)
print(f'Temos a nossa primeira lista: {lista_completa}')

lista_pares = range(2,20,2)

lista_completa_pares = list(lista_pares)
print(f'Agora nossa lista só com os números pares: {lista_completa_pares}')

lista_impares = range(1,20,2)

lista_completa_impares = list(lista_impares)
print(f'Agora nossa lista só com os números ímpares: {lista_completa_impares}')

