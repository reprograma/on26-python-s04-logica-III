#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa

numeros = []

for _ in range(10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    

print("Estes foram seus números: ", list(reversed(numeros)))