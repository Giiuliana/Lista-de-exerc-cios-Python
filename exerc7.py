# Manipulando texto 
# Cada caractere de uma string é enumerado a partir do índice 0. então o decimo caractere está na casa 9.
# Faça um programa que leia uma string e imprima o caractere que está na posição 10.
# O python diferencia letras minusculas e maiusculas
# Frase [:5] - imprime do primeiro caractere até o quinto (não inclui o quinto)
# Frase [5:] - imprime do quinto caractere até o final da string
# Frase [5:10] - imprime do quinto caractere até o décimo (não inclui o décimo)
# Frase [5:10:2] - imprime do quinto caractere até o décimo (não inclui o décimo) pulando de 2 em 2
# Frase [5::2] - imprime do quinto caractere até o final da string pulando de 2 em 2
# frase.replace (a, b)- substitui uma string por outra
# frase.upper() - transforma a string em maiusculo
# frase.lower() - transforma a string em minusculo
# usando len() para contar o número de caracteres da string
# usando frase.count('o') para contar o número de caracteres 'o' minusculo na string 
# frase.captalize() - transforma a primeira letra da string em maiusculo e o resto em minusculo
# frase.title() - transforma a primeira letra de cada palavra em maiusculo e o resto em minusculo
# frase.strip() - remove os espaços em branco do começo e do final da string
# frase.rstrip() - remove os espaços em branco do final da string


frase = input("Digite seu nome: ").lstrip()
frase_minusculo = frase.lower()
frase_maiusculo = frase.upper()
n_caracteres = len(frase)
primero_nome = frase.split()[0]
print("Seu nome em maiusculo é:{}".format(frase_maiusculo))
print("Seu nome em minusculo é:{}".format(frase_minusculo))
print("Seu nome tem {} caracteres".format(n_caracteres))        
print("Seu primeiro nome é: {}".format(primero_nome))
print("Seu primeiro nome tem {} caracteres".format(len(primero_nome)))

