

velocidade = float(input('Digite a velocidade do carro em Km/h: '))
limite = 50

limite_excesso = (velocidade - limite) *7
if velocidade > limite:
    print('Você foi multado por {}, por excesso de velocidade!'.format(limite_excesso))
else:
    print('Você está dentro do limite de velocidade, continue assim!')