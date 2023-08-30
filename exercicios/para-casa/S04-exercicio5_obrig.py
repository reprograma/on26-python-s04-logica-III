#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR 
#e os números IMPARES no vetor impar. Imprima os três vetores.

lista = []
lista_par = []
lista_impar = []

while True:
    try:
        if len(lista) != 20:
            numero = int(input("Adicione um número positivo e inteiro à lista: "))
            if numero > 0:
                lista.append(numero)
            else:
                print("Número deve ser inteiro e positivo!")
            continue
        else:
            break
    except:
        print("Números devem ser inteiros e positivos!")


for num in lista:
    if (num % 2) == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)

print(f"Os números pares são: {lista_par}\nOs números ímpares são: {lista_impar}")