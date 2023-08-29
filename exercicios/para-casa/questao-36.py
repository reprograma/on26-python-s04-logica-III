#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário. 
#A tabuada não deve necessariamente iniciar em 1 e terminar em 10. O valor inicial e final devem ser informados também pelo usuário.
#Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.


valor_fixo = int(input('Voce quer a tabuada de qual número, amigue? '))
valor_inicial =  int(input(f'Vamos começar multiplicando {valor_fixo} por qual número? '))
valor_final =  int(input(f'Vamos terminar multiplicando {valor_fixo} por qual número? '))

if valor_final < valor_inicial:
    print('Ops, nossa tabuada só apresenta valores em ordem crescente, amigue. O primeiro multiplicador precisa ser maior do que o último. :)')
    
for multiplicador in range(valor_inicial, valor_final+1, 1):
    print(f'{valor_fixo} x {multiplicador} = {valor_fixo * multiplicador}')