n = 1
Par = 0
Impar = 0

while n <= 10:
    a = int(input())
    n = n + 1
    if a % 2 == 0:
        Par = Par + 1
    else:
        Impar = Impar + 1

print("A quantidade de números pares é: ", Par)
print("A quanttdade de números ímpares é: ", Par)