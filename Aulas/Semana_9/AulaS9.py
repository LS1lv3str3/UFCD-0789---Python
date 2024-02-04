'''
() - tuplo - o tuplo é imutável 

[] - lista

{} - set

{:} - diicionario
'''
print("TUPLOS \n\n")
tp = ("Lucas", 12, "ATEC")

print(tp[0])
print(tp[1])
print(tp[2])

print("------------------------------")
for i in tp:
    print(i)

print("------------------------------")  
tp = tp + (4, ) #O tuplo é imutavel mas neste exemplo é rescrito com o numero 4 .
print(tp)

print("----------------ARRAYS-----------------\n\n") 

lista = [0,1,2,3,4,5,6,7,8,9]

print(lista[0]) # Primeiro indice da lista 
print(lista[4])

print("------------------------------\n")

print("len - demonstra o tamanho da lista")
print(len(lista)) #Retorna o tamanho da lista
print("\n")

print("append - demonstra o tamanho da lista")
lista.append(232) #Adiciona o numero 232 à lista
print(lista)
print("\n")

print("insert - adiciona a um indice um determinado valor")
lista.insert(2, 999) #adiciona o numero 999 ao indice 2 deixando de ser 2
print(lista)
print("\n")

print("remove - remove o valor especifico")
lista.remove(999)
print(lista)
print("\n")

print("pop - remove o indice especifico")
lista.pop(2)
print(lista)
print("\n")

print("step - apresenta os valores do intervalo especifico de indices 'lista[1_indice:ultimo_indice]'")
print(lista)
print(lista[:5])
print("\n")

print("lista slicing apresenta os valores de um determinado intervalo de indices de x em x posições 'lista[1_indice:ultimo_indice]:saltos que queremos que de'")
print(lista)
print(lista[0:6:2])
print("\n")

print("sort - ordena a lista de maneira que queremos ")
print(lista)
lista.sort(reverse=True)
print(lista)
print("\n\n")

print("----------------SETS-----------------\n") 
'''
Os sets nao permitem ter elementos repetidos, nao conseguimos aceder a um indice especifico
'''

myset = {3, 4, 1, 2, 5, 2, 6}
print(myset)
print("\n")

print("add - adiciona o elemento que queremos")
myset.add(50)
print(myset)
print("\n")

print("remove - retira o elemento que queremos")
myset.remove(3)
print(myset)
print("\n\n")

print("------------------------------")

r1 = {
    "Leite",
    "Oleo",
    "Ovos",
    "Sal",
    "Queijo"
}

r2 = {
    "Farinha",
    "Ovos",
    "Açucar",
    "Fermento",
    "Chocolate",
    "Manteiga"
    }

print("union - faz a união entre os 2 sets")
print(r1.union(r2))
print("\n")

print("intersection -mostra o que os 2 têm em cômum")
print(r1.intersection(r2))
print("\n")

print("diferece - faz a diferença entre os 2 conjuntos")
print(r1.difference(r2))
print("\n")

print("symmetric_difference - apaga o que é em comum entre os 2")
print(r1.symmetric_difference(r2))
print("\n")

print("intersection_update - Faz update ao set selecionado")
print(r1)
print(r2)
r1.intersection_update(r2)
print("\n\n")

print("----------------DICT-----------------\n\n") 

dict = {"key":"Value", "key2":"Value"}
print(dict)
print("\n\n")

print(dict["key"])

dict2 = {
    "Hommer": "Pai da familia",
    "Marge": "Mãe da familia",
    "Bart": "Filho mais velho",
    "Lisa": "Filha do meio",
    "Maggie": "Bebe da familia"
    }

print("Par aceder ao valor do dicionario acedemos à key")
print("Hommer", dict2["Hommer"])
print("\n")

#Adicionar um elemento ao dicionario 
dict2["Moe"] = ["Dono do Bar"]
print(dict2)
print("\n")

print("pop - apaga a key e o value da key selecionada ")
print(dict2)
dict2.pop("Moe")
print(dict2)
print("\n")

print(".keys demosntra as keys ")
print(dict2.keys())
print("\n")

print(".values demosntra aos values ")
print(dict2.values())
print("\n")

for i in dict2.keys():
    print(i)
print("\n\n") 

for i in dict2.values():
    print(i)
print("\n\n")
    
for i in dict2.items():
    print(i)
print("\n\n")

print("----------------unpack-----------------\n\n") 

tp = ("Lucas", 12, "ATEC")
