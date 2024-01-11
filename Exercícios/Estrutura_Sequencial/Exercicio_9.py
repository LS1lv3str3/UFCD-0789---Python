'''
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

    C = 5 * ((F-32) / 9). 
'''
import math

grau_Fah = float(input("Desejas converter graus Fahrenheit em graus Celsius? \n Graus Fahrenheit = "))
grau_Cel = 5 * ((grau_Fah - 32) / 9)

conversao = round(grau_Cel , 2)

print(f"{grau_Fah}ºF = {conversao}ºC")