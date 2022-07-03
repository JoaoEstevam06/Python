"""
crie um algoritimo que leia um numero e mostre o seu dobro,
triplo e raiz quadrada
"""
num = int(input('Digite um numero: '))
dob = num*2
trip = num*3
raiz  = num**(1/2)
print('O dobro de {0} é: {1}\nO triplo de {0} é {2}\nE a raiz quadrada é: {3:.2f}'.format(num, dob, trip, raiz))