def calcula_media(notas):
    soma_notas = 0 
    for nota in notas:
        soma_notas = soma_notas + nota
    return soma_notas/len(notas)

notas = [15, 98, 75]

#acessando notas por index
print(calcula_media(notas)) 