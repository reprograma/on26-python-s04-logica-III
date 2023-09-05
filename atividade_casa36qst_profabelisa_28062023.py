# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo 
# usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e 
# final devem ser informados também pelo usuário, conforme exemplo abaixo:
# Montar a tabuada de: 5
# Começar por: 4
# Terminar em: 7
# Vou montar a tabuada de 5 começando em 4 e terminando em 7:
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35
# Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

tabuadade_esclh_usuario = int(input("Escolha o mutiplicando para montarmos sua tabuada: "))
multiplicador_esclh_inicio = int(input("Digite o número para iniciarmos? "))
multiplicador_esclh_termino = int(input("Agora escolha outro número para finalizarmos: "))

while multiplicador_esclh_inicio > multiplicador_esclh_termino:
    print("O mutiplicador inicial é maior que o mutiplicador final.Tente novamente!")

    multiplicador_esclh_inicio = int(input("Digite o número para iniciarmos? "))
    multiplicador_esclh_termino = int(input("Agora escolha outro número para finalizarmos: "))

for numb in range(multiplicador_esclh_inicio, multiplicador_esclh_termino +1):
    produto = tabuadade_esclh_usuario * numb
    print(f"{tabuadade_esclh_usuario} X {numb} = {produto}")

else:
    print("Sua tabuada chegou ao fim.")
