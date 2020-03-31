class Carte:
    def __init__(self,id,titlu,descriere,autor):
        self.__id = id
        self.__titlu = titlu
        self.__descriere = descriere
        self.__autor = autor
    
    def get_id(self):
        return int(self.__id)
    
    
    def get_titlu(self):
        return self.__titlu
    
    
    def get_descriere(self):
        return self.__descriere
    
    
    def get_autor(self):
        return self.__autor
    
    
    def __eq__(self,other):
        return self.__id == other.__id
    
    
    def __str__(self):
        return str(self.__id)+" "+self.__titlu+" "+self.__descriere+" "+self.__autor
    
    @staticmethod
    def read_carte(line):
        parts = line.split(';')
        return Carte(int(parts[0].strip()),parts[1].strip(),parts[2].strip(),parts[3].strip())
        
    @staticmethod
    def write_carte(carte):
        return str(carte.__id) + ';' + str(carte.__titlu) + ';' + str(carte.__descriere) + ';' + str(carte.__autor)
    
    
class Client:
    def __init__(self,c_id,nume,CNP):    
        self.__c_id = c_id
        self.__nume = nume
        self.__CNP = CNP
    
    
    def get_id(self):
        return self.__c_id
    
    
    def get_nume(self):
        return self.__nume
    
    
    def get_CNP(self):
        return self.__CNP
    
    
    def __eq__(self,other):
        return self.__c_id == other.__c_id
    
    
    def __str__(self):
        return str(self.__c_id)+" "+self.__nume+" "+str(self.__CNP)
    
    @staticmethod
    def read_client(line):
        parts = line.split(';')
        return Client(int(parts[0].strip()),parts[1].strip(),parts[2].strip())

    @staticmethod
    def write_client(client):
        return str(client.__c_id) + ';' + str(client.__nume) + ';' + str(client.__CNP)
        
        
        
class Inchiriere:
    def __init__(self,client,carte,e_inchiriat=1):
        """
        e_inchiriat: 1 - pt relatie existenta
                     0 - pt ca o carte e returnata
        """
        self.__client = client
        self.__carte = carte
        self.__e_inchiriat = e_inchiriat
        
        
    def get_id(self):
        return str(self.__client.get_id())+"_"+str(self.__carte.get_id())
    
    
    def get_client(self):
        return self.__client
    
    
    def get_carte(self):
        return self.__carte
    
    
    def get_e_inchiriat(self):
        return self.__e_inchiriat
    
    
    def returneaza_cartea(self):
        self.__e_inchiriat = 0
        
    
    def __str__(self):
        return str(self.__client.get_id())+"_"+str(self.__carte.get_id())+"_"+str(self.__e_inchiriat)
    
    @staticmethod   
    def read_inchiriere(line):
        parts = line.split(';')
        return Inchiriere(Client(parts[0].strip(),"",""),Carte(parts[1].strip(),"","",""),parts[2].strip())
    
    @staticmethod
    def write_inchiriere(inchiriere):
        return str(inchiriere.__client.get_id()) +';'+ str(inchiriere.__carte.get_id()) +';'+ str(inchiriere.__e_inchiriat)
        
        
class Ceva:
    def __init__(self,nume,prenume,varsta):
        self.__nume = nume
        self.__prenume = prenume
        self.__varsta = varsta

    def get_nume(self):
        return self.__nume


    def get_prenume(self):
        return self.__prenume


    def set_nume(self, value):
        self.__nume = value


    def set_prenume(self, value):
        self.__prenume = value


    def del_nume(self):
        del self.__nume


    def del_prenume(self):
        del self.__prenume

    

        
        
        
        
        
                