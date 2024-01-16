'''
Faça um Programa que leia três números e mostre-os em ordem decrescente. 
'''
num_1 = float(input("Introduz o numero 1: "))
num_2 = float(input("Introduz o numero 2: "))
num_3 = float(input("Introduz o numero 3: "))

if num_1 > num_2 and num_1 > num_2 and num_2 > num_3:
    print(f"Ordem decrescente: Numero 1 = {num_1}, Numero 2 = {num_2}, Numero 3 = {num_3}")
    
elif num_1 > num_2 and num_1 > num_2 and num_2 < num_3:
    print(f"Ordem decrescente: Numero 1 = {num_1}, Numero 3 = {num_3}, Numero 2 = {num_2}")
    
elif num_2 > num_1 and num_2 > num_1 and num_1 > num_3:
    print(f"Ordem decrescente: Numero 2 ={num_2}, Numero 1 ={num_1}, Numero 3 ={num_3}")
    
elif num_2 > num_1 and num_2 > num_3 and num_1 < num_3:
    print(f"Ordem decrescente: Numero 2 = {num_2}, Numero 3 = {num_3}, Numero 1 = {num_1}")

elif num_3 > num_1 and num_3 > num_2 and num_1 < num_2:
    print(f"Ordem decrescente: Numero 3 = {num_3}, Numero 2 = {num_2}, Numero 1 = {num_1}")
else:
    print(f"Ordem decrescente: Numero 3 = {num_3}, Numero 2 = {num_2}, Numero 1 = {num_1}")
