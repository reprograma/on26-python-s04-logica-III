#Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores.

#variaveis de listas que vão receber os números
numbers = []
even_numbers = []
odd_numbers = []

#vai analisar os numéros e ver se são impares ou pares
for i in range(20):
    number = int(input(f'Digite o {i} numero: '))
    numbers.append(number)
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

#printar os tipos de variaveis        
print(f'Os números são: {numbers}')
print(f'OS números pares são: {even_numbers}')
print(f'Os números ímpares são {odd_numbers}')