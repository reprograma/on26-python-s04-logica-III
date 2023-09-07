
numero1 = int(input())
numero2 = int(input())

# solicitando que o programa tente fazer a divisão
try:
    print(numero1/numero2)
# se não conseguir fazer a divisão, faz isso aqui
except:
    print("Não é possível dividir por zero.")