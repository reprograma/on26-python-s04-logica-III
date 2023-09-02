#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.


num_dado, num_pares, num_impares = [], [], [] #listas criadas para colocar os itens dentro

for num in range(20):
    numero = int(input(f"Digite o {num+1}º número inteiro: "))
    num_dado.append(numero)
    if numero % 2 == 0:
        num_pares.append(numero)
    else:
        num_impares.append(numero)

print("Total de números digitados:", num_dado)
print("Total de números pares:", num_pares)
print("Total de números números ímpares:", num_impares)
