# precisamos trabalhar com um número grande de variáveis e dados
# como armazenar e organizar dados?
# precisamos armazenar nossas variáveis em estruturas de dados

# vamos organizar as três notas em um dicionário
# criamos uma variável e colocamos os valores das notas entre chaves com seus nomes e separadas por vírgula

notas = { 
    "notas1": 8, 
    "notas2": 5, 
    "notas3": 7.3
    }

# para acessar os valores de um dicionário usamos a função .values(): 
def calcula_media(notas):
    # definimos a variável de retorno
    soma_notas = 0
    # dentro da função acessamos o dicionário
    for nota in notas.values():
        soma_notas = soma_notas + nota
    # usamos o len para calcular a média, assim podemos trabalhar com n quantidades de notas sem precisar alterar o código
    return round((soma_notas/len(notas)), 2)

# acessamos as notas por index para chamar a função
print(calcula_media(notas))