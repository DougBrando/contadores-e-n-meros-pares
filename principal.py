'''
Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''

def obter_numero_inteiro(prompt):
    """Função para obter um número inteiro do usuário com tratamento de exceção."""
    while True:
        try:
            return int(input(prompt))  # Solicita um número inteiro ao usuário
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")  # Mensagem de erro para entradas inválidas

soma = 0  # Inicializa a variável soma para acumular a soma dos números pares
cont = 0  # Inicializa o contador para contar quantos números pares foram digitados
conttotal = 0  # Inicializa o contador para contar quantos números foram digitados, no caso 6

# Loop que itera 6 vezes, de 1 a 6
for c in range(1, 7):
    num = obter_numero_inteiro(f'Digite o {c}º valor: ')  # Obtém um número inteiro do usuário

    # Verifica se o número digitado é par
    if num % 2 == 0:
        soma += num  # Adiciona o número par à soma total
        cont += 1  # Incrementa o contador de números pares

    conttotal += 1  # Incrementa o contador total de números digitados

# Exibe o total de números digitados, quantos foram pares e a soma desses números
print(f'Você digitou {conttotal} números, {cont} pares e a soma deles é {soma}.')
