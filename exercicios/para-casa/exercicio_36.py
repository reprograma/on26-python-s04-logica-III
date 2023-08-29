#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
#Montar a tabuada de: 5
#Começar por: 4
#Terminar em: 7

#Vou montar a tabuada de 5 começando em 4 e terminando em 7:
#5 X 4 = 20
#5 X 5 = 25
#5 X 6 = 30
#5 X 7 = 35
#Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.'''

#variaveis que irão receber os números
first_num = int(input('Qual é a tabuada que você quer?'))
second_num = int(input('Qual é o número que você quer começar a tabuada?'))
third_num = int(input('Qual é o ultimo número Tabuada?'))
result = 0

#verificação caso o número final seja menor que o começo da tabuada
if third_num < second_num:
    print('Erro: O número de término deve ser maior ou igual ao número de início da Tabuada.')
else:
    print(f'Vou montar a tabuada de {first_num} começando em {second_num} e terminando em {third_num}:')

#imprime a tabuada
for num in range(second_num, third_num + 1):
    result = first_num * second_num
    print(f"\n{first_num}x{second_num} = {result}")
    second_num += 1

print("Fim da Tabuada")
