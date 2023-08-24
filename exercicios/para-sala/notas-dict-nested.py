def calcula_media(notas):
    for notas_da_aluna in notas.values():
        soma_notas = 0
        for nota in notas_da_aluna.values(): 
            soma_notas = soma_notas + nota
        notas_da_aluna['media'] = (soma_notas/len(notas_da_aluna))
    
def avalia_situacao(aluna):
    if aluna['media'] > media_aprovacao or aluna.get('media_recuperacao', False) > media_aprovacao:
        aluna['situacao'] = 'aprovada'
    elif aluna['media'] >= 2 and not aluna.get('media_recuperacao', False):
        aluna['situacao'] = 'em recuperação'
    else: 
        aluna['situacao'] = 'reprovada'

media_aprovacao = 60
notas_das_alunas = {
    "Belisa": 
        {
        "nota1": 15,
        "nota2": 25,
        "nota3": 35
        },
    "Jani": 
        {
        "nota1": 98,
        "nota3": 100
        },
    "Mayhhara": 
        {
        "nota1": 100,
        "nota2": 98,
        "nota3": 99
        },
}

calcula_media(notas_das_alunas)
for nome, notas in notas_das_alunas.items():
    avalia_situacao(notas)
    print(f"A aluna {nome} obteve média {notas['media']} e está {notas['situacao']}")
    if notas['situacao'] != 'em recuperação': 
        continue
    print('Informe {nome} a nota de recuperação da aluna:')
    try:
        notas['media_recuperacao'] = (float(input("Nota de recuperacao: ")) + notas['media']) / 2
    except:
        print("As notas de recuperacao devem ser informadas somente com números")
        break
    avalia_situacao(notas)
    print("")
    print(f"A aluna {nome} obteve média final {notas['media']} e está {notas['situacao']}")
else: 
    print('Todas as notas foram calculadas com sucesso!')

