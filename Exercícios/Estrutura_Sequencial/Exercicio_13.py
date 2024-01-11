'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7 
    
'''
import math

gen = input("Digite o seu sexo: \n M ou F: ")

while gen != 'M' and gen != 'F':
    print("Insira o seu sexo de forma incorreta \n Apenas insira M ou F: ")
    gen = input("Digite o seu sexo: \n M ou F: ")
    
if gen == 'M':
    altura = float(input("Insere a tua altua em metros \n Altura = "))
    peso = (72.7 * altura) - 58
    peso_Ideal_M = round(peso, 2)
    print(f"O seu peso Ideal é {peso_Ideal_M}")
    
if gen == 'F':
    altura = float(input("Insere a tua altua em metros \n Altura = "))
    peso = (62.1 * altura) - 44.7
    peso_Ideal_F = round(peso, 2)
    print(f"O seu peso Ideal é {peso_Ideal_F}")
    