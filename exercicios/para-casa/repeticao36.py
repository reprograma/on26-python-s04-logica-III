#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo: Obs: Você deve verificar se o usuário não digitou o final menor que o inicial. OK

print("Introduza o número que deseja para a tabuada: ")
num_init = int(input())

print("Introduza de quanto até quando deseja que faça os cálculos: ")

valor_inter = int(input("Número de onde inicia: "))
valor_final = int(input("Número de onde finaliza: "))



if valor_final < valor_inter: 
    print("Error, valor inválido")
else:
    num1 = range(valor_inter, valor_final + 1)
    for num in num1:
        resultado = num_init * num
        print(f"{num_init} X {num} = {resultado}")
        

        
    




