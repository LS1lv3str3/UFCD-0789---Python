'''
Faça um Programa que pergunte em que turno você estuda.
Peça para digitar:
    M-Manhã
    V-Tarde
    N- Noite
    
Imprima a mensagem 
    "Bom Dia!"
    "Boa Tarde!"
    "Boa Noite!"
    "Valor Inválido!" 

'''
while True:
    horario = input("Estudas em que horário? Escreve a baixo 1 dos seguintes horários: M - Manhã, T - Tarde ou N - Noite \n Horario de estudo - ")

    if horario == "M" or horario == 'm':
        print("Bom dia!")
        break
        
    elif horario == 'T' or horario == 't':
        print("Boa Tarde!")
        break
        
    elif horario == 'N' or horario == 'n':
        print("Boa Noite!")
        break

    else:
        print("Por Favor Insere um dos hoários disponiveis!")
