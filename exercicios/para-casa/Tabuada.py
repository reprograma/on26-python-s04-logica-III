#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, 
#mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e 
#final devem ser informados também pelo usuário

inicio_tabuada = int(input("Digite o algarismo inicial da sua tabuada: "))
meio_tabuada = int(input("Digite o algarismo de onde quer que comece a sua tabuada. EXP: Quero que comece em 10: "))
fim_tabuada = int(input("Agora digite o algarismo final da sua tabuada. EXP: até onde quer que ela vá: "))
counter = 0
for i in range(meio_tabuada, fim_tabuada + 1):
    resultado = i * inicio_tabuada
    print(f"{inicio_tabuada} x {i} = {resultado}")