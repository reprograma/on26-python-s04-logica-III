#Desenvolva um programa que faça a tabuada de um número qualquer
# inteiro que será digitado pelo usuário, mas a tabuada não deve 
# necessariamente iniciar em 1 e terminar em 10, o valor 
# inicial e final devem ser informados também pelo usuário, 
# conforme exemplo abaixo:
#Montar a tabuada de: 5
#Começar por: 4
#Terminar em: 7
#Vou montar a tabuada de 5 começando em 4 e terminando em 7:
#5 X 4 = 20
#5 X 5 = 25
#5 X 6 = 30
#5 X 7 = 35
#Obs: Você deve verificar se o usuário não digitou o final
# menor que o inicial.

print( "Digite um numero inteiro para montar a tabuada de Subtração")

num1 = int(input())

print( "Digite o numero inicial ")
num_inicial = int(input())

print( "Digite o numero final ")
num_final = int(input())

if num_final < num_inicial:
    print("O número final não deve ser menor que número inicial. Digite um numero válido")
else:
    print("Tabuada de", num1,  " -  A operação iniciando no número: " , num_inicial,  " e terminando no numero: ", num_final,  ":")


for num in range( num_inicial , num_final + 1 ):
    subtrai  = num1 - num
    
    print (num1, " - ", num , " = ", subtrai )