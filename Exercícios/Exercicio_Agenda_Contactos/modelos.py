class Contactos:
    
    def __init__(self, nome:str, telefone:str, email:str=None, dataNas:str = None):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        self.__dataNas = dataNas
    
    def mostrarContacto (self):
        listaContactos = [self.__nome, self.__telefone, self.__email, self.__dataNas]      
        return listaContactos
    
    def editContacto(self, novo_nome:str = None, novo_telefone:str = None, email:str=None, dataNas = None):
        
        if novo_nome is not None:
            self.__nome = novo_nome
            
        if novo_telefone is not None:
            self.__telefone = novo_telefone
            
        if self.__email is not None:
            self.__email = email
        
        if self.__dataNas is not None:
            self.__dataNas = dataNas

    def addListaContacto(self, nome, telefone, email, dataNas):
        
        file = open("Lista_De_Contactos.csv", "a")
        contacto = f"{nome}\t{telefone}\t{email}\t{dataNas}"
        file.write(contacto + "\n")
        file.close()
       
        
        
        