# Resolucao do exercicio 36 (https://wiki.python.org.br/EstruturaDeRepeticao)
# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado 
# pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10,
# o valor inicial e final devem ser informados também pelo usuário, conforme ex abaixo:

# Montar a tabuada de:
# Começar por:
# Terminar em:

# Obs: Você deve verificar se o usuário não digitou o final menor que o inicial. 

tabuada_de = int(input("Montar a tabuada de: "))
inicio = int(input("Começar por: "))
final = int(input("Terminar em: "))

if inicio < final: #para que o número de início seja menor que o final
    for tabuada in range(inicio * tabuada_de, (final+1) * tabuada_de, tabuada_de):  
        print("%d x %d = %d" % (tabuada_de, inicio, tabuada))
        inicio = inicio + 1
else:
    print("ATENÇÃO: o número de término deve ser maior que o início!")
