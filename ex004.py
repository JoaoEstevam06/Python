teste = input('Digite algo: ')

print('É um numero? {}'.format(teste.isnumeric()))
print('Contem somente espaco? {}'.format(teste.isspace()))
print('É alphanumerico? {}'.format(teste.isalnum()))
print('Esta em maiusculo? {}'.format(teste.isupper()))
print('Esta em minusculo? {}'.format(teste.islower()))
print('Esta capitalizada? {}'.format(teste.istitle()))

