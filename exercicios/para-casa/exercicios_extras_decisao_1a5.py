# 1. Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido 
# e continue pedindo até que o usuário informe um valor válido. 

nota = float(input("Informe um valor entre zero e dez: "))

while nota < 0 or nota > 10:
    print("O valor é inválido. Favor informar um valor válido.")
    nota = float(input("Informe um valor entre zero e dez: "))
else: print("A nota informada foi", nota, "Fim do programa.")

# 2. Faça um programa que leia um nome de usuário e a sua senha e 
# não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações. 

nome = input("Informe o nome do usuário: ")
senha = input("Informe a senha: ")

while nome == senha:
    print("O nome do usuário e a senha não podem ser iguais. Por favor insira novamente as informações.")
    nome = input("Informe o nome do usuário: ")
    senha = input("Informe a senha: ")
else: print("A operação foi concluída com sucesso.")

# 3. Faça um programa que leia e valide as seguintes informações:

# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f', 'm' ou 'ni';
# Estado Civil: 's', 'c', 'v', 'd'; 

nome = input("Informe o nome do usuário: ")

while len(nome) <= 3:
    print("Informe um nome com mais de 3 caracteres.")
    nome = input("Informe o nome do usuário: ")
else: 
    idade = float(input("Informe a idade do usuário: "))
    while idade < 0 or idade > 150:
        print("Informe uma idade válida.")
        idade = float(input("Informe a idade do usuário: "))
    else:
        salario = float(input("Informe o salário: "))
        while salario < 0:
            print("Informe um salário válido.")
            salario = float(input("Informe o salário: "))
        else:
            sexo = str(input("Informe o sexo segundo a legenda: f - feminino, m - masculino: "))
            while sexo != 'f' and sexo != 'm':
                print("Informe um sexo válido.")
                sexo = str(input("Informe o sexo segundo a legenda: f - feminino, m - masculino: "))
            else:
                estado_civil = input("Informe o estado civil segundo a legenda: s - solteiro(a), c - casado(a), v - viúvo(a), d - divorciado(a): ")
                while estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d":
                    print("Informe um estado civil válido")
                    estado_civil = input("Informe o estado civil segundo a legenda: s - solteiro(a), c - casado(a), v - viúvo(a), d - divorciado(a): ")
                else: print("Fim do programa.")

# 4. Supondo que a população de um país A seja da ordem de 80000 habitantes 
# com uma taxa anual de crescimento de 3% 
# e que a população de B seja 200000 habitantes 
# com uma taxa de crescimento de 1.5%. 
# Faça um programa que calcule e escreva o número de anos necessários 
# para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. 

pop_a = 80000
pop_b = 200000
taxa_a = 0.03
taxa_b = 0.015
ano = 0

while pop_a <= pop_b:
	pop_a = (pop_a + pop_a * taxa_a)
	pop_b = (pop_b + pop_b * taxa_b)
	ano += 1
        
print("População de A superará a de B em", ano, "anos")

# 5. Altere o programa anterior permitindo ao usuário 
# informar as populações e as taxas de crescimento iniciais. 
# Valide a entrada e permita repetir a operação. 

pop_a = float(input("Informe a população inicial de A: "))
pop_b = float(input("Informe a população inicial de B: "))
taxa_a = float(input("Informe a taxa de crescimento de A: "))
taxa_b = float(input("Informe a taxa de crescimento de B: "))
ano = 0

while taxa_a < 0 or taxa_a > 1 or taxa_b < 0 or taxa_b > 1:
    print("Informe uma taxa válida, ou seja, uma porcentagem representada por um número entre 0 e 1")
    taxa_a = float(input("Informe a taxa de crescimento de A: "))
    taxa_b = float(input("Informe a taxa de crescimento de B: "))
else:
    while taxa_a < taxa_b:
        print("A taxa de crescimento A deve ser maior do que a de B")
        taxa_a = float(input("Informe a taxa de crescimento de A: "))
        taxa_b = float(input("Informe a taxa de crescimento de B: "))
    else:
        while pop_a < 0 or pop_b < 0:
            print("Informe um valor positivo para população.")
            pop_a = float(input("Informe a população inicial de A: "))
            pop_b = float(input("Informe a população inicial de B: ")) 
        else:
            while pop_a > pop_b:
                print("O valor de a deve ser menor do que o de b.")
                pop_a = float(input("Informe a população inicial de A: "))
                pop_b = float(input("Informe a população inicial de B: "))
            else:
                while pop_a <= pop_b:
                    pop_a = (pop_a + pop_a * taxa_a)
                    pop_b = (pop_b + pop_b * taxa_b)
                    ano += 1

print("População de A superará a de B em", ano, "anos")
