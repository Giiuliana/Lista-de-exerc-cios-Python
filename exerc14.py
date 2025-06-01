nome = input('Digite o nome completo: ').lower()
#print('Seu nome contém "Silva"?', 'SILVA' in nome.upper())
if 'silva' in nome:
    print(nome == 'silva')

else:
    print(nome != 'silva')