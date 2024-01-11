'''
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área
'''
import math

raio = float(input("Qual o raio do circulo que desejas calcular a area? \n O raio é: "))

area_circulo = math.pi * raio * raio

print(f"A area do circulo são: {round(area_circulo, 2)} cm2")

