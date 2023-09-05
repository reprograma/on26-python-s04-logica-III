# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve 
# necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário

# Tabuada de multiplicação precisa de: o valor multiplicador, o valor multiplicando inicial e o valor multiplicando final. 
# Nota mental = usar try e except pra evitar valores que não sejam inteiros(?)

apresentacao = print("Olá, boas vindas ao seu gerador de tabuada! Insira os valores pedidos para gerar sua tabuada")

def tabuada (multiplicador, multi_inicial, multi_final):
    inicio = multi_inicial
    while  inicio <= multi_final:
        solucao = multiplicador*inicio
        print (f"{multiplicador} x {inicio} = {solucao}")
        inicio += 1

try:
    multiplicador = int(input("insira o valor do multiplicador da tabuada: "))
    multi_inicial = int(input("Insira o valor inicial da tabuada: "))
    multi_final = int(input("Insira o valor final da tabuada: "))

    tabuada (multiplicador, multi_inicial, multi_final)

except:
    print("Por favor, insira números inteiros")


