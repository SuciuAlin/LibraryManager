from erori.exceptii import RepoError, ValidError
from domeniu.enititati import Inchiriere

class Consola:
    
   
    def __ui_adauga_client(self,params):
        if len(params)!=3:
            raise ValueError("nr params trebuie sa fie exact 3!\n")
        c_id = int(params[0])
        nume = params[1]
        CNP = params[2]
        self.__serviceClienti.adauga_client(c_id,nume,CNP)
    
    def __ui_adauga_client2(self,params):
        if len(params)!=3:
            raise ValueError("nr params trebuie sa fie exact 3!\n")
        c_id = int(params[0])
        nume = params[1]
        CNP = params[2]
        self.__serviceClienti.adauga_client2(c_id,nume,CNP)
    
    def __ui_print_clienti(self,params):
        clienti = self.__serviceClienti.get_clienti()
        for client in clienti:
            print(str(self.__serviceClienti.get_clienti()[client]))
            
    
    def __ui_adauga_carte(self,params):
        if len(params)!=4:
            raise ValueError("nr params invalid! trebuie sa fie fix 4!\n")
        ca_id = params[0]
        titlu = params[1]
        descriere = params[2]
        autor = params[3]
        self.__serviceCarti.adauga_carte(ca_id,titlu,descriere,autor)
        
    
    def __ui_print_carte(self,params):
        carti = self.__serviceCarti.get_carti()
        for carte in carti:
            print(self.__serviceCarti.get_carti()[carte]) 
    
    
    def __ui_adauga_inchiriere(self,params):
        if len(params) != 2:
            raise ValueError("nr params invalid!trebuie sa fie fix 2!\n")
        cl_id = params[0]
        ca_id = params[1]
        self.__serviceInchirieri.adauga_inchiriere(cl_id,ca_id)
    
    
    def __ui_print_inchiriere(self,params):
        inchirieri = self.__serviceInchirieri.get_inchirieri_ids()
        for inchiriere in inchirieri:
            print(inchirieri[inchiriere])
            
            
    def __ui_cauta_carte(self,params):
        if len(params) != 1:
            raise ValueError("nr params invalid!trebuie sa fie fix 1!\n")
        ca_id = params[0]
        print(self.__serviceCarti.cauta_carte_dupa_id(ca_id))
    
    
    def __ui_cauta_client(self,params):
        if len(params) != 1:
            raise ValueError("nr params invalid!trebuie sa fie fix 1!\n")
        cl_id = params[0]
        print(self.__serviceClienti.cauta_client_dupa_id(cl_id))
    
    
    def __ui_modifica_carte(self,params):
        #ia parametrii prost fiindca is mai multe cuvinte pt unul
        #revazut
        if len(params) != 4:
            raise ValueError("nr params invalid! trebuie sa fie fix 6!\n")
        id_carte = params[0]
        titlu = params[1]
        descriere = params[2]
        autor = params[3]
        self.__serviceCarti.modifica_carte(id_carte,titlu,descriere,autor)
    
    
    def __ui_modifica_client(self,params):
        if len(params) != 3:
            raise ValueError("nr params invalid! trebuie sa fie fix 3!\n")
        cl_id = params[0]
        nume = params[1]
        CNP = params[2]
        self.__serviceClienti.modifica_client(cl_id,nume,CNP)
    
    
    def __ui_retunare_carte(self,params):
        if len(params) != 2:
            raise ValueError("nr params invalid! trebuie sa fie fix 2!\n")
        cl_id = params[0]
        ca_id = params[1]
        self.__serviceInchirieri.returnare_inchiriere(cl_id,ca_id)
    
    
    def __ui_sterge_client(self,params):
        if len(params) != 1:
            raise ValueError("nr params invalid! trebuie sa fie fix 1!\n")
        cl_id = int(params[0])
        self.__serviceInchirieri.sterge_client(cl_id)
    
    def __ui_sterge_carte(self,params):
        if len(params) != 1:
            raise ValueError("nr params invalid! trebuie sa fie fix 1!\n")
        ca_id = int(params[0])
        self.__serviceInchirieri.sterge_carte(ca_id)
    
    def __ui_raport_carti(self,params):
        for carte in self.__serviceInchirieri.raport_cele_mai_inchiriate_carti():
            print(carte)
    
    
    def __ui_raport_clienti_cu_carti(self,params):
        for client in self.__serviceInchirieri.sortare_clienti_dupa_nume_apoi_carti():
            print(client)
    
    
    def __ui_raport_20(self,params):
        for client in self.__serviceInchirieri.raport_cei_mai_20():
            print(*client)
            
    def __ui_generare_n(self,params):
        if len(params)!= 1:
            raise ValueError("nr invalid de params! Trebuie sa fie exact 1!\n")
        
        self.__serviceClienti.generare_n_clienti(params[0])
        self.__serviceCarti.generare_n_carti(params[0])    
         
    
    def __ui_raport_autori(self,params):
        
        raport_autori = self.__serviceInchirieri.raport_autori()
        for cheie in raport_autori:
            print("{}".format(cheie[0]))
            print("{}".format(cheie[1]))
            
        
            
    def __init__(self, serviceCarti, serviceClienti, serviceInchirieri):
        self.__serviceCarti = serviceCarti
        self.__serviceClienti = serviceClienti
        self.__serviceInchirieri = serviceInchirieri
        self.__comenzi= {
        "add_client":self.__ui_adauga_client,
        "add_client2":self.__ui_adauga_client2,
        "print_clienti":self.__ui_print_clienti,
        "add_carte":self.__ui_adauga_carte,
        "print_carti":self.__ui_print_carte,
        "add_inchiriere":self.__ui_adauga_inchiriere,
        "print_inchirieri":self.__ui_print_inchiriere,   
        "search_client":self.__ui_cauta_client,
        "search_carte":self.__ui_cauta_carte,
        "modify_carte":self.__ui_modifica_carte,
        "modify_client":self.__ui_modifica_client,
        "return_carte":self.__ui_retunare_carte,
        "delete_client":self.__ui_sterge_client,
        "delete_carte":self.__ui_sterge_carte,
        "raport_carti":self.__ui_raport_carti,
        "raport_clienti":self.__ui_raport_clienti_cu_carti,
        "raport_20":self.__ui_raport_20,
        "raport_autori":self.__ui_raport_autori,
        "generare":self.__ui_generare_n
        
        }
        
    
    def run(self):
        while True:
            cmd = input(">>>")
            if cmd == "exit":
                return
            cmd = cmd.strip()
            parts = cmd.split(';')
            cmd_nume = parts[0]
            params = parts[1:]
            if cmd_nume in self.__comenzi:
                try:
                    self.__comenzi[cmd_nume](params)
                #except ValueError as ve:
                 #  print("UI error:\n"+str(ve))
                except ValidError as vale:
                    print("Validare error:\n"+str(vale))
                except RepoError as re:
                    print("Repo error:\n"+str(re))
            else:
                print("comanda invalida!")
            

