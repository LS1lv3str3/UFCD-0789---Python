'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120 
'''

num = int(input("Qual o numero que queres calcular o fatorial?\nNumero --> "))

fatorial = 1

for i in range(1, num+1):
    fatorial *= i
print(fatorial)