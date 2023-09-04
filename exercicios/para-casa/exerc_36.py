# Desenvolva um programa que faça uma tabuada de UM NUMERO QUALQUER INTEIRO que será digitado 
# PELO USUÁRIO, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor 
# inicial e final devem ser informados também pelo usuário.

numero = int(input("Insira um número para criar sua tabuada: "))

inicio_tabuada = int(input("Por qual número sua tabuada irá começar? "))

final_tabuada = int(input("Por qual número sua tabuada irá terminar? "))

for multiplicador_da_tabuada in range(inicio_tabuada, final_tabuada+1):
    print(f"{numero} x {multiplicador_da_tabuada} = {numero*multiplicador_da_tabuada}")
