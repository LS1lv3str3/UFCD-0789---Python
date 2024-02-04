""" 
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
O usuário deve informar de qual numero ele deseja ver a tabuada. 
A saída deve ser conforme o exemplo abaixo:

    Tabuada de 5:
    5 X 1 = 5
    5 X 2 = 10
    ...
    5 X 10 = 50 
"""
tabuada = int(input("Qual a tabuada que desejas calcular?\nTabuado do: "))

if 0 <= tabuada <= 10:
    for multi in range(0,11):
        
        resultado = tabuada * multi
        print(f'{tabuada} x {multi} = {resultado}')

else:
    print("Insere uma tabuada entre 0 e 10")
