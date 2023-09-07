# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
# Imprima os três vetores.

# criamos as listas para armazenar os números a serem informados
lista_numeros = []
lista_pares = []
lista_impares = []

# utilizamos for para solicitar a entrada de dados com o range() para definir o tamanh da lista
for numero in range(4):
    #  utilizamos a função .append() para inserir as entradas na lista
    lista_numeros.append(int(input("Informe o número: ")))
    
# precisamos separar os valores nas listas pares e impares
# utilizamos for e condicionais para pegar esses grupos de valores e acrescentar nas respectivas listas
# utilizamos o resto do quocinete para saber se o número é par ou ímpar
for numero in lista_numeros:
    if (numero % 2 == 0):
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print(lista_numeros)
print(lista_pares)
print(lista_impares)
print("Fim do programa")