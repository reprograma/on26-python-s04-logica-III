# Desenvolva um programa que faça a tabuada de
# um número qualquer inteiro que será digitado pelo usuário, 
# mas 
# a tabuada não deve necessariamente iniciar em 1 e terminar em 10, 
# o valor inicial e final devem ser informados também pelo usuário

qualTabuada = int(input("Informe um número inteiro para definir qual será a tabuada calculada:"))
inicioTabuada = int(input("Informe um número inteiro para definir o número inicial do cálculo da tabuada:"))
terminoTabuada = int(input("Informe um número inteiro para definir o número final do cálculo da tabuada:"))

# o numero do inicio não pode ser maior do que o número final

while inicioTabuada > terminoTabuada:
    print("Por favor, informe novamente. O começo da tabuada não pode ser maior que o final da tabuada.")
    inicioTabuada = int(input("Informe um número inteiro para definir o número inicial do cálculo da tabuada:"))
    terminoTabuada = int(input("Informe um número inteiro para definir o número final do cálculo da tabuada:"))

 
for tabuada in range(inicioTabuada, terminoTabuada):
    multiplicacao = tabuada * qualTabuada
    print(f"Sua multiplicação é {tabuada} + {qualTabuada} = {multiplicacao}")