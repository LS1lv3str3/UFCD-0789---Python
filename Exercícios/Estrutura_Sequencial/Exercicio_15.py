'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que: 
são descontados 11% para o Imposto de Renda
8% para o INSS 
5% para o sindicato

Faça um programa que nos dê:
    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    
    calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

'''

import math

numero_Horas = float(input("Quantas horas trabalhaste este mes? \n Horas trabalhadas = "))
valor_Hora = float(input("Qual o teu valor por hora? \n Valor por Horas = "))

salario_Bruto = numero_Horas * valor_Hora
valor_IR = salario_Bruto *  0.11
valor_INSS = salario_Bruto * 0.08
valor_Sindicato = salario_Bruto * 0.05
salario_Liquido = salario_Bruto - (valor_INSS + valor_IR + valor_Sindicato)

print(f"Salário Bruto = {salario_Bruto}€ \n Imposto Renda = {valor_IR}€ \n Imposto INSS = {valor_INSS}€ \n Valor Sindicato = {valor_Sindicato}€ \n Salário Líquido = {salario_Liquido}€")