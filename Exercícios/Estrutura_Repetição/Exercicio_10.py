'''
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles. 
'''

num1 = int(input("Introduz um numero: "))
num2 = int(input("Introduz um numero: "))

numerosTodos = ''
for numeros in range(num1 + 1 ,num2):
    numerosTodos += f" {str(numeros)}"

print(numerosTodos)
    


