def montar_tabuada(numero, inicio, fim):
    if fim < inicio:
        print("Erro: O valor final deve ser maior ou igual ao valor inicial.")
    else:
        print(f"Vou montar a tabuada de {numero} começando em {inicio} e terminando em {fim}:")
        for i in range(inicio, fim + 1):
            resultado = numero * i
            print(f"{numero} X {i} = {resultado}")

numero = int(input("Montar a tabuada de: "))
inicio = int(input("Começar por: "))
fim = int(input("Terminar em: "))

montar_tabuada(numero, inicio, fim)


numero = int(input("Montar a tabuada de: "))
inicio = int(input("Começar por: "))
fim = int(input("Terminar em: "))

if fim < inicio:
    print("Erro: O valor final deve ser maior ou igual ao valor inicial.")
else:
    print(f"Vou montar a tabuada de {numero} começando em {inicio} e terminando em {fim}:")
    for i in range(inicio, fim + 1):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")
