from modelos import Pessoa

nome = str(input("Insere o teu Nome: "))
idade = int(input("Insere o teu Idade: "))
peso = float(input("Insere o teu Peso: "))
altura = float(input("Insere o teu Altura: "))

p1 = Pessoa(nome, idade, peso, altura)

print(p1.nome)
print(p1.idade)
print(p1.peso)
print(p1.altura)

if idade < 21:
    for i in range(p1.idade, 21):
        p1.crescer()
    
    print(f"Aos 21 anos preve-se que tenhas {p1.altura}cm de altura")

else:
    print(f"A tua idade é maior que 21 anos a partir daqui já é so para baixo =)")