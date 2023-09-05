# Desenvolva um programa que faça a tabuada de um número qualquer inteiro
# que será digitado pelo usuário, mas a tabuada não deve necessariamente 
# iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados 
# também pelo usuário. Observação: Você deve verificar se o usuário não digitou
# o final menor que o inicial.


# solicitar o número, valor inicial e valor final ao usuário
numero = int(input("Digite um número inteiro para a tabuada: "))
valor_inicial = int(input("Digite o valor inicial da tabuada: "))
valor_final = int(input("Digite o valor final da tabuada: "))

# verificar se o valor final é maior ou igual ao valor inicial
if valor_final < valor_inicial:
    print("Erro: O segundo valor digitado deve ser maior ou igual ao primeiro valor.")
else:
    # imprimir a tabuada no intervalo determindo pelo usuário com loop 
    print(f"Tabuada do {numero} começando em {valor_inicial} e terminando em {valor_final}:")
    for i in range(valor_inicial, valor_final + 1):
    # calcular o resultado da multiplicação entre o número e o valor atual (i)
        resultado = numero * i
    # imprimir a expressão da multiplicação e seu resultado
    print(f"{numero} x {i} = {resultado}")
