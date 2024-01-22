'''
Faça um Programa que peça um número e informe se o número é inteiro ou decimal

'''
num = float(input("Introduz um numero: "))

round_num = round(num)

if num == round_num:
    print("O numero introduzido é inteiro")
else:
    print("O numero introduzido é decimal")


