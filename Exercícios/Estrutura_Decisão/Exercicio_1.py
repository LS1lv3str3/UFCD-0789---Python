'''
Faça um Programa que peça dois números e imprima o maior deles. 
'''
num_1 = float(input("Introduza um numero: "))
num_2 = float(input("Introduza um numero: "))

if num_1 == num_2:
    print(f"Os numeros são iguais")
elif num_1 > num_2:
    print(f"O numero maior é {num_1}")
else:
    print(f"O numero maior é {num_2}")