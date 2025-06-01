nome = input('Digite seu nome:')

nome_maisculo = nome.upper()
nome_minusculo = nome.lower()
nome_limpo = nome.replace(' ', '')
nome_qtd = len(nome_limpo)
primeiro_nome = nome.split()[0]


print('Seu nome em minusculo é ', nome_minusculo)
print('Seu nome em maiusculo é ', nome_maisculo)
print('Seu nome contém {} letras'.format(nome_qtd))
print('Seu primeiro nome é {} e ele contém {} letras'.format(primeiro_nome, nome_qtd))