nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota:"))
media = (nota1 + nota2) / 2

if media <= 4.9:
    print("Sua média foi: {}\nAluno REPROVADO, tente outra vez!".format(media))
elif media <= 5.9:
    print("Sua média foi: {}\nAluno em RECUPERAÇÃO!".format(media))
else:
    print("Aluno APROVADO com a média: {} \nPARABÉNS".format(media))
