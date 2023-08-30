inicio=4
fim=7
tabuada=12
while (inicio>=fim):
    tabuada=int(input("Tabuada do :"))
    inicio=int(input("Digite o número incial:"))
    fim= int(input("Digite o numero de fechamento:"))
    if inicio>=fim:
        print("Valor não permitido")

print((f"Tabuada de: {tabuada}"))
print(f"Inicio= {inicio}")
print(f"fim {fim}")

while (inicio<(fim+1)):
    print(tabuada, "X", inicio, "=", tabuada * inicio)
    inicio= inicio+1

         