# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário,
# mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, 
# o valor inicial e final devem ser informados também pelo usuário

numero_tabuada = int(input("insira o numero da tabuada: "))
valor_inicial = int(input("insira valor inicial: "))
valor_final = int(input("insira valor final: "))

if valor_inicial <= valor_final:
    for numeros_multiplicaveis in range(valor_inicial, valor_final):
        print(numeros_multiplicaveis)

    while valor_inicial < valor_final:
        numeros_multiplicados = numero_tabuada * valor_inicial
        print(numeros_multiplicados)
        valor_inicial = valor_inicial + 1
else:
    print("o numero inicial precisa ser menor que o final. Refaça o programa")

