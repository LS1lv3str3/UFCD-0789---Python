'''
Faça um Programa que leia três números e mostre o maior e o menor deles.
'''

num_1 = float(input("Introduz o Numero 1: "))
num_2 = float(input("Introduz o Numero 2: "))
num_3 = float(input("Introduz o Numero 3: "))

array = [num_1, num_2, num_3]

maior_valor = max(array)
menor_valor = min(array)

print(f"O maior Numero é {maior_valor}")
print(f"O maior Numero é {menor_valor}")