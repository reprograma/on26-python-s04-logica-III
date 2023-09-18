#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente 
#iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
#Montar a tabuada de: 5
#Começar por: 4
#Terminar em: 7
#Vou montar a tabuada de 5 começando em 4 e terminando em 7:
#5 X 4 = 20
#5 X 5 = 25
#5 X 6 = 30
#5 X 7 = 35
#Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

#opção de como fazer com while:
#while inicial <= final:
#resultado = num * inicial
# print(f"{num} X {inicial} = {resultado}")
#inicial += 1

while True:
    try:
        num = int(input("Você deseja fazer a tabuada de qual número inteiro? "))
        inicial = int(input("Qual é o número inicial da tabuada? "))
        final = int(input("Qual é o número final da tabuada? "))

        if num >= 0 and num <= 10 and inicial >= 0 and inicial <= 10 and final >= 0 and final <= 10 and final > inicial:
            for i in range(inicial, final + 1):
                resultado = num * i
                print(f"{num} X {i} = {resultado}")
            else:
                print("Número final deve ser maior que o número inicial")
        else:
            print("Números devem ser inteiros positivos menores que 10")
        
    except:
        print("Entradas devem ser números inteiros.")
    break