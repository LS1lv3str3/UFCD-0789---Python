'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 
'''

letra = input("Introduz uma letra: ")

vogais = ["a", "e", "i", "o", "u"]

if letra in vogais or vogais.upper:
    print(f"A letra {letra} é uma Vogal")
else:
    print(f"A letra {letra} é uma Consoante.")