numero_tabuada = int(input("informe o numero da tabuada: "))
inicio_tabuada = int(input("informe o inicio: "))
fim_tabuada = int(input("informe o final: "))

if inicio_tabuada > fim_tabuada:
    inicio_tabuada, fim_tabuada = fim_tabuada, inicio_tabuada

for numero in range(inicio_tabuada, fim_tabuada+1):
    resultado = numero_tabuada*numero
    print(f"{numero_tabuada} x {numero}: {resultado}")