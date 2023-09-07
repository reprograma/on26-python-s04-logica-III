# Vamos mudar nosso laço para imprimir um intervalo
# iniciado em 0 com n número informado pelo usuário.

# definindo as variáveis
inicio = 0
fim = int(input("Informe um número: "))

# definindo a  comparação
# utilizamos <= porque queremos que que o número informado também seja impresso
# imprimimos antes de incrementar porque queremos que o valor da comparação seja impresso 
while inicio <= fim:
    print(inicio)
    inicio = inicio + 1 # essa equação pode ser escrita como "inicio += 1"

print("Fim do programa")