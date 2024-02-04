'''
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares. 
'''

inputUser = []
pares = []
impares = []

for posicao in range(1,11):
    numeros = int(input(f"Insere o {posicao} numero: "))
    inputUser.append(numeros)

for i in inputUser:
    if i % 2 == 0: 
        pares.append(i)
    else:
        impares.append(i)

print(f"Nos {posicao} numeros introduzidos existe:\n{len(pares)} --> Pares\n{len(impares)} --> impares")
    
    