# precisamos trabalhar com um número grande de variáveis e dados
# como armazenar e organizar dados?
# precisamos armazenar nossas variáveis em estruturas de dados

# vamos organizar as três notas em uma lista:
# criamos uma variável e colocamos os valores das notas entre colchetes e separados por vírgula

notas = [7, 5 , 7.3]

def calcula_media(nota1, nota2, nota3):
    media = round(((nota1 + nota2 + nota3)/3), 2)
    return media

# acessamos as notas por index para chamar a função
print(calcula_media(notas[0], notas[1], notas[2]))