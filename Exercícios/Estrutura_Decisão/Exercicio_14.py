'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

      Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0        A
      Entre 7.5 e 9.0         B
      Entre 6.0 e 7.5         C
      Entre 4.0 e 6.0         D
      Entre 4.0 e zero        E

    O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E. 
    
'''

nota_1 = float(input("Qual a tua nota 1: "))
nota_2 = float(input("Qual a tua nota 2: "))

media = (nota_1 + nota_2) / 2

if 0 <= media <= 4.0:
    print(f"Nota 1: {nota_1} \n Nota 2: {nota_2} \n O teu conceito é: E \n Resultado: Reprovado")

if 4.0 < media <= 6.0:
    print(f"Nota 1: {nota_1} \n Nota 2: {nota_2} \n O teu conceito é: D \n Resultado: Reprovado")
    
if 6.0 < media <= 7.5:
    print(f"Nota 1: {nota_1} \n Nota 2: {nota_2} \n O teu conceito é: C \n Resultado: Aprovado")

if 7.5 < media <= 9.0:
    print(f"Nota 1: {nota_1} \n Nota 2: {nota_2} \n O teu conceito é: B \n Resultado: Aprovado")
    
if 9.0 < media <= 10.0:
    print(f"Nota 1: {nota_1} \n Nota 2: {nota_2} \n O teu conceito é: A \n Resultado: Aprovado")