numeros = []
num_pares = []
num_impares = []

cont = 1
tam = 21 # o contador começa em 1, por isso 21 
while cont < tam: 
    
    
    print ("Digite o " , cont,"º número inteiro de 20 numeros: ")
    num = int(input())
    numeros =  numeros + [num] #acrescenta [num](digitado pelo usuário) a lista 
    
    if( num % 2 == 0):
        num_pares = num_pares + [num] #acrescenta numeros perae[num]  (digitado pelo usuário) a lista 
    else:
         num_impares = num_impares + [num] #acrescenta [num](digitado pelo usuário) a lista 
    cont += 1        
    
print("Os números digitados são: ", numeros)
print(" ")
print("Os números pares são: ", num_pares)
print(" ")
print("Os números ímpares são:" , num_impares)


