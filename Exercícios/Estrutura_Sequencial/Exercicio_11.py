'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    A) o produto do dobro do primeiro com metade do segundo .
    B) a soma do triplo do primeiro com o terceiro.
    C) o terceiro elevado ao cubo. 
'''
import math
num_1 = int(input("Digita um numero inteiro: "))
num_2 = int(input("Digita um numero inteiro: "))
num_3 = float(input("Digita um numero décimal: "))

calc_1 = (num_1 * 2) * (num_2 / 2)
calc_2 = (num_1 * 3) + num_3
calc_3 = num_3 ** 3

calc_A = round(calc_1, 2)
calc_B = round(calc_2, 2)
calc_C = round(calc_3, 2)

print(f"Soluções: \n A) {calc_A} \n B) {calc_B} \n C) {calc_C}")