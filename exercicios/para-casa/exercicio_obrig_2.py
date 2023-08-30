# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

lista = [int(input("Insira o primeiro valor: ")), int(input("Insira o segundo valor: ")), int(input("Insira o terceiro valor: ")), \
         int(input("Insira o quarto valor: ")), int(input("Insira o quinto valor: ")), \
         int(input("Insira o sexto valor: ")), int(input("Insira o sétimo valor: ")), int(input("Insira o oitavo valor: ")), \
         int(input("Insira o nono valor: ")), int(input("Insira o décimo valor: ")), \
         int(input("Insira o décimo primeiro valor: ")), int(input("Insira o décimo segundo valor: ")), int(input("Insira o décimo terceiro valor: ")), \
         int(input("Insira o décimo quarto valor: ")), int(input("Insira o décimo quinto valor: ")), \
         int(input("Insira o décimo sexto valor: ")), int(input("Insira o décimo sétimo valor: ")), int(input("Insira o décimo oitavo valor: ")), \
         int(input("Insira o décimo nono valor: ")), int(input("Insira o vigésimo valor: "))]

numeros_pares = []
numeros_impares = []

for numero in lista:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else: numeros_impares.append(numero)

print("Números pares: ", sorted(numeros_pares))
print("Números ímpares: ", sorted(numeros_impares))
print("Lista: ", sorted(lista))

