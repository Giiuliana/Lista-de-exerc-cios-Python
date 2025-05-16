# Programa que le tres stings e sorteia um deles
import random

n1 = str(input('Digite a fruta 1:'))
n2 = str(input('Digite a fruta 2:'))
n3 = str(input('Digite a fruta 3:'))

lista = [n1, n2, n3]

sorteio = random.choice(lista)
print('A fruta sorteada foi: {}'.format(sorteio))

