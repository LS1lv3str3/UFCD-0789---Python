'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?" 

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder:
    positivamente a 2 questões ela deve ser classificada como "Suspeita"
    entre 3 e 4 como "Cúmplice" 
    5 como "Assassino"
    Caso contrário, ele será classificado como "Inocente". 
'''

print("Houve um Homicidio e ao que parece tu estavas no local so crime por favor tens de seguir o seguinte interrogatório")

respostas = [str(input("Telefonou para a vítima?")),
             str(input("Esteve no local do crime?")),
             str(input("Mora perto da vítima?")),
             str(input("Devia para a vítima?")),
             str(input("Já trabalhou com a vítima?")),
             ]

def verificar_respostas(res):
    resp_S = 0
    resp_N = 0
    
    for respostas in res:
    
        if respostas == 'S':
            resp_S += 1

            
        elif respostas == 'N':
            resp_N += 1
        
        else:
            print ("Por favor responda apenas com S ou N às questões")
            

    return resp_S, resp_N

sentenca = verificar_respostas(respostas)    

if sentenca[0] == 2:
    print(f" O resultado do seu interrogatório foi: \n Respostas positivas: {sentenca[0]} \n Respostas positivas: {sentenca[1]} \n A sua sentença é --> SUSPEITO")

if 3 < sentenca[0] <= 4:
    print(f" O resultado do seu interrogatório foi: \n Respostas positivas: {sentenca[0]} \n Respostas positivas: {sentenca[1]} \n A sua sentença é --> CÚMPLICE")
    
if sentenca[0] == 5:
    print(f" O resultado do seu interrogatório foi: \n Respostas positivas: {sentenca[0]} \n Respostas positivas: {sentenca[1]} \n A sua sentença é --> ACUSADO")
else:
    print(f" O resultado do seu interrogatório foi: \n Respostas positivas: {sentenca[0]} \n Respostas positivas: {sentenca[1]} \n A sua sentença é --> INOCENTE")
 