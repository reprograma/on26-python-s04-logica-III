# Resolução exercício para casa - Questão 05
# Link de acesso: https://wiki.python.org.br/ExerciciosListas

dados= [[], [], []]

valor = 0

for c in range(1, 21):
    numero_recebido= int(input('Digite um número: '))
    dados[0].append(numero_recebido)

    if numero_recebido % 2 == 0:
        dados[1].append(numero_recebido)
    else:
        dados[2].append(numero_recebido)

print(f'Todos os números da lista: {dados[0]}') 
print(f'Números pares {dados[1]}')
print(f'Números ímpares{dados[2]}')