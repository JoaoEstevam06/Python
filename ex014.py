

gc = float(input('Quantos graus está fazendo nesse momento? '))
gf = gc * 1.8 + 32
gk = gc + 273.15
print('A conversão de Graus Celcios {:.2f} p/ Fahrenheit nesse momento é: {:.2f} '.format(gc, gf))
print('E convertido p/ Graus Kelvin fica {:.2f}GK'.format(gk))