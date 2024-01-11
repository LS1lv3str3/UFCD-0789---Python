'''
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. 
'''
import math

grau_Cel = float(input("Desejas converter graus Fahrenheit em graus Celsius? \n Graus Celsius = "))
grau_Fah = grau_Cel * 1.8 + 32

conversao = round(grau_Fah , 2)

print(f"{grau_Cel}ºC = {conversao}ºF")