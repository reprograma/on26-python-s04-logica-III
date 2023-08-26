#Exercício 36 - Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
# Montar a tabuada de: 5
# Começar por: 4
# Terminar em: 7
# Vou montar a tabuada de 5 começando em 4 e terminando em 7:
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35

#Colhendo os inputs do usuário
print("✖️✖️ GERADOR DE TABUADA ✖️✖️")
input_user = int(input("Digite um número para multiplicar: "))
valor_inicial = int(input("Digite o menor valor para começar a tabuada: "))
valor_final = int(input("Digite o maior valor para terminar a tabuada: "))

#Algoritmo onde a estrutura do print é formada
resultado_tabuada = input_user * valor_inicial
print(f"{input_user} X {valor_inicial} = {resultado_tabuada}")
while valor_inicial < valor_final: #Enquanto o valor inicial for menor que o final
    valor_inicial = valor_inicial + 1 # Vamos incrementando seu valor
    resultado_tabuada = input_user * valor_inicial
    print(f"{input_user} X {valor_inicial} = {resultado_tabuada}")
else:
    print("FIM DA TABUADA 🧮") #Isso eu adicionei só pra que o código ficasse bonitinho

