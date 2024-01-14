'''
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
import math

area = float(input("Quantos metros quadrados tem a area que deseja pitar?? "))

total_area_p_lata = 18 * 3
preco_lata = 80

total_latas = math.ceil(area / total_area_p_lata) # Numero de total de latas arredondado em excesso
preco_total = total_latas * preco_lata

print(f"Para {area}m² irá precisar de {total_latas} latas com um custo de {preco_total}€")