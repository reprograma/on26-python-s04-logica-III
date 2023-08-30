def calcular_populacao(populacao_inicial, taxa_crescimento, anos):
    populacao_final = populacao_inicial * (1 + taxa_crescimento/100) ** anos
    return populacao_final

while True:
    try:
        populacao_inicial = int(input('informe a população inicial: '))
        taxa_crescimento = float(input('informe a taxa de crescimento (em %): '))
        anos = int(input('informe o número de anos: '))
        
        if populacao_inicial < 0 or taxa_crescimento < 0 or anos < 0:
            print('valores inválidos. Todos os valores devem ser positivos.')
        else:
            populacao_final = calcular_populacao(populacao_inicial, taxa_crescimento, anos)
            print(f'a população após {anos} anos será de {populacao_final:.2f}')
            
        repetir = input('deseja realizar outra operação? (s/n): ')
        if repetir.lower() != "s":
            break
    except ValueError:
        print('entrada inválida. Certifique-se de inserir valores numéricos corretos.')
