from infrastructura.repos import Repo
from domeniu.enititati import Client, Carte
from validare.validatoare import ValidatorCarte
from sorts import shake_sort

class Teste:
    def __init__(self):
        pass
    
    
    def test_get_all(self):
        repoTest = Repo()
        assert(repoTest.get_all()=={})
    
    def test_size(self):
        repoTest = Repo()
        assert (repoTest.size() == 0)
    
    def test_adauga(self):
        repoTest = Repo()
        assert(repoTest.size()==0)
        repoTest.adauga(Client(1,"An J",3123))
        assert(repoTest.size()==1)
        assert(repoTest.get_all()[1].get_id()==1)
        assert(repoTest.get_all()[1].get_nume()=="An J")
        assert(repoTest.get_all()[1].get_CNP()==3123)
    
    def test_sterge(self):    
        repoTest = Repo()
        assert(repoTest.size()==0)
        client = Client(1,"An J",3123)
        repoTest.adauga(client)
        assert(repoTest.size()==1)
        assert(repoTest.get_all()[1].get_id()==1)
        assert(repoTest.get_all()[1].get_nume()=="An J")
        assert(repoTest.get_all()[1].get_CNP()==3123)
        repoTest.elimina(client.get_id())
        assert(repoTest.size() == 0)
    
    def test_modifica(self):
        repoTest = Repo()
        assert(repoTest.size()==0)
        client = Client(1,"An J",3123)
        repoTest.adauga(client)
        assert(repoTest.size()==1)
        assert(repoTest.get_all()[1].get_id()==1)
        assert(repoTest.get_all()[1].get_nume()=="An J")
        client2 = Client(1,"Io D",31221)
        repoTest.modifica(client2)
        assert(repoTest.get_all()[1].get_id() == 1)
        assert(repoTest.get_all()[1].get_nume() == "Io D")
        assert(repoTest.get_all()[1].get_CNP() == 31221)
        
   
            
        
    def test_adauga_carte(self):
        repoTest = Repo()
        #validTest = 
        #carte = Client(1,"An J",3123)
        
        
    def test_shake_sort(self):
        a = [5, 1, 4, 2, 8, 0, 2] 
        shake_sort.shake_sort(a, cmp = lambda x,y: x<=y)
        b = [0, 1, 2, 2, 4, 5, 8] 
        assert(a==b)
        
    def run_all_tests(self):
        self.test_adauga()
        self.test_get_all()
        self.test_modifica()
        self.test_size()
        self.test_sterge()
        self.test_shake_sort()
