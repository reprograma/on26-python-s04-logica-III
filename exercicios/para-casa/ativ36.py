numero_a_ser_multiplicado = int(input('Montar a tabuada de: '))
inicio = int(input('Começar por: '))
fim = int(input('Terminar em: '))

print(f'Vou montar a tabuada de {numero_a_ser_multiplicado} começando em {inicio} e terminando em {fim}:')
for numero_inicial in range(inicio, fim + 1):
    print(f'{numero_a_ser_multiplicado} X {numero_inicial} = {numero_a_ser_multiplicado*numero_inicial}')