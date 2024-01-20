'''
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
'''
from datetime import datetime

data = str(input("Que dia é hoje? "))

if data : 
    datetime.strptime(data, '%d/%m/%Y')
    print(f"{data} é uma data válida")
else:
    print(f"{data} é uma data inválida")