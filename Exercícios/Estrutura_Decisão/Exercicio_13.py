'''
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido. 
'''

while True:
    dia = int(input("Que dia é hoje? \n 1-Domingo \n 2- Segunda \n 3- Terça-Feira \n 4- Quarta-feira \n 5 - Quinta-feira \n 6 - Sexta-feira \n 7 - Sábado \n Dia da Semana: " ))
    match dia:
        case 1:
            print("Hoje é Ddomingo!")
            break
        case 2:
            print("Hoje é Segunda!")
            break
        case 3:
            print("Hoje é Terça-Feira")
            break
        case 4:
            print("Hoje é Quarta-Feira")
            break
        case 5:
            print("Hoje é Quinta-Feira")
            break
        case 6:
            print("Hoje é Sexta-Feira")
            break
        case 7:
            print("Hoje é Sábado")
            break
        case other:
            print("Introduza um dia de forma válida")
            
        
