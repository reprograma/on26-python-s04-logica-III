# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, 
# mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser 
# informados também pelo usuário, conforme exemplo abaixo:
#        Montar a tabuada de: 5
#        Começar por: 4
#        Terminar em: 7
#        Vou montar a tabuada de 5 começando em 4 e terminando em 7:
#        5 X 4 = 20
#        5 X 5 = 25
#        5 X 6 = 30
#        5 X 7 = 35
# Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

# definindo as variáveis a serem informadas pelo usuário

numero_tabuada = int(input("Montar a tabuada de: "))
inicio_tabuada = int(input("Começar por: "))
fim_tabuada = int(input("Terminar em: "))

# se o inicio da tabuada for menor ou igual ao fim da tabuada
# criamos uma sequência utilizando range()
# para cada número dentro desse intervalo multiplique pelo número da tabuada
if inicio_tabuada <= fim_tabuada:
    for numero in range(inicio_tabuada, fim_tabuada + 1): # somamos +1 para que o stop seja considerado parte da lista
        # utilizamos a interpolação de variável para apresentar o resultado
        print(f"{numero_tabuada} x {numero}: {numero_tabuada*numero}")
# se o fim da tabuada for menor que o início da tabuada o usuário será informado para tentar novamente
elif fim_tabuada < inicio_tabuada:
    print("O multiplicador não pode ser maior que o multiplicando.\nTente novamente!")

print("Fim do programa")