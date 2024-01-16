'''
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. 
'''

produto_1 = input("Introduz o Produto 1: ")
produto_2 = input("Introduz o Produto 2: ")
produto_3 = input("Introduz o Produto 3: ")
preco_1 = float(input(f"Introduz o preço do {produto_1}: "))
preco_2 = float(input(f"Introduz o preço do {produto_2}: "))
preco_3 = float(input(f"Introduz o preço do {produto_3}: "))

precos = [preco_1, preco_2, preco_3]
  
if min(precos) == precos[0]:
    print(f"O produto mais barato é o {produto_1} que custa {preco_1}€")
elif min(precos) == precos[1]:
    print(f"O produto mais barato é o {produto_2} que custa {preco_2}€")
else:
    print(f"O produto mais barato é o {produto_3} que custa {preco_3}€")

