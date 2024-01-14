'''
Faça um Programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em:
    latas de 18 litros custam R$ 80,00
    galões de 3,6 litros custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

import math

area = float(input("Quantos metros quadrados tem a area que deseja pitar?? "))

litros_lata = 18
total_area_pLata = float(18 * 6)
preco_lata = 80

litros_galao = 3.6
total_area_pGalao = float(3.6 * 6)
preco_Galao = 25

#Calculos apenas Latas
total_latas = math.ceil(area / total_area_pLata)
preco_total_latas = total_latas * preco_lata

#Calculos apenas galoes
total_galoes = math.ceil(area / total_area_pGalao)
preco_total_galoes = total_galoes * preco_Galao

#Descobrir o desperdicio
litros_Nec = (area / 6) * 1.1   
rest_lata = litros_Nec % litros_lata
latas_Nec = math.floor(litros_Nec / litros_lata)
galoes_Nec = math.ceil (litros_Nec % (rest_lata / litros_galao))
preco_Misturado = (latas_Nec * preco_lata) + (galoes_Nec * preco_Galao)

print(f"Para {area}m²\n Há 3 opções: \n - {total_latas} latas com um custo de {preco_total_latas}€ \n - {total_galoes} galoes com um custo de {preco_total_galoes}€ \n - {latas_Nec} latas + {galoes_Nec} galoes com um custo de {preco_Misturado}€")





