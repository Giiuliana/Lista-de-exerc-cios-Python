#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador

from random import randint
computador = randint(0, 5)  # computador escolhe um número entre 0 e 5
jogador = int(input('Digite um numero de 0 a 5:'))
print('pensei no numero {}'.format(computador))

if jogador == computador:
    print('Parabéns, você acertou!')

else:
    print('Você errou! Eu pensei no número {}'.format(computador))