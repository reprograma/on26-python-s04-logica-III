par= []
impar= []
vetor=[]
for x in range (20):
    numero = int(input("Digite o número ="))
    vetor.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print("vetor")
for numero in vetor:
    print(numero)

print("par")
for numero in par:
    print(numero)

print("impar")
for numero in impar:
    print(numero)



