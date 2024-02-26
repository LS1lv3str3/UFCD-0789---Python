from modelos import Contactos

agenda = [[]]

c1 = Contactos("Lucas", "987978769")

print(c1.mostrarContacto())

c1.addListaContacto("Lucas", "987978769", email= None, dataNas=None)

print(c1.mostrarContacto())

