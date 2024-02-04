'''
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo. 
'''

n = int(input("Digita o valor de termos que queres que seja representado o Fibonacci: "))

termo_anterior = 1
termo_atual = 0

for i in range(n):
    proximo_termo = termo_anterior + termo_atual
    print(proximo_termo)
    
    termo_anterior = termo_atual
    termo_atual = proximo_termo