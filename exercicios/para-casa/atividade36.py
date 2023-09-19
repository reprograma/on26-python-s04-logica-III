# Questão 36 

numero_tabuada = int(input("Tabuada de: "))

inicio_tabuada = int(input("iniciar por: "))
fim_tabuada = int(input("terminar em: "))

while fim_tabuada < inicio_tabuada: 
    print("Valor final deve ser maior ou menor que o inicial.")
    fim_tabuada = int(input("termina em: "))
print(f"montar a tabuada de {numero_tabuada} começando em {inicio_tabuada} e terminando em {fim_tabuada}:")

for i in range(inicio_tabuada, fim_tabuada + 1):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")
    