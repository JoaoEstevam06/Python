"""
faca um programa que leia a largura e a altura de uma pared em
metros, calcule a sua area e a quantidade de tinta
necessario para pintar. sabendo que cada litro de trinta
pinta uma area de 2m
"""
altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = altura*largura
print('Voce precisa de {} L de tinta para concluir'.format(area))
