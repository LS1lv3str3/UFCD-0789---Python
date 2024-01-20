'''
Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
'''

ano = int(input("Intoduz um ano qualquer: "))

while True:
    if ano % 4 == 0:
        print("O ano introduzido é um ano bissexto, ou seja, terá 366 dias")
    
    else:
        print("O ano introduzido não é um ano bissexto, ou seja, terá 365 dias")
    break
        
        