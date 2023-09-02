var_texto = "Eu não tenho criatividade"

for caracter in var_texto:
    print(caracter)

print(var_texto)

#se quiserssemos colocar as letras pulando uma por uma

var_texto = "Eu não tenho criatividade"

for caracter in range(0, len(var_texto), 2):
    print(var_texto[caracter])

print(var_texto)