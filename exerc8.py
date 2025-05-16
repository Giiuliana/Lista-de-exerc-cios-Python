# Progrma que verifica se o nome de uma cidade começa com "Rio"
# tranforma todas as letras em minusculo com o método lower()
# caso o usuário digite espaços em branco antes da cidade, o metodo lstrip () remove o espaços
cidade = input('dgite o nome da cidade:').lstrip()
cidade_minusculo = cidade.lower()
print(cidade_minusculo[:4] == 'rio')
