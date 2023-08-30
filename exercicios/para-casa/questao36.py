
# Solicita ao usuário o número a ser multiplicado
numero = int(input("Digite um número: "))

# Solicita ao usuário o valor inicial da tabuada
valor_inicial = int(input("Digite o valor inicial da tabuada: "))

# Solicita ao usuário o valor final da tabuada
valor_final = int(input("Digite o valor final da tabuada: "))

# Verifica se o valor inicial é menor ou igual ao valor final
if valor_inicial >= valor_final:
    print("O valor inicial deve ser menor que o valor final.")
else:
    # Imprime a tabuada
    for i in range(valor_inicial, valor_final + 1):
        print(f"{numero} x {i} = {numero * i}")