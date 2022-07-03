"""
faca um programa que leia o preco de um produto e mostre seu
novo preco com 5% de desconto
"""
preco = float(input('Qual preco do produto? '))
desc = preco - (preco * 5 / 100)
print('O preco {:.2f} com 5% de desconto é: {:.2f}'.format(preco, desc))
