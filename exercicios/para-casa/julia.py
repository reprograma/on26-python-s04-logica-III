tabuada_de = int(input('Taboada de: '))
numero_inicial = int(input('Primeiro número: '))
numero_final = int(input('Último número: '))



while numero_inicial <= numero_final:
    print(f'{tabuada_de} x {numero_inicial} = {tabuada_de*numero_inicial}')
    numero_inicial = numero_inicial + 1