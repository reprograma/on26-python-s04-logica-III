# Damaris Santos
#Ex.05
#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.
#resolvido em grupo de estudos

inteiro = []
par = []
impar = []

for variavel_numero in range(20):
    numeros = int(input("Digite um número inteiro: "))
    inteiro.append(numeros)

    if numeros % 2 == 0:
        par.append(numeros)
    else:
        impar.append(numeros)

print("Números digitados:", inteiro)
print("Números pares:", par)
print("Números ímpares:",impar)
      
