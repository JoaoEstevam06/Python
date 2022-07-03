from datetime import date

atual = date.today().year
nasc = int(input("Digite seu ano de nascimento: "))
idade = atual - nasc

if idade <= 9:
    print("Você tem {} anos de idade e é MIRIM.".format(idade))
elif idade <= 14:
    print("Você tem {} anos de idade e é INFANTIL.".format(idade))
elif idade <= 19:
    print("Você tem {} anos de idade e é JUNIOR.".format(idade))
elif idade <= 25:
    print("Você tem {} anos de idade e é SÊNIOR.".format(idade))
else:
    print("Você tem mais de 25 anos, então é MASTER.".format(idade))

