
operador = input("Digite a operação que deseja fazer (soma, subtração, multiplicação ou divisão): ")
tabuada = int(input("Número para montar a tabuada: "))
inicio = int(input("Digite o número para inicar a tabuada: "))
final = int(input("Digite o número para terminar a tabuada: "))



i = inicio

if operador == "soma":
    while i <= final:
        resultado = int(tabuada + i)
        print(tabuada, "+", i, "=", resultado)
        i += 1


elif operador == "subtração":
    while i <= final:
        resultado = int(tabuada - i)
        print(tabuada, "-", i, "=", resultado)
        i += 1

elif operador == "multiplicaçã o":
    while i <= final:
        resultado = int(tabuada * i)
        print(tabuada, "*", i, "=", resultado)
        i += 1

elif operador == "divisão":
    while i <= final:
        resultado = int(tabuada / i)
        print(tabuada, "/", i, "=", resultado)
        i += 1

else:
    print("Nenhum das operações possíveis foi escolhida")