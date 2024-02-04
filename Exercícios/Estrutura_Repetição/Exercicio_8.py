'''
Faça um programa que leia 5 números e informe a soma e a média dos números.
'''

list=[]

for num in range(5):
    numero = int(input("Introduz um numero: "))
    
    list.append(numero)
    
soma = sum(list)
media = soma / len(list)

print(soma)
print(f"Soma = {soma}\nMedia = {media}")

