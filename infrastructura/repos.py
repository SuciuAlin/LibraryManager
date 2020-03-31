from erori.exceptii import RepoError
from domeniu.enititati import Client
from asyncore import write


class Repo:
    
    
    def __init__(self):
        self._entitati = {}
        
    
    def size(self):
        return len(self._entitati)
    
    
    def cauta(self,cheie):
        if int(cheie.get_id()) not in self._entitati:
            raise RepoError("id inexistent!\n"+ str(cheie.get_id()))
        for elem in self._entitati:
            if elem == cheie.get_id():
                return self._entitati[int(elem)]
            
            
    def modifica(self,elem_nou):
        if elem_nou.get_id() not in self._entitati:
            raise RepoError("id inexistent!\n")   
        self._entitati[elem_nou.get_id()] = elem_nou
    
    
    def adauga(self,elem):
        if elem.get_id() in self._entitati:
            raise RepoError("id existent!\n"+ str(elem.get_id()))
        self._entitati[elem.get_id()]=elem
    
    def __numara_nume(self,nume):
        nr = 0
        for i in self._entitati:
            nume_aux = self._entitati[i].get_nume().split("(")
            if nume_aux[0] == nume:
                nr += 1
        return nr
        
        #doar pentru client
    def adauga2(self,elem,nr=0):
        if elem.get_id() in self._entitati:
            raise RepoError("id existent!\n")
        nr = self.__numara_nume(elem.get_nume())
        if nr == 0:
            self.adauga(elem)
        else:
            self._entitati[elem.get_id()] = Client(elem.get_id(),elem.get_nume()+"("+str(nr+1)+")",elem.get_CNP())
            
            
            
    
    def elimina(self,cheie):
        if cheie not in self._entitati:
            raise RepoError("id inexistent!\n")
        
        self._entitati.pop(cheie,None)
    
    
    def get_all(self):
        return self._entitati
    

class FileRepo(Repo):
    
    def __init__(self,filename,read_entity,write_entity):
        Repo.__init__(self)
        self.__filename = filename
        self.__read_entity = read_entity
        self.__write_entity = write_entity
    
    def __read_all_from_file(self):
        self._entitati = {}
        with open(self.__filename,"r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    entitate = self.__read_entity(line)
                    self._entitati[entitate.get_id()] =  entitate
    
    def __write_all_to_file(self):
        with open(self.__filename,"w") as f:
            for entitate in self._entitati:
                f.write(self.__write_entity(self._entitati[entitate])+'\n')

    def adauga(self,entitate):
        self.__read_all_from_file()
        Repo.adauga(self, entitate)
        self.__write_all_to_file()
        
    def cauta(self, entitate):
        self.__read_all_from_file()
        Repo.cauta(self, entitate)
        
    def elimina(self,entitate):
        self.__read_all_from_file()
        Repo.elimina(self, entitate)
        self.__write_all_to_file()
    
    def modifica(self, entitate):
        self.__read_all_from_file()
        Repo.modifica(self, entitate)
        self.__write_all_to_file()
    
    def get_all(self):
        self.__read_all_from_file()
        return Repo.get_all(self)
    
    
class RepoFileCl():
    def __init__(self,filename,read_entity,write_entity):
        self.__filename = filename
        self.__read_entity = read_entity
        self.__write_entity = write_entity
        self.__aux = 'aux.txt'
        
        
    def adauga(self,element):
        with open(self.__filename,'a+') as f:
            f.write('\n'+str(element.get_id())+';'+element.get_nume()+';'+element.get_CNP())
    
    def elimina(self,element):
        
        with open(self.__aux,'w') as f2:
            pass
        
        with open(self.__filename,'r') as f1:
            with open(self.__aux,'a') as f2:
                lines = f1.readlines()
                for line in lines:
                    print(line)
                    print(line.split(';'))
                    if element != int(line.strip().split(';')[0]):
                        f2.write(line)
        
        
        with open(self.__filename,'w') as f1:
            f1.write("")
        
        with open(self.__aux,'r') as f1:
            with open(self.__filename,'a') as f2:        
                lines = f1.readlines()
                for line in lines:
                    f2.write(line)
        
    def cauta(self,element):
        with open(self.__filename,'r') as f1:
                lines = f1.readlines()
                for line in lines:
                    if element.get_id() == int(line.strip().split(';')[0]):
                        return self.__read_entity
    
import unittest
class TesteCeva(unittest.TestCase):
    def setUp(self):
        #class.repo=Repo(asdasd)
        pass
    def test1(self):
        self.assertEqual(1, 2)
        self.assertRaise 