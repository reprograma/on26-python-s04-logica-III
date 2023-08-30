# Resolução exercício para casa - Questão 36
# Link de acesso: https://wiki.python.org.br/EstruturaDeRepeticao

valor1 = int(input('Montar a tabuada de: '))
valor2 = int(input('Começar por: '))
valor3 = int(input('Terminar em: '))

if valor2 <= valor3:
    print('Aguarde, estamos trabalhando na sua tabuada!')
else:
    print('Por favor, digite um valor final maior ou igual que o valor inicial')

for c in range(valor2, valor3 +1):
    print('{} x {:2} = {}'.format(valor1, c, valor1*c))