'''
Altere o programa anterior para mostrar no final a soma dos números. 
'''

num1 = int(input("Introduz um numero: "))
num2 = int(input("Introduz um numero: "))

numerosTodos = 0
for numeros in range(num1 + 1 ,num2):
    numerosTodos += numeros

print(numerosTodos)