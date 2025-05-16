import random

# Ler 4 strings
n1 = input('Digite a string 1: ')
n2 = input('Digite a string 2: ')
n3 = input('Digite a string 3: ')
n4 = input('Digite a string 4: ')

# Criar uma lista com as strings
lista = [n1, n2, n3, n4]

# Embaralhar a lista
random.shuffle(lista)

# Sortear uma posição
sorteio = random.choice(lista)

# Exibir os resultados
print(f'A lista embaralhada é: {lista}')
print(f'A string sorteada foi: {sorteio}')