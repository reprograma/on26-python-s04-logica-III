numero = int(input("TABUADA DE QUAL NÚMERO?: "))

inicio = int(input("COMEÇAR POR: "))
fim = int(input("TERMINAR EM: "))

if inicio > fim:
    print("O valor inicial deve ser menor ou igual ao valor final.")
else:
    
    contador = inicio
    
    while contador <= fim:
        resultado = numero * contador
        print(f"{numero} X {contador} = {resultado}")
        contador += 1
 





