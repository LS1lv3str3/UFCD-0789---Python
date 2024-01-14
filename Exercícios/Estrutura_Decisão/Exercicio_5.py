'''
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez. 
'''

nota_1 = float(input("Qual a tua nota 1? "))
nota_2 = float(input("Qual a tua nota 2? "))

media = (nota_1 + nota_2) / 2

if 7 <= media >= 9.9 :
    print(f"Aluno APROVADO com média de: {media}")
else:
    print(f"Aluno REPROVADO com média de: {media}")
    
if media == 10:
    print(f"Aluno APROVADO COM Distinção")
