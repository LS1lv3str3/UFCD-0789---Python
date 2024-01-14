'''
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. 
'''
num_1 = int(input("Introduza um numero: "))

if num_1 < 0:
    print("O numero é negativo")
elif num_1 > 0:
    print("O numero é positivo")
else:
    print("O numero é igual a 0")