num1 = int(input("Digite o PRIMEIRO número: "))
num2 = int(input("Digite o SEGUNDO número: "))

if num1 > num2:
    print("O PRIMEIRO número é maior que o SEGUNDO número!")
elif num2 > num1:
    print("O SEGUNDO número é maior que o PRIMEIRO número!")
elif num1 == num2:
    print("Os números digitados são IGUAIS!")
else:
    print("Opção inválida.")
