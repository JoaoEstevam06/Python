nome = str(input("Qual é seu nome? "))
if nome == 'Hanzi':
    print('Que nome bonito!' )
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é tão popular no Brasil..')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino! ')
else:
    print('Seu nome é bem normal; ')
print('Tenha um bom dia, {}'. format(nome))