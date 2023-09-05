tabuada = int(input("Montar a tabuada de: "))
comeco = int(input("Começar por: "))
termina = int(input("Terminar em: "))

for i in range(comeco, termina + 1):
    print(f"{tabuada} X {i} = {tabuada * i}")

    if comeco < termina:
        print(str("Por favor, comece com um numero maior que o campo 'termina'!"))
        