'''
Faça um programa que leia 5 números e informe o maior número. 
'''
maior_numero = None

for num in range(5):
    numero = int(input(f"Digite um número: "))

    if maior_numero is None or numero > maior_numero:
        maior_numero = numero
    
print(f"O maior número é: {maior_numero}")

    
    