from contacto import Contacto
from utils import DataError

class Agenda:
    
    def __init__(self):
        self.lista_contactos = []
    
    def add_contacto(self,
                     contacto: Contacto =  None,
                     nome: str = None,
                     telefone: int = None):
        
        if Contacto is not None and (nome is not None or telefone is not None):
            raise DataError("O contacto e o nome nao podem ser adicionados ao mesmo tempo!")
        
        if contacto is not None:
            self.lista_contactos.append(contacto)
        else:
            self.lista_contactos.append(Contacto(nome, telefone))
        
a = Agenda()

a.add_contacto(contacto =Contacto("Lucas", 96198456), nome = "Lucas", telefone = 96198456)
        
