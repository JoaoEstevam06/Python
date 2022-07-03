"""
escreva um programa que laia um valor em metros e exiba convertito em
centimetros e milimetros
"""
metros = float(input('Digite a metragem: '))
kms = metros*10000
cent = metros*100
mili = metros*1000
print('O valor de {0} metros convertido em cm é: {1}\nE em mm é: {2}'.format(metros, cent, mili))
print('O valor em kilometros é: {}'.format(kms))