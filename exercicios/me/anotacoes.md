#erros
o try e o except, os dois sempre são usados juntos;

O bloco try e except em Python é semelhante ao try e catch em JavaScript. Ambos são usados para lidar com exceções (erros) que podem ocorrer durante a execução do código. A ideia geral é a mesma em ambas as linguagens: você coloca o código que pode gerar uma exceção dentro do bloco try, e se ocorrer um erro, você captura e lida com a exceção no bloco except.

webScraping

Em complemento ao que a professora tá falando, a iteração é uma maneira eficaz de automatizar tarefas repetitivas e processar grandes quantidades de dados de maneira ordenada.

#Complementando o que a professora disse: Você deve ter certeza de que a condição eventualmente se tornará falsa para evitar um loop infinito

#Geralmente, você escolhe a posição do incremento com base no que faz sentido para a lógica do seu programa e nos resultados que deseja alcançar.

#O loop está incrementando o contador e imprimindo os valores, mas a posição do incremento determina qual sera o primeiro valor impresso. Voce pode mudar a ordem no VSC para confirmar. 🙂

#####

numero = 0
numero_2 = int(input("Digite um numero inteiro: "))

while numero <= numero_2:
    print(numero)
    numero += 1
#for e range
#start primeiro, a parada depois e o step por último

for numero in range (1, 5, 2):
    print(numero)

#for com string
frase_qualquer = "Vamos testar! "

for letra in frase_qualquer:
    print(letra)
    
#O que eu entendi sobre o for com string: É como se você pegasse a frase que está no papel e a colocasse em outro lugar em partes. Você a corta em pedacinhos e a exibe por partes dentro de outra variável, que é a letra. 

for caracter in range(0, len(frase_qualquer), 2):
    print(caracter)
    print(variavel_texto[caracter])
    
#for e range
#Crie um código que imprima todos os número inteiros entre 0 e 10 
#Crie um código que imprima todos os número inteiros entre 10 e 0 
#Crie um código que imprima todos os número pares maiores do que 22 e menores do que 68 
#Crie um código que imprima a soma de todos os números entre 0 e 10 
#Crie um código que conte as letras do seu nome

#1

for numero in range (11):
    print(numero)

print('fim')
#2

for num in range (10,0, -1):
    print(num)
   
print('fim') 
#3

for par in range(24, 69, 2):
    print(par)

print('fim')
#4
soma = 0

for number in range (11):
    soma += number
    
print(soma)

print('fim, 5')   

#ou 

print(sum(range(11)))
#5

meu_nome = "Stefany"
tamanho = 0

for tamanho in range (len(meu_nome)):
    print(tamanho)
   
print(f' O meu tem {tamanho} letras') 

print('fim')   

#ou 

meu_nome = str(input("Qual é o seu nome?"))

print(len(meu_nome(" ","")))
print(meu_nome.replace(" ", ""))


#listas, podemos colcoar listas dentro de listas, mas não é bacana colocar; varioss tipos;



#com o s.append[x], ele adiciona um valor a lista na ultima poisição;

#pop a gent retira o valor da sua posição

nome_da_lista.pop(0)

#pop se quisr a apgar o vlaor

nome_da_lista.pop
78



## exercicio 36
## exercicio de lista - numero 5 




