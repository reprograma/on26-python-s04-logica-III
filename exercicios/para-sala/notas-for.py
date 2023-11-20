def calcula_media(notas):
    soma_notas = 0 
    for nota in notas:
        soma_notas = soma_notas + nota
    return soma_notas/len(notas)

notas = [15, 98, 75]

#acessando notas por index então dá erro porque as notas separadas viram três argumentos e a função espera receber somente um argumento 
# então devemos puxar a lista completa e acessar cada item dela por meio do for 
 
print(calcula_media(notas)) 