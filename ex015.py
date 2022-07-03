

dias = int(input('Quantos dias voce ficou com o carro? '))
km = float(input('Quantos KMs rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é: {:.2f}'.format(pago))
