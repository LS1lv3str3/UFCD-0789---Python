'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. 
'''

horas_trabalhadas = float(input("Quantas horas trabalhaste este mês? \n Qty Horas = "))
valor_hora = float(input("Qual o teu valor por hora? \n Valor p/ hora = "))

salario = horas_trabalhadas * valor_hora

print(f"O teu salário ao final por mês é {salario:g}€")