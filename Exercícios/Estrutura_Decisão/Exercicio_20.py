'''
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:

    A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    A mensagem "Aprovado com Distinção", se a média for igual a 10. 


'''
import math

notas = [
    float(input("Introduz a nota 1: ")),
    float(input("Introduz a nota 2: ")),
    float(input("Introduz a nota 3: "))
]

def calcular_media(nota):
    
    media = (nota[0] + nota[1] + nota[2]) / 3
            
    return round(media , 2)

if calcular_media(notas) == 10:
    print(f"Aprovado com DISTINÇÃO com média = {calcular_media(notas)}")

elif calcular_media(notas) > 7:
    print(f"Tiveste média de: {calcular_media(notas)}\n Foste APROVADO! Parabéns!!")

else:
    print(f"Tiveste média de: {calcular_media(notas)}\n Foste REPROVADO!")