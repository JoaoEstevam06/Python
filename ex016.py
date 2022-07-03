"""
Crie um programa que leia um numero Real qualquer pelo teclado
e mostre na tela a sua porção inteira.
ex: Digite um número: 6.127.
O numero 6.127 tem a parte inteira 6
GO!!!
"""
from math import trunc
num = float(input('Digite um número: '))
print('A parte inteira de {0} é: {1}'.format(num, trunc(num)))

