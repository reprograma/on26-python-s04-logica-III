#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 
#200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a 
#população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita 
#repetir a operação.

try:
    pop_a = int(input("Qual o número de habitantes do país A? "))
    pop_b = int(input("Qual o número de habitantes do país B? "))
    tx_a = float(input("Qual a taxa de crescimento do país A, em %? Informe apenas o número. ")) / 100
    tx_b = float(input("Qual a taxa de crescimento do país B, em %? Informe apenas o número. ")) / 100
    anos = 0

    def calc_nova_pop(pop, tx):
        nova_pop = pop * (1 + tx)
        return nova_pop

    if (pop_a <= pop_b and tx_a > tx_b) or (pop_a >= pop_b and tx_a < tx_b):
        while pop_a < pop_b:
            pop_a = calc_nova_pop(pop_a, tx_a)
            pop_b = calc_nova_pop(pop_b, tx_b)
            anos += 1
        print(f"A população do país menos populoso vai alcançar ou ultrapassar a população do mais populoso em {anos} anos.")
    else:
        print("População dos dois países nunca serão iguais.")
    
except:
    print("Entradas devem ser numéricas")