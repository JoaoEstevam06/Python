numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
#print('O resultado foi: {}'.format(resultado))
if resultado == 0:
    print('O número {} é par!'.format(numero))
else:
    print('O número {} é impar!'.format(numero))
