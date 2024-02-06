import modelos as m 

f1 = m.Fruta("Verde", 10, "Oval", "Pera", 1, "Lisa", True)
f2 = m.Fruta("Azul", 10, "Oval", "Morango", 1, "Lisa", True)
f3 = m.Fruta(cor = "Roxa",
             tamanho = float,
             formato = "Oval",
             nome = "Laranja",
             idade = 1,
             textura = "bla bla bla",
             comestivel = True)

f4 = m.Fruta("Maçã", "Vermelha", 10)
f5 = m.Fruta("Maçã", "Vermelha", 10, textura = "Lisa")

print(f1)
print(f5)

print("-----" * 10)
f12 = f1 

print(f1)
print(f12)

f12.nome = "Ana"
print(f1)
print(f12)


'''
As classes funcionam para atribuir diversos atributos predefinidos anteriormente (Quando se cria uma classe) para se atribuir aos objetos que vao contituir essas classes.
Com valores pre-definidos podemos criar objetos com os atributos que nao foram atribuidos na criação da Class.
Podemos atribuir novos objetos iguais a outros objetos ja definidos.

'''

g = m.Gato("Tom",20)
print(g)