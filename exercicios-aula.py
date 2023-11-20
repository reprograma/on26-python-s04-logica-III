inicio = 0
intervalo = int(input("Insira um número:")) # o int é colocado antes do input porque o input recebe string então o int altera o tipo do dado recebido pela variável

while inicio <= intervalo:
    print(inicio)  
    # inicio += 1 --> errei porque não imprimiria o número inputado pelo usuário
    inicio = inicio + 1

    