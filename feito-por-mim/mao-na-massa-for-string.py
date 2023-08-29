#Crie um código que imprima todos os número inteiros entre 0 e 10 
num = 0

while num <= 10:
    print(num)
    num += 1

print("Cabou aqui!")

#Crie um código que imprima todos os número inteiros entre 10 e 0 

num2 = 10

while num2 >= 0:
    print(num2)
    num2 -= 1

#Crie um código que imprima todos os número pares maiores do que 22 e menores do que 68

for num3 in range(24, 68, 2):
    print(num3)

print("Finalizado.")

#Crie um código que imprima a soma de todos os números entre 0 e 10 
soma = 0
for num4 in range(11):
    soma += num4

print("A soma dos números de 0 a 10 é:", soma)

#Crie um código que conte as letras do seu nome

nome = "Thaysa Pereira dos Reis Lima"

for quant in range(0, len(nome), 1):
    print(nome[quant])

print(nome)


meu_nome = "Thaysa Pereira dos Reis Lima"

print(len(meu_nome.replace(" ", "")))
print(len(meu_nome))
print(len(meu_nome))
print(meu_nome.replace(" ", ""))
