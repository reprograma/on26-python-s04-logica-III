#Vamos mudar nosso laço para imprimir um intervalo iniciado em 0 com n números informado pelo usuário. 

num_user = float(input("Coloque aqui seu número: "))
num_inicial = 0

while num_inicial < num_user:
    print(num_inicial)
    num_inicial += 1

print("Cabou aqui!")