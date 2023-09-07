# crie um código que imprima todos os números entre 0 e 10
for numero in range(0, 11, 1):
    print(numero)
print("fim do programa")

# crie um código que imprima todos os números inteiros entre 10 e 0
# como stop não pode ser menor que start
# precisamos usar o step negativo para subtrair 1 de 11 até chegar em 0
for numero in range(10, 0, -1):
    print(numero)
print("fim do programa")

#crie um código que imprima todos os números pares maiores de que 22 e menores que 68
for numeros_pares in range(24, 68, 2):
    print(numeros_pares)
print("fim do programa")

# crie um código que imprima a soma de todos os números entre 0 e 10
# precisamos definir a variável soma começando em 0
soma = 0
for numero in range(11):
    soma = soma + numero
print(soma)
print("fim do programa")

# crie um código que conte as letras do seu nome
# precisamos remover os espaços, podemos usar o replace que substitui o que existe por outra coisa
nome = "Carla Freitas"
print(len(nome.replace(" ", "")))
print("fim do programa")
