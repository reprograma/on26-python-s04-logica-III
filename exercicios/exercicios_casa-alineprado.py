""" Exercicio 36 - Repetição

O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
Preço do pão: R$ 0.18
Panificadora Pão de Ontem - Tabela de preços
1 - R$ 0.18
2 - R$ 0.36
...
50 - R$ 9.00"""


preco_pao = float(input("Digite o preço do pão: R$ "))

print("Panificadora Pão de Ontem - Tabela de preços")

for quantidade in range(1, 51):
    valor_total = quantidade * preco_pao
    print(f"{quantidade} - R$ {valor_total:.2f}")



"""Exercicio 5 - Listas """


numeros = []
pares = []
impares = []

for i in range(20):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(numero)

    if numero % 2 == 0:  
        pares.append(numero)
    else:
        impares.append(numero)

print("Números Inteiros:", numeros)
print("Números Pares:", pares)
print("Números Ímpares:", impares)


