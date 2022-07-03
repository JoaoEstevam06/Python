velocidade = float(input('Qual  a velocidade do carro? '))
if velocidade > 80:
    print('MULTADO!!! Você excedeu o limite de velocidade'.format(velocidade))
    multa = (velocidade - 80) * 7
    print('Voce deve pagar RS${} de multa'.format(multa))
else:
    print('limite permitido, boa viagem! ')
