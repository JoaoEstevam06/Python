from time import sleep
distancia = float(input('Digite a distância da sua viagem: '))
print('Calculando a distancia da sua viagem...')
sleep(3)
print('A distância da sua viagem é de {}Km'.format(distancia))
km1 = distancia * 0.50
km2 = distancia * 0.45
if distancia <= 199:
    print('O valor da viagem é R${:.2f}'.format(km1))
else:
    print('O valor da viagem é R${:.2f}'.format(km2))
