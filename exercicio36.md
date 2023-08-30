numero = int(input('montar a tabuada de multiplicação: '))

inicio = int(input('começar por: '))
fim = int(input('terminar em: '))

if fim < inicio:
    print('erro: O valor final não pode ser menor que o valor inicial.')
else:
    print(f'vou montar a tabuada de {numero} começando em {inicio} e terminando em {fim}:')
    for i in range(inicio, fim + 1):
        resultado = numero * i
        print(f'{numero} X {i} = {resultado}')
