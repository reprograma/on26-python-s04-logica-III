variavel1 = input("Informe um número: ")
variavel2 = input("Informe um segundo número: ")

try:
    variavel1_numerica = float(variavel1)
    variavel2_numerica = float(variavel2)
    print(variavel1_numerica/variavel2_numerica)
except:
    print("Operação inválida!\nInforme apenas números.")

