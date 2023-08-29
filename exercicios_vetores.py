vetor_int = []
vetor_par = []
vetor_impar = []


while len(vetor_int) < 21:
    n = int(input("Escreva um numero: "))
    if n in vetor_int:
        print("Nao pode escrever esse numero.")
    else:
        vetor_int.append(n)

print("Vetor Inteiro: ", vetor_int)

for n in vetor_int:
    if n % 2 == 0:
        vetor_par.append(n)
    else:
        vetor_impar.append(n)

print ("Vetor Par: ", vetor_par)
print ("Vetor Impar: ", vetor_impar)