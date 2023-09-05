# 1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

lista = [int(input("Insira o primeiro valor: ")), int(input("Insira o segundo valor: ")), int(input("Insira o terceiro valor: ")), int(input("Insira o quarto valor: ")), int(input("Insira o quinto valor: "))]

print("Lista:", sorted(lista))

# 2. Faça um Programa que leia um vetor de 5 números reais e mostre-os na ordem inversa.

lista = [float(input("Insira o primeiro valor: ")), float(input("Insira o segundo valor: ")), float(input("Insira o terceiro valor: ")), float(input("Insira o quarto valor: ")), float(input("Insira o quinto valor: "))]

print("Lista:", sorted(lista, reverse = True))
print("Lista:", list.reverse(sorted(lista)))

# 3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

def calcula_media(notas):
    soma_notas = 0
    for nota in notas.values(): 
        soma_notas = soma_notas + nota
    return soma_notas/len(notas)

notas = {
    "Nota 1": float(input("Insira a primeira nota: ")),
    "Nota 2": float(input("Insira a segunda nota: ")),
    "Nota 3": float(input("Insira a terceira nota: ")),
    "Nota 4": float(input("Insira a quarta nota: "))
                   
}

print(notas)

print("A média é:", calcula_media(notas))

# 4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

lista = [str(input("Insira o primeiro caracter: ")), str(input("Insira o segundo caracter: ")), str(input("Insira o terceiro caracter: ")), \
         str(input("Insira o quarto caracter: ")), str(input("Insira o quinto caracter: ")), \
         str(input("Insira o sexto caracter: ")), str(input("Insira o sétimo caracter: ")), str(input("Insira o oitavo caracter: ")), \
         str(input("Insira o nono caracter: ")), str(input("Insira o caracter valor: "))]

consoantes = []

for caracter in lista:
    if caracter != "a" or caracter != "e" or caracter != "i" or caracter != "o" or caracter != "u":
        consoantes.append(caracter)

print("A lista", consoantes, "possui", len(consoantes), "consoantes")
print("Fim do programa")

