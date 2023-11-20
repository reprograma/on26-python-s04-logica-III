# # range com stop == 5, start == 0 e step == 1

# print("range(5)") #imprimiu a string "range (5)" e em seguida imprimiu a execução da função range(5)
# print(range(5))

# # range com start == 1 e stop == 10
# print("range(1, 10)")
# print(range(1, 10))

# # range com start == 1, stop == 89, step == 3 
# print("range(25, 89, 3)") 
# print(range(25, 89, 3)) 

# # range com start == 5, stop == 1
# print("range(5, 1)") 
# print(range(5, 1)) 

# em range teremos um intervalo sempre semiaberto, nosso ponto de parada nunca estará incluso na função range
# range servirá para ser utilizada em outros laços como o for; definindo o intervalo em que esse laço ocorre   

# for numero in range(1, 10, 2): #se eu quiser que o 10 seja impresso, preciso codar um parâmetro stop 11 porque o último nunca estará incluso
#     print(numero)

# o step é o terceiro parâmetro após a segunda vírgula e indica um comportamento para que a função saiba quando 'pular' uma execução
# 2 pular a cada dois, 3 pular a cada 3 etc... 
# para poder utilizar o step é sempre necessário informar o start! 
# não é possível utilizar o range com uma variável de texto, somente com números

variavel_texto = "marianna está absurdamente atrasada no conteúdo"

# for parte in variavel_texto:
#     print (parte)

# for numero in range (0,len(variavel_texto), 2):
#     print(numero)
#     print(variavel_texto[numero])
#     # print(variavel_texto[caracter])

# print(variavel_texto)

# ### para imprimir todos os números de zero a dez

# # for numero in range (0,11):
# #     print(numero)

#************#

# numero = 0
# while numero <= 10:
#     print(numero)
#     numero += 1

# ### para imprimir todos os números de dez a zero

# for numero in range (10, -1, -1):
#     print(numero)

# for numero in range (22, 68, 2):
#     print(numero)

# soma = 0
# for numero in range(0,11):
#      soma = soma + numero

# print(soma)

# print(sum(range(11)))

# um código para somar as letras do meu home

meu_nome = "marianna pimentel de carvalho"
print(len(meu_nome.replace(" ","")))