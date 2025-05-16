#Sorteando um nome

import random

nome1 = input("Nome do aluno 1: ")
nome2 = input("Nome do aluno 2: ")
nome3 = input("Nome do aluno 3: ")
nome4 = input("Nome do aluno 4: ")  
nome5 = input("Nome do aluno 5: ")
nome6 = input("Nome do aluno 6: ")

nomes = [nome1, nome2, nome3, nome4, nome5, nome6]
sorteio = random.choice(nomes)

print("O nome soteado foi {}".format(sorteio))

#random.choice