'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e cointrataram-lhe para desenvolver o programa que calculará os reajustes.

    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% 
    
    Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento. 
'''
import math
salario_atual = float(input("Qual o seu salário atual? "))
percentual = ["20%", "15%", "10%", "5%"]

if salario_atual <= 280.00:
    valor_aumento = salario_atual * 0.20
    valor_aumento = round(valor_aumento , 2)
    salario_novo = salario_atual * 1.20
    salario_novo = round(salario_novo , 2)
    print(f"Salário Antigo = {salario_atual}€ \n Percentagem do aumento aplicado - {percentual[0]} \n Valor do aumento = {valor_aumento}€ \n Salario futuro = {salario_novo}€ ")

if 280.00 < salario_atual <= 700.00:
    valor_aumento = salario_atual * 0.20
    valor_aumento = round(valor_aumento , 2)
    salario_novo = salario_atual * 1.20
    salario_novo = round(salario_novo , 2)
    print(f"Salário Antigo = {salario_atual}€ \n Percentagem do aumento aplicado - {percentual[1]} \n Valor do aumento = {valor_aumento}€ \n Salario futuro = {salario_novo}€ ")

if 700.00 < salario_atual <= 1500:
    valor_aumento = salario_atual * 0.20
    valor_aumento = round(valor_aumento , 2)
    salario_novo = salario_atual * 1.20
    salario_novo = round(salario_novo , 2)
    print(f"Salário Antigo = {salario_atual}€ \n Percentagem do aumento aplicado - {percentual[2]} \n Valor do aumento = {valor_aumento}€ \n Salario futuro = {salario_novo}€ ")

if salario_atual > 1500:
    valor_aumento = salario_atual * 0.20
    valor_aumento = round(valor_aumento , 2)
    salario_novo = salario_atual * 1.20
    salario_novo = round(salario_novo , 2)
    print(f"Salário Antigo = {salario_atual}€ \n Percentagem do aumento aplicado - {percentual[3]} \n Valor do aumento = {valor_aumento}€ \n Salario futuro = {salario_novo}€ ")