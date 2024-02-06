from modelos import Retangulo

ladoA = int(input("Introduz o lado A: "))
ladoB = int(input("Introduz o lado B: "))

r1 = Retangulo(ladoA, ladoB)

r1.mudarLados(novo_ladoA = int(input("Introduz o Novo Lado A: ")) , novo_ladoB= int(input("Introduz o Novo Lado B: ")) )

print(f"O novo lado A = {r1.ladoA}\nO novo lado B = {r1.ladoB}")

area = r1.calcArea()
perimetro = r1.calcPer()

print(f"A area do novo retangulo = {area}\nO perimetro do novo Retangulo = {perimetro}")
    