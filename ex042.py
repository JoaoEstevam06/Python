lado1 = int(input("Digite o primeiro lado: "))
lado2 = int(input("Digite o segundo lado: "))
lado3 = int(input("Digite o terceiro lado: "))
if lado1 < lado2 + lado3 and lado2 < lado3 + lado1 and lado3 < lado1 + lado2:
    print("Os segmentos PODEM formar um triangulo!")
    if lado1 == lado2 == lado3:
        print("O triangulo é: EQUILÁTERO!")
    elif lado1 != lado2 != lado3 != lado1:
        print("O triangulo é: ESCALENO!")
    else:
        print("O triangulo é: ISOSCELES")
else:
    print("Não é um triangulo!")

