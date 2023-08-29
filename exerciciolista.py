#Faça um Programa que leia 20 números inteiros e armazene-os numa lista,
#armazene os números pares na lista par e os números ímpares na lista impar.
#Imprima os três vetores.

 
# criar as listas
numero = []
par = []
impar = []

#fazer o for com range, pedir digitação com imput e reservar na primeira lista
for i in range (20):
    digito = int(input("Digite um número:"))
    numero.append(digito)
    
# com if reservar no par os que com resto da divisão por 2 for zero    
    if digito % 2 == 0:
     par.append(digito)
# com else guardar os outros na lista de ímpares
    else: 
       impar.append(digito) 
    
# imprimir os resultados    
print("Números digitados:", numero)
print("Números pares:", par)
print("Números ímpares", impar)



 





