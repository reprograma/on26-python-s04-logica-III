#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
#Montar a tabuada de: 5
#Começar por: 4
#Terminar em: 7

#Vou montar a tabuada de 5 começando em 4 e terminando em 7:
#5 X 4 = 20
#5 X 5 = 25
#5 X 6 = 30
#5 X 7 = 35

## OBSERVAR SE O NUMERO DE INICIO É MENOR QUE O NUMERO DE TÉRMINO

n_da_tabuada = int(input("Digite um número que deseja calcular a tabuada dele:"))
n_de_inicio = int(input("Digite onde você quer que a tabuada comece:"))
n_de_parada = int(input("Digite até onde você quer que a tabuada termine:"))

if n_de_inicio >= n_de_parada:
    print ("Número de inicio deve ser menor que o numero que termina")
else:
     while (n_de_inicio < (n_de_parada+1)):

        print("%d x %d = %d" % (n_da_tabuada, n_de_inicio, n_da_tabuada*n_de_inicio))
        n_de_inicio = n_de_inicio +1