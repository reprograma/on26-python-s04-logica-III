def calcula_media(notas):
    soma_notas = 0
    for nota in notas.values():
        soma_notas = soma_notas + nota
    return soma_notas/len(notas)

notas = {
    "nota1": 15,
    "nota2": 98,
    "nota3": 75
}

print(calcula_media(notas)) 