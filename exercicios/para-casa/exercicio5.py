#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
# Imprima os três vetores.


numeros = []
num_pares = []
num_impares = []

cont = 1
tam = 6 # o contador começa com 1, por isso 21
while cont < tam: 
    
    
    print ("Digite o " , cont,"º número inteiro de 20 numeros: ")
    num = int(input())
    #print ("Digite o º número inteiro de 20 numeros: ")
    #num2 = int(input())
    numeros.append(num)
  
    if num % 2 == 1:
        num_impares.append(num) # coloca na lista num_impares( estrutura : nome_da_lista.(o ponto chama a função da variável)append(função)) só os nummeros com resto 1
                                #num_impares.append(num_pares) lista dentro de kista 
    else:
        num_pares.append(num)
        
    
    cont += 1


print("")
print("Os números digitados são: ", sort(numeros)) # ordena crescente
print(" ")
print("Os números pares são: ", sort(num_pares))
print(" ")
print("Os números ímpares são:" , sort(num_impares))


