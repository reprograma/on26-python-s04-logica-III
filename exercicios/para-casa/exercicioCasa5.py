# Exercício 5 - Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

#Primeiro vamos criar os vetores de números ímpar e par vazios
vetor_par = []
vetor_impar = []

#Função para iterar a lista completa. Adicionei uma versão que imprime logo abaixo do número se ele é par ou não inicialmente, mas o enunciado pede que seja adicionado dentro de vetores.
def itera_lista(numeros_lista):
    for i in numeros_lista: #Iterando a lista pra ver se cada valor é par ou não
        # print(i) #Essa linha vai fazer a lista ser impressa de um jeito não ordenado
        if (i % 2 == 0): #Jeito mais fácil de checar se um número é impar ou par
            vetor_par.append(i) #Adicionando os valores pares à um array à parte
        else:
            vetor_impar.append(i) #Adicionando os valores impares em um array à parte
        
numeros_lista = [10,27,8,3,5,1,7,11,2,15,42,12,33,6,19,21,5,14,28,23]
#Agora vamos rodar a função e imprimir os valores
itera_lista(numeros_lista)
print(f"NÚMEROS LISTA: {numeros_lista}")
print(f"NÚMEROS PARES: {vetor_par}")
print(f"NÚMEROS IMPARES: {vetor_impar}")
