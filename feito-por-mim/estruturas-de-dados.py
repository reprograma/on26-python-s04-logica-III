def calc_media(notas): 
    soma_notas = 0
    for nota in notas:
        soma_notas += nota
    return soma_notas / 3  ##Como triar esse 3 aqui, sem precisar ficar contando? 

notas = [15, 98, 75]

print(calc_media(notas))

 ##Como triar esse 3 aqui, sem precisar ficar contando?

def calc_media(notas): 
    soma_notas = 0
    for nota in notas:
        soma_notas += nota
    return soma_notas / len(notas) 

notas = [15, 98, 75]

print(calc_media(notas))