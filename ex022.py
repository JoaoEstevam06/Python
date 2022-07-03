"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras MAIÚSCULAS
- O nome com todas as letras minúsculas
- Quantas letras ao todo (sem considerar espaço)
- Quantas letras tem o primeiro nome
"""
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculo é: {}'.format(nome.upper()))
print('Seu nome em minúsculo é: {}'.format(nome.lower()))
print('Seu nome contém {} letras!'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome contém {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
