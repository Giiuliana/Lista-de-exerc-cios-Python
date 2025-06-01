

cidade = input("Digite o nome da cidade: ")
primeiro_nome = cidade.split()[0] # Obs: sempre abrir parenteses para usar o método split
print('O primeiro nome da cidade é:', (primeiro_nome))

if primeiro_nome.upper() == 'SANTO':
    print(primeiro_nome == 'SANTO')
else:
    print(primeiro_nome.upper() == 'SANTO')
