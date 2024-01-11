'''
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58 

'''
import math

print("CALCULADORA DO PESO IDEAL \n")

altura = int(input("Digite a tua altura em metros \n Altura = "))


peso = (72.7 * altura) - 58
peso_Ideal = round(peso, 2)


print(f"O se peso ideal é {peso_Ideal}Kg")

