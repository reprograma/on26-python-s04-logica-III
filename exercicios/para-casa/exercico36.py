# Exercício realizado em grupo



comeco = 10
final = 1
tabuada = 5

while (comeco >= final):
	tabuada = int(input("Digite a tabuada que deseja (1 a 10): "))
	comeco = int(input("Digite por qual número deseja começar: "))
	final = int(input("Digite por qual número deseja finalizar: "))
	if (comeco >= final):
		print("")
		print("O valor inicial não pode ser maior que o final!\n")
		print("")
		
print("")	
print("Tabuada de: ", tabuada)
print("Inicializada por: ", comeco)
print("Finalizada por: ", final)

while (comeco < (final + 1)):
	print(tabuada, "X", comeco, "=", tabuada * comeco)
	comeco = comeco + 1