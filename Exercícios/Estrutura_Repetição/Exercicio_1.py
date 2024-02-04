'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. 
'''

num = float(input("Insere uma nota entre 0 e 10!\nNota = "))

while num < 0 or num > 10:
    print("Por favor insere um numero entre 0 e 10")
    num = float(input("Insere uma nota entre 0 e 10!\nNota = "))
    
print("Nota registada com sucesso")

