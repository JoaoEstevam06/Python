"""
faca um programa que leia um angulo qualquer
e mostre o valor de seno, cosseno e tangente do angulo
"""
from math import radians, sin, cos, tan
angulo = float(input('Digite um angulo qualquer: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O angulo de {} tem o seno: {:.2f}'.format(angulo, seno))
print('O angulo de {} tem o cosseno: {:.2f}'.format(angulo, cosseno))
print('O angulo de {} tem a tangente: {:.2f}'.format(angulo, tangente))



