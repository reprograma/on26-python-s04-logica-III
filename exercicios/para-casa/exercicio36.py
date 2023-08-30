#Atividade realizada em grupo

tabuada_de = int(input("Montar tabuada de: "))

comecar_por = int(input("Começar por: "))

terminar_em = int(input("Terminar em: "))

while terminar_em < comecar_por:

    print("\nO número final é menor que o inicial, ajuste!\n")

    comecar_por = int(input("Começar por: "))

    terminar_em = int(input("Terminar em: "))

for i in range(comecar_por, terminar_em + 1):
    resultado = tabuada_de * i
    print(f"{tabuada_de} x {i} = {resultado}")