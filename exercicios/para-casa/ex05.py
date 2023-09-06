num_par = []
num_impar = []
nums = []

while len(nums) < 20:
    valores = int(input("Digite 20 números: "))
    nums.append(valores)

    if valores % 2 == 0:
        num_par.append(valores)

    else: 
        num_impar.append(valores)

print("A lista de números é: ", nums)
print("A lista de números pares é: ", num_par)
print("A lista de números ímpares é: ", num_impar)
