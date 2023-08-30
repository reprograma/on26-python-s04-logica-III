# Damaris Santos
#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário.
# Resolvido em grupo de estudos

tabuada = int(input("Fazer tabuada de: "))
comecar = int(input("Começar pelo n°: "))
terminar = int(input("Terminar pelo n°: "))

while terminar < comecar:

    print("\nO número final não pode ser menor que o inicial, realize o ajuste!\n")

    comecar = int(input("Começar por: "))

    terminar = int(input("Terminar em: "))

for i in range(comecar, terminar + 1):
    resultado = tabuada * i
    print(f"{tabuada} x {i} = {resultado}")