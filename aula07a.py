n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
soma = n1+n2
mult = n1*n2
div = n1/n2
divint = n1//n2
pot = n1**n2
resto = n1%n2
print('O resultado da soma é: {}'.format(soma))
print('A multiplicacao é: {}'.format(mult))
print('A divisao é: {:.3f}\nE a divisao inteira é: {}'.format(div, divint))
print('E aqui a potencia: {}\nMais o resto: {}'.format(pot, resto))
