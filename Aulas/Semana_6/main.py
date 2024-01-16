'''
A Semana 5 foi fazer os Exercícios que iniciamos na Semana 4
'''
'''
EXTRA AULA
from datetime import datetime

minf = datetime.now().time().minute + 1
c = 0
while True:
    # print(datetime.now().time().second)
    
    if datetime.now().time().second == 59:
        c += 1
    
    if datetime.now().time().minute >= minf:
        break

print(c)
'''
from pessoa import Pessoa

p1 = Pessoa("Carlos", 20, "Masculino")

print(p1) #Print de toda as caracteristicas do objeto
print(p1.nome) #Print do nome
print(p1.idade) #Print do idade
print(p1.genero) #Print do genero

print("-----------------------------")

p2 = Pessoa("Maria", 20, "Feminino")

print(p2) #Print de toda as caracteristicas do objeto
print(p2.nome) #Print do nome
print(p2.idade) #Print do idade
print(p2.genero) #Print do genero

print("-----------------------------")

p3 = p1 #Estamos a criar um objeto igual ao p1

p3.nome = "Paulo"

print(p3)
print(p1)

#O print será o mesmo porque foi criado uma referencia p3=p1
#Os objetos mutaveis são todos aqueles que conseguimos alterar os seus valores sem criar referencias, por exemplo, arrays, dicionarios etc..

def mudar_nome(novo_nome:str, pessoa:Pessoa):
    pessoa.nome = novo_nome
    
print(p1.nome)

mudar_nome("Rui", p1) #mudados o partametro nome da calsse Pessoa na função porque a class é mutavel

print(p1.nome)

print("-----------------------------")

print(p1.idade)
print(p2.idade)

print("-----------------------------")

p1.envelhecer(10)
print(p1.idade)
print(p2.idade)

print("-----------------------------")

p1.envelhecer() #é equivalente a ter p1e«.envelhecer = 1
print(p1.idade)
print(p2.idade)