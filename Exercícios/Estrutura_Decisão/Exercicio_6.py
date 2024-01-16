'''
Faça um Programa que leia três números e mostre o maior deles. 
'''

num_1 = int(input("Digite um numero 1 : "))
num_2 = int(input("Digite um numero 2 : ")) 
num_3 = int(input("Digite um numero 3 : "))

if num_1 > num_2 and num_1 > num_3:
    print(f"O numero maior é o {num_1}")
    
elif num_2 > num_1 and num_2 > num_3:
    print(f"O numero maior é o {num_2}")

else:
    print(f"O numero maior é o {num_3}")