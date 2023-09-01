list_input = []

for i in range(20):
    list_input.append(int(input()))

list_par = []
list_impar = []
for i in list_input:
    if i%2:
        list_impar.append(i)
    else:
        list_par.append(i)
        

print(list_input)
print(list_par)
print(list_impar)