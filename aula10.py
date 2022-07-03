'''nome = str(input('Qual é seu nome? ')).lower().strip()
if nome == 'hanzi':
    print('Que nome lindo voce tem! '.format(nome.lower('hanzi')))
else:
    print('Seu nome é tão normal! ')
print('Bom dia! {}'.format(nome.capitalize()))
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A média é: {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa, parabéns!!' )
else:
    print('Sua média foi ruim, estude mais!')
