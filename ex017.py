"""
Faca um programa que leia o comprimento do cateto oposto
e do cateto adjascente de um triangulo retangulo.
calcule e mostre o comprimento da hipotenusa
"""
from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjascente: '))
hip = hypot(co, ca)
print('A hipotenusa dos catetos é: {:.2f}'.format(hip))


