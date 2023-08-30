
#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

def main():
    numeros = []
    pares = []
    impares = []

    # Lê 20 números inteiros
    contador = 0
    while contador < 20:
        #deverá ser usado while, para ler 20 numeros inteiros. O loop continua enquanto o contador for menor que 20
        
        numero = int(input(f"Digite o {contador + 1}º número: "))
        numeros.append(numero)
        contador += 1

    # Separa os números pares e ímpares
    # for - para verificar se cada numero é par (num %2 ==0) o que identifica se for par, add a lista pares
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    # Ordenação dos vetores
    #Sorted - para ordenar as listas pares e impares
    pares = sorted(pares)
    impares = sorted(impares)

    # Imprime os vetores
    print("Números digitados:", numeros)
    print("Números pares:", pares)
    print("Números ímpares:", impares)

