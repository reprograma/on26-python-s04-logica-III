
#questao 36 - Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
#Montar a tabuada de: 5
#Começar por: 4
#Terminar em: 7

#Vou montar a tabuada de 5 começando em 4 e terminando em 7:
#5 X 4 = 20
#5 X 5 = 25
#5 X 6 = 30
#5 X 7 = 35
#Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

#Deverá solicitar o usuário o numero (inteiro) para fazer a tabuada
#int = usar numero inteiro
#input = para solicitar que o usuário digite e armazena


numero = int(input("Montar a tabuada de: "))
# usuario digita o valor inicial
comeco = int(input("começar com:"))
#usuario digita o valor final
final = int(input("terminar com:"))

# verificar se o valor inicial é menor ou igual o valor final
#caso em tela, poderá usar while (verificar de o valor inicial é maior que o valor final, caso seja,devera apresentar mensagem e o usuario insira o valor novamente
# ideia de repetição


while comeco > final:

  print("Erro: O valor inicial deve ser menor ou igual ao valor final!")
  comeco = int(input("Começar com:"))
  final = int(input("Terminar em:"))

print(f"Vou montar a tabuada de {numero} começando em {comeco} e terminando em {final}:")
# f = incorpora expressão dentro da string
#{} = marcadores para as expressões serem inseridas


#loop que percorre os numeros do comeco ao final
for i in range(comeco, final + 1):
    resultado  = numero * i 
    print(f"{numero} X {i} = {resultado}")

