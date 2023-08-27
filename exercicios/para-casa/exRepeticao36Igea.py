print('Programa de tabuada limitada')
num = int(input('Digite o número que deseja gerar a tabuada: '))
v1 = int(input('Digite o multiplicador inicial: '))
v2 = int(input('Digite o multiplicador final: '))

if v2 < v1 :
    print('O valor inicial não pode ser menor que o valor final! Por favor tente de novo.')

for it in range(v1 * num, (v2+1) * num):
    if it%num == 0:
        print(it)