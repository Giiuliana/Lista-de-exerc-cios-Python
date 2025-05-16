# Procurar  o nome Silva na string

# O programa remove os espaços em branco tanto na esquerdsa quanto na direita
# Transforma todas as letras em minusculo, para não haver divergencias entre a entrada do usuário e a leitura do programa
nome = input("Digite seu nome: ").lstrip().rstrip()
print("O seu nome tem Silva? {}".format("silva" in nome.lower()))

# O programa verifica se o nome digitado tem a palavra Silva, e retorna True ou False