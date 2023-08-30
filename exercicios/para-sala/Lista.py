#LSITAS
def calcula_media(notas):
    soma_das_notas = 0
    for nota in notas:
        soma_das_notas += nota
    return soma_das_notas/len(notas)

notas = [15, 98, 75]

print(calcula_media(notas))


# def calcula_media(nota1, nota2, nota3):
#    media = (nota1 + nota2 + nota3)/3
#    return media

# notas = [15, 98, 75]

# print(calcula_media(notas[0], notas[1], notas[2]))

