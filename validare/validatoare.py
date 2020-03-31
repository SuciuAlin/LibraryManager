from erori.exceptii import ValidError
from domeniu.enititati import Client



class ValidatorCarte:
    def __init__(self):
        pass
    
    
    def valideaza_carte(self,carte):
        """
        descrierea poate lipsi
        """
        erori = ""
        if carte.get_id() < 1:
            erori += "id invalid!\n"
        if carte.get_titlu() == "":
            erori += "titlu invalid!\n"
        if carte.get_autor() == "":
            erori +="autor invalid!\n"
        if len(erori)>0:
            raise ValidError(erori)
        

class ValidatorClient:
    def __init__(self):
        pass
    
    def valid_CNP(self,CNP):
        #adaugat conditiile ca cnp ul sa fie corect
        if True:
            return 1
        else:
            return 0
    
        
    def valideaza_client(self,client):
        erori = ""
        if client.get_id() < 1:
            erori += "id invalid\n"
        if client.get_nume() == "":
            erori += "nume invalid\n"
        if self.valid_CNP(client.get_CNP()) == 0:
            erori += "CNP invalid"
        if len(erori) > 0:
            raise ValidError(erori)
            
class ValidatorInchiriere:
    def __init__(self):
        pass
    
    
    def valideaza_inchiriere(self,inchiriere):
        erori = ""
        if inchiriere.get_e_inchiriat() != 0:
            if inchiriere.get_e_inchiriat() != 1:
                erori += "relatie invalida!\n"
        if len(erori)>0:
            raise ValidError(erori)

