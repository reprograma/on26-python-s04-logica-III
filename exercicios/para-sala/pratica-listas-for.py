#combinando listas e for
# se usamos for não precisamos usar o index

# criamos uma lista
notas = [7, 5 , 7.3]

# nossa função vai receber a lista inteira
def calcula_media(notas):
    # definimos a variável de retorno
    soma_notas = 0
    # dentro da função acessamos a lista
    # para cada nota na lista de notas some essa nota
    # não precisamos usar index, pois o for vai precorrer a lista pegando os valores em sequência 
    for nota in notas:
        soma_notas = soma_notas + nota
    # usamos o len para calcular a média, assim podemos trabalhar com n quantidades de notas sem precisar alterar o código
    return round((soma_notas/len(notas)), 2)

# acessamos as notas por index para chamar a função
print(calcula_media(notas))