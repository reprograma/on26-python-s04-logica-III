var1 = int(input())
var2 = int(input())

try: 
    print(var1/var2)
except: 
    print("Não é possivel dividir por zero")


#outro exemplo
var1 = input("Informe o numero 1: ")
var2 = input("Informe o numero 2: ")

try: 
    var1_numerica = float(var1)
except: 
    print("informe um número")