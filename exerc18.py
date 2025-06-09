# Manipulando indices de strings
# Cada caractere de uma string é enumerado a partir do índice 0. então o decimo caractere está na casa 9.

# Frase [:5] - imprime do primeiro caractere até o quinto (não inclui o quinto)
# Frase [5:] - imprime do quinto caractere até o final da string
# Frase [5:10] - imprime do quinto caractere até o décimo (não inclui o décimo)
# Frase [5:10:2] - imprime do quinto caractere até o décimo (não inclui o décimo) pulando de 2 em 2
# Frase [5::2] - imprime do quinto caractere até o final da string pulando de 2 em 2
# frase.replace (a, b)- substitui uma string por outra

print(("=<>=")*20)
Frase = input("Digite uma frase: ")
print("Frase pulando de 2 em 2: {}".format(Frase[::2]))
print("Frase do quinto caractere até o final: {}".format(Frase[5:]))
print("Mostrando apenas a ultima palavra da frase{}".format(Frase.split()[-1]))
print(("=<>=")*20)

