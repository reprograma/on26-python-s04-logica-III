# com o range podemos usar apenas números
# se quero imprimir partes de uma frase usamos o len
# len dá o tamanho da variável 
# com ela podemos saber a posição dos caracteres de uma string

# se a gente quiser a última letra da string mas não sabemmos a posição dela
# podemos usar len direto chamando a variável e o tamanho dela:
# variavel_texto[len(variavel_texto)-1]


variavel_texto = "muito legal aprender python!"

# monta uma sequência de números que começa em 0 (start), 
# termina no tamanho da string (stop), com intervalo de 2 em 2 (step)

for caracter in range(0, len(variavel_texto), 2):
    print(caracter) # vai imprimir o intervalo de números da frase
    # para imprimir a letra que está em cada posição usamos:
    print(variavel_texto[caracter])