'''
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

'''

n = int(input("Quantos numeros tem o teu conjunto? "))

list =[]

for i in range(0, n):
    numero = int(input(f"Introduz o {i + 1}º numero do teu conjunto: "))
    
    list.append(numero)

print(f"O teu conjuno é {list}\n Menor numero --> {min(list)}\n Maior numero --> {max(list)}\n A soma de todos os numeros do conjunto = {sum(list)}")