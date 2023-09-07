
numero = 0

# enquanto número for menor que 5, imprime x
# ele vai rodar "infinitamente" enquanto a condição for verdadeira
# temos que criar uma condição de parada
# quando a condição for falsa, o bloco interno não será executado

# incrementando antes de imprimir
while numero < 5:
    numero = numero + 1 
    print(numero)

print("Fim do programa")


# incrementando depois de imprimir
while numero < 5:
    print(numero)
    numero = numero + 1 
    
print("Fim do programa")