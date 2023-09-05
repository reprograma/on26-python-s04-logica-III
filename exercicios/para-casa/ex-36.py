# Desenvolva um programa que faça a tabuada de um número qualquer inteiro
# que será digitado pelo usuário, mas a tabuada não deve necessariamente 
# iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados 
# também pelo usuário. Observação: Você deve verificar se o usuário não digitou
# o final menor que o inicial.


numero = int(input("Digite seu número de tabuada: "))
valor_inicial = int(input("Digite o valor inicial da tabuada: "))
valor_final = int(input("Digite o valor final da tabuada: "))


if valor_final < valor_inicial:
    print("Atenção: O valor final digitado deve ser maior ou igual ao valor inicial.")
else:
    
    print(f"Tabuada do {numero} começando em {valor_inicial} e terminando em {valor_final}:")
    for t in range(valor_inicial, valor_final + 1):

        resultado = numero * t
  
    print(f"{numero} x {t} = {resultado}")