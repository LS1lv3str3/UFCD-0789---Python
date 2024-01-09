"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média. 
"""

nota_1 = int(input("Introduz a tua nota de Jan. & Fev.: "))
nota_2 = int(input("Introduz a tua nota de  Mar. & Abr.: "))
nota_3  = int(input("Introduz a tua nota de Maio & Jun.: "))
nota_4 = int(input("Introduz a tua nota de jul. & Ago.: "))

media = float((nota_1 + nota_2 + nota_3 + nota_4) / 4)

print(f"A tua média nos primeiros  meses do ano foi {media} valores")
