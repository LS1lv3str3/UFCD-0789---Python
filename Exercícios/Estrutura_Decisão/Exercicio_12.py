'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que:
    os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 
    3% para o Sindicato 
    FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
    O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
    O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% 
    Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

            Salário Bruto: (5 * 220)        : R$ 1100,00
            (-) IR (5%)                     : R$   55,00  
            (-) INSS ( 10%)                 : R$  110,00
            FGTS (11%)                      : R$  121,00
            Total de descontos              : R$  165,00
            Salário Liquido                 : R$  935,00
'''

total_horas = float(input("Quantas horas trabalhaste este mês? \n Total Horas = "))
valor_hora = float(input("Qual o teu valor? \n Valor Hora = "))

salario_bruto = valor_hora * total_horas

def imposto_IR(salario_bruto): #CALCULO DO IMPOSTO IR
    if 0 < salario_bruto <= 900:
        taxa = 0.0
    if 900 < salario_bruto <= 1500:
        taxa = 0.05
    if 1500 < salario_bruto <= 2500:
        taxa = 0.10
    if salario_bruto > 2500:
        taxa = 0.20

    taxaP = taxa * 100
    imposto = taxa * salario_bruto 
    return imposto, taxaP


valor_IR = imposto_IR(salario_bruto)[0]
taxa_P = imposto_IR(salario_bruto)[1]
imposto_INSS = salario_bruto * 0.10
imposto_FGTS = salario_bruto * 0.11

total_discontos = imposto_INSS + valor_IR
salario_liquido = salario_bruto - total_discontos

print(f"Salário Bruto: {salario_bruto}€ \n  - IR ({taxa_P}%) = {valor_IR}€ \n  - INSS(10%) = {imposto_INSS}€ \n- FGTS (11%) = {imposto_FGTS}€ \n Total Discontos = {total_discontos}€ \n\n Salário Liquido = {salario_liquido}€")
