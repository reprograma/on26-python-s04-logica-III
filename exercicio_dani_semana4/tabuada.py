


def tabuada(tab, fator_inicial, fator_final):
    for t in range(tab, tab + 1):
        print(f"Tabuada do {t}:")
        for f in range(fator_inicial, fator_final + 1):
            resultado = t * f
            print(f"{t} x {f} = {resultado}")
        print()

tabuada_do = int(input("Digite o número que deseja a tabuada: "))
fator_inicial = int(input("Qual o fator multiplicativo que deseja iniciar? "))
fator_final = int(input("Qual o fator multiplicativo que deseja finalizar? " ))
tabuada(tabuada_do, fator_inicial, fator_final)