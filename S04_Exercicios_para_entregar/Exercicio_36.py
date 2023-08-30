#Atividade feita com meu grupinho

Tabuada = []
Comeca_por = []
Termina_em = []

Tabuada_de = int(input("Digite a tabuada que deseja visualizar: "))
Comeca_por = int(input("Digite um número para iniciar a tabuada: "))
Termina_em = int(input("Digite um número para terminar a tabuada: "))

while Termina_em < Comeca_por:

    print("\nO número final é menor que o inicial, ajuste!\n")

    Comeca_por = int(input("Começar por: "))

    Termina_em = int(input("Terminar em: "))

for i in range(Comeca_por, Termina_em + 1):
    Resultado = Tabuada_de * i
    print(f"{Tabuada_de} x {i} = {Resultado}")