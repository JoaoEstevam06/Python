"""
crie um programa que laia quanto em dinheiro uma pessoa
tem na carteira e mostre quantos dorares ela pode comprar
"""
real = float(input('Quanto dinheiro voce tem em R$? '))
dolar = real / 3.27
print('Com R$ {:.2f} voce pode comprar U${:.2f} dolares'.format(real, dolar))

