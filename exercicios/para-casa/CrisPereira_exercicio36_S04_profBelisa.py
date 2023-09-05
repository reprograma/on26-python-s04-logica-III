# Semana 04 - exercício da Semana
# Prof Belisa - estudante Cris Pereira

# Ex. 36 
# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário. Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

print("Programa Tabuada Infinita")

def usuario():
    num_tabuada = int(input("Montar a tabuada de: "))
    inicio = int(input("Começar por: "))
    fim = int(input("Terminar em: "))

    return num_tabuada, inicio, fim

numero_tabuada, inicio_tabuada, fim_tabuada = usuario()

while fim_tabuada < inicio_tabuada:
    print("Por favor, informe números inteiros e o número inicial deve ser menor que o último.")
    numero_tabuada, inicio_tabuada, fim_tabuada = usuario()


print(f"Vou montar a tabuada de {numero_tabuada} começando em {inicio_tabuada} e terminando em {fim_tabuada}:")

fator = inicio_tabuada
for fator in range(inicio_tabuada,fim_tabuada+1,1):
    print (f"{numero_tabuada} X {fator}: {numero_tabuada*fator}")
    fator = fator+1

print("Fim do programa")
