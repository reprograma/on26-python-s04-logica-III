def calcula_media(notas):
    for aluna in notas.values():
        if aluna.values():
            soma_notas = 0
            for nota in aluna.values(): 
                soma_notas = soma_notas + nota
            aluna.update({"media": (soma_notas/len(aluna))})
    return notas

notas = {
    "Belisa": 
    {
    "nota1": 15,
    "nota2": 98,
    "nota3": 75
    },
}

notas = calcula_media(notas)
for nome, notas in notas.items():
    print(f"A aluna {nome} obteve média {notas['media']}")
else: 
    print("Todas ")
