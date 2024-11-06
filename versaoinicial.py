'''
Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''

soma = 0  # Inicializa a variável soma para acumular a soma dos números pares
cont = 0  # Inicializa o contador para contar quantos números pares foram digitados
conttotal = 0 # Inicializa o contador para contar quantos números foram digitados, no caso 6

# Loop que itera 6 vezes, de 1 a 6
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))  # Solicita ao usuário que digite um número inteiro

    # Verifica se o número digitado é par
    if num % 2 == 0:
        soma = soma + num  # Adiciona o número par à soma total
        cont = cont + 1  # Incrementa o contador de números pares

    conttotal += 1

# Exibe o total de números pares digitados e a soma desses números
print('Você digitou {} numeros, {} pares e a soma de ambos é {}.'.format(conttotal, cont, soma))
# A linha abaixo é uma versão alternativa da impressão, utilizando f-strings (comentada)
#print(f'Você digitou {cont} números pares e a soma de ambos é {soma}.')
