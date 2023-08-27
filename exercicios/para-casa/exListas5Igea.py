#Faça um Programa que leia 20 números inteiros e armazene-os numa lista.
#Armazene os números pares na lista PAR e os números IMPARES na lista impar.
#Imprima os três vetores.

print('Programa para gerar uma lista de 20 números inteiros e os separa em par e impar')

num20 = []
num20par = []
num20impar = []

while (len(num20)) < 20:
    num20.append(int(input('Informe um número inteiro: ')))
else:
    print('A lista já tem 20 itens,')

for num in num20:
    if num%2 == 0:
        num20par.append(num)
    elif num%2 != 0:
        num20impar.append(num)

print('os numeros pares são: ', num20par)
print('os numeros impares são: ', num20impar)
print('a lista completa com todos os números: ', num20)