numero_tabuada = int(input("informe o numero da tabuada: "))
inicio_tabuada = int(input("informe o inicio: "))
fim_tabuada = int(input("informe o final: "))

while inicio_tabuada > fim_tabuada:
    print("o começo tem que ser menor que o fim")
    inicio_tabuada = int(input("informe o inicio: "))
    fim_tabuada = int(input("informe o final: "))

for numero in range(inicio_tabuada, fim_tabuada+1):
    resultado = numero_tabuada*numero
    print(f"{numero_tabuada} x {numero}: {resultado}")