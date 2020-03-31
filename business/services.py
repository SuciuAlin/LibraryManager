from domeniu.enititati import *
from infrastructura.repos import Repo
from validare.validatoare import ValidatorClient
import random
from sorts.shake_sort import shake_sort

class ServiceCarti:
    
    def __init__(self,repoCarti,validCarte):
        self.__repoCarti = repoCarti
        self.__validCarte = validCarte
    
    
    def adauga_carte(self,id_carte,titlu,descriere,autor):
        carte = Carte(id_carte,titlu,descriere,autor)
        self.__validCarte.valideaza_carte(carte)
        self.__repoCarti.adauga(carte)
    
    
    def cauta_carte_dupa_id(self,id_carte):
        return self.__repoCarti.cauta(Carte(id_carte,None,None,None))
    
    
    def modifica_carte(self,id_carte,titlu_nou,descriere_noua,autor_nou):
        carte_noua = Carte(id_carte,titlu_nou,descriere_noua,autor_nou)
        self.__validCarte.valideaza_carte(carte_noua)
        self.__repoCarti.modifica(carte_noua)
    
    
    def sterge_carte(self,id_carte):
        self.__repoCarti.elimina(id_carte)
    
    def get_carti(self):
        return self.__repoCarti.get_all()
    
    
    def __generare_id(self):
        id_maxim = 0
        repoCarti = self.__repoCarti.get_all()
        for carte in repoCarti:
            if carte > id_maxim:
                id_maxim = carte
        return id_maxim + 1
    
    def __generare_titlu_descriere_autor(self):
        titlu = ["Ananas","Reptilian","Sub mare","La plaja"]
        descriere = ["Minunat","Incredibil","Nemaipomenit"]
        autor = ["Vasile Voiculescu","Ioan Graaur","Eratostene"]
        rand_titlu = random.randrange(0,3)
        rand_desc = random.randrange(0,2)
        rand_autor = random.randrange(0,2)
        return (titlu[rand_titlu],descriere[rand_desc],autor[rand_autor])
        
    def __generare_carte(self):
        id = self.__generare_id()
        tuplu = self.__generare_titlu_descriere_autor()
        titlu = tuplu[0]
        autor = tuplu[2]
        descriere = tuplu[1]
        return Carte(id,titlu,descriere,autor)
        
    def generare_n_carti(self,n):
        for i in range(0,int(n)):
            self.__repoCarti.adauga(self.__generare_carte())
            
            
            
        
class ServiceClienti:
    def __init__(self,repoClienti,validClient):
        self.__repoClienti = repoClienti
        self.__validClient = validClient
        
        
    def adauga_client(self,id_client,nume,CNP):
        client = Client(id_client,nume,CNP)
        self.__validClient.valideaza_client(client)
        self.__repoClienti.adauga(client)
    
    
    def adauga_client2(self,id_client,nume,CNP):
        client = Client(id_client,nume,CNP)
        self.__validClient.valideaza_client(client)
        self.__repoClienti.adauga2(client, )
        
      
    def cauta_client_dupa_id(self,id_client):
        return self.__repoClienti.cauta(Client(id_client,None,None))
    
    
    def modifica_client(self,id_client,nume_nou,CNP_nou):
        client_nou = Client(id_client,nume_nou,CNP_nou)
        self.__validClient.valideaza_client(client_nou)
        self.__repoClienti.modifica(client_nou)
        
        
    def get_clienti(self):
        return self.__repoClienti.get_all()
    
    
    def __generare_id_unic(self):
        ok = True
        id = random.randrange(1,200)
        while ok:
            
            try:
                self.__repoClienti.cauta(Client(id,None,None))
                id = random.randrange(1,200)
            except:
                ok = False
        return id
    
    
    def __generare_id_unic_rec(self):
        id = random.randrange(1,200)
        try:
            self.__repoClienti.cauta(Client(id,None,None))
            self.__generare_id_unic_rec()
        except:
            return id
    
    def __generare_CNP(self):
        #prima cifra 1 2 5 sau 6
        c1 = 2
        c2_c3 = random.randrange(30,99)
        c4 = 0
        c5 = random.randrange(1,9)
        c6_c7 = random.randrange(10,28)
        c8_c9_c10_c11_c12_c13 = random.randrange(0,999999)
        return c8_c9_c10_c11_c12_c13 + c6_c7*1000000 + c5*100000000 + c2_c3*10000000000 + c1 *1000000000000

    def __generare_client(self):
        lista_prenume =["Aaliyah","Abbey","Abby","Abigail","Abrienda","Acacia","Ada","Addie","Adela","Adelie","Adelina","Adelyn","Adina","Adonia","Adria","Adriana","Adrianne","Afrodita","Agapia","Agata","Amara","Amaryllis","Amaya","Amber","Amena","Ami","Amira","Amora","Amy","Ana","Anabela","Anabella","Ananda","Anastacia","Anastasia","Anaya","Anca","Anda","Andreea"]
        lista_nume = ["Armășescu","Arnăuțoiu","Arnautu","Arnăutu","Asachi","Athanasiu","Averescu","Avramescu","Bacalbașa","Baciu","Baconschi","Baconski","Baconsky","Bădărău","Badea","Bădescu","Bădulescu","Baghiu","Baicu","Bălăceanu","Bălan","Balanici","Balauru","Băloșescu","Bălțat","Bănățeanu","Bănică","Bănică",",Bănulescu","Baracci","Bărboianu","Barbu","Bărbuceanu","Bărbulescu","Bârcă","Barcianu","Bârlea","Bârloiu","Barna","Bârsănescu","Barzin"]
        nr_prenume = random.randrange(0,34)
        nr_nume = random.randrange(0,40)
        id = self.__generare_id_unic()
        cnp = self.__generare_CNP()
        return Client(id,lista_nume[nr_nume] + " " + lista_prenume[nr_prenume], cnp)

    def generare_n_clienti(self,n):
        for i in range(0,int(n)):
            self.__repoClienti.adauga(self.__generare_client())

    def generare_n_clienti_rec(self,n):
        if n > 0 :
            self.__repoClienti.adauga(self.__generare_client())
            self.generare_n_clienti_rec(n-1)
    
    def selection_sort(self,*,key = lambda x:x.get_val()):
        #ia minimul intotdeauana si il pozitioneaza la locul lui
        lista_clienti = self.__repoClienti.get_all()
        for i in range(0,len(lista_clienti)-1):
            mi = i
            for j in range(i+1,len(lista_clienti)):
                if key(lista_clienti[j])< key(lista_clienti[mi]):
                    mi = j
            
            lista_clienti[i],lista_clienti[j] = lista_clienti[j],lista_clienti[i]
            
        return lista_clienti




class ServiceInchirieri:
    
    def __init__(self,repoClienti,repoCarti,repoInchirieri,validInchiriere):
        self.__repoClienti = repoClienti
        self.__repoCarti = repoCarti
        self.__repoInchirieri = repoInchirieri
        self.__validInchiriere = validInchiriere
        
    
    def adauga_inchiriere(self,cl_id,ca_id):
        inchiriere = Inchiriere(Client(cl_id,"",""),Carte(ca_id,"","",""),1)
        self.__validInchiriere.valideaza_inchiriere(inchiriere)
        self.__repoClienti.cauta(Client(cl_id,None,None))
        self.__repoCarti.cauta(Carte(ca_id,None,None,None))
        self.__repoInchirieri.adauga(inchiriere)
     
    def cauta_client_dupa_id(self,id_client):
        return self.__repoClienti.cauta(Client(id_client,None,None))
       
        
    
    def returnare_inchiriere(self,cl_id,ca_id):
        inchiriere_noua = Inchiriere(cl_id,ca_id,0)
        self.__validInchiriere.valideaza_inchiriere(inchiriere_noua)
        self.__repoInchirieri.modifica(inchiriere_noua)
    
    
    def __raport_cele_mai_inchiriate_carti_iduri(self):
        #revazut verificat
        #cheia e id_ca, value e nr aparatii in inchirieri
        dictionar_carti = {}
        #cheie din inchiriere e sub forma idClient_idCarte 
        #e necesar pt carti int(cheie[2])
        for cheieL in self.__repoInchirieri.get_all():
            cheie = cheieL.split("_")
            if int(cheie[1]) in dictionar_carti:
                dictionar_carti[int(cheie[1])] += 1
            else:
                dictionar_carti[int(cheie[1])] = 1
    
        #plec de la maxim
        maxim = 0
        for cheie in dictionar_carti:
            if dictionar_carti[cheie] > maxim:
                maxim = dictionar_carti[cheie]
        
        sir_maxime =[]
        #cat timp maxim>0
        maxim2 = 1
        while maxim2!=0:
            maxim2 = 0
            for cheie in dictionar_carti:
                if dictionar_carti[cheie] == maxim:
                    sir_maxime.append(cheie)
                elif dictionar_carti[cheie] < maxim and dictionar_carti[cheie] > maxim2:
                    maxim2 = dictionar_carti[cheie]
            maxim = maxim2
            
        return sir_maxime
    
    
    
    def raport_cele_mai_inchiriate_carti(self):
        sir_id = self.__raport_cele_mai_inchiriate_carti_iduri()
        sir_carti = []
        for ca_id in sir_id:
            sir_carti.append(self.__repoCarti.cauta(Carte(ca_id,None,None,None)))
        return sir_carti
    
    
    def get_inchirieri_ids(self):
        #din repo le iau doar pe cele care nu au al treilea atribut 0
        #le pun in alt dictionar
        entitati = self.__repoInchirieri.get_all()
               
        inchiriate = {}
        for cheie in entitati:
            if int(entitati[cheie].get_e_inchiriat()) == 1:
                inchiriate[cheie] = entitati[cheie]
        return inchiriate
    
    
    def get_inchirieri(self):
        inchiriate = self.get_inchirieri_ids()
        inchirieri = {}
        for cheie in inchiriate:
            parts = str(inchiriate[cheie]).split('_')
            cl_id = parts[0]
            ca_id = parts[1]
            #fiecare valoare din dictionar contine un obiect inchiriere ce contine un client si o carte
            inchirieri[cl_id+'_'+ca_id] = Inchiriere(self.cauta_client_dupa_id(cl_id),self.cauta_carte_dupa_id(ca_id))
        for cheie in inchirieri:    
            print(inchirieri[cheie])
        return inchirieri    
    
    
    def cauta_carte_dupa_id(self,id_carte):
        return self.__repoCarti.cauta(Carte(id_carte,None,None,None))
       
    
    def sterge_client(self,cl_id):
        self.__repoClienti.cauta(Client(cl_id,None,None))
        self.__repoClienti.elimina(cl_id)
        #sterge_toate inchirierile ce au id ul cl_id pt client
        inchirieri = self.__repoInchirieri.get_all()
        
        
        id_inchirieri_de_sters = []
        for cheie in inchirieri:
            inchirieri_cl_id = int(cheie.split("_")[0])
            if inchirieri_cl_id == cl_id:
                id_inchirieri_de_sters.append(cheie)
        
        for cheie in id_inchirieri_de_sters:
            self.__repoInchirieri.elimina(cheie)
            
    def sterge_carte(self,ca_id):
        self.__repoCarti.cauta(Carte(ca_id,None,None,None))
        self.__repoCarti.elimina(ca_id)
        #sterge_toate inchirierile ce au id ul cl_id pt client
        inchirieri = self.__repoInchirieri.get_all()
        
        
        id_inchirieri_de_sters = []
        for cheie in inchirieri:
            inchirieri_ca_id = int(cheie.split("_")[1])
            if inchirieri_ca_id == ca_id:
                id_inchirieri_de_sters.append(cheie)
        
        for cheie in id_inchirieri_de_sters:
            self.__repoInchirieri.elimina(cheie)
       
            
    def __id_clienti_cu_carti_inchiriate(self):
        clienti_id = {}
        repoInchirieriDictionar = self.__repoInchirieri.get_all()
        for cheie in repoInchirieriDictionar:
            #din cheie primu char
            id_client = int(str(repoInchirieriDictionar[cheie]).split('_')[0])
            clienti_id[id_client] = ""
        
        return clienti_id

    def __clienti_cu_carti_inchiriate(self):
        id_clienti = self.__id_clienti_cu_carti_inchiriate()
        dictionar_clienti = self.__repoClienti.get_all()
        clienti = {}
        for cheie in id_clienti:
            clienti[cheie] = dictionar_clienti[cheie]
        return clienti
    
    
    def __mutare_clienti_din_dictionar_in_lista(self):
        lista_clienti = []
        clienti_cu_carti_inchiriate = self.__clienti_cu_carti_inchiriate()
            
        for cheie in clienti_cu_carti_inchiriate:
            lista_clienti.append(clienti_cu_carti_inchiriate[cheie])
        
        return lista_clienti
        
    def selection_sort(self,*,key = lambda x:x.get_val()):
        #ia minimul intotdeauana si il pozitioneaza la locul lui
        lista_clienti = self.__repoClienti.get_all()
        for i in range(0,len(lista_clienti)-1):
            mi = i
            for j in range(i+1,len(lista_clienti)):
                if key(lista_clienti[j])< key(lista_clienti[mi]):
                    mi = j
            
            lista_clienti[i],lista_clienti[j] = lista_clienti[j],lista_clienti[i]
            
        return lista_clienti  
    
     
    def __sortare_clienti_dupa_nume(self):    
        lista_clienti = self.__mutare_clienti_din_dictionar_in_lista()
        
        '''ok = True
        while ok:
            ok = False
            for i in range(0,len(lista_clienti)-1):
                if lista_clienti[i].get_nume() > lista_clienti[i+1].get_nume():
                    aux = lista_clienti[i]
                    lista_clienti[i] = lista_clienti[i+1]
                    lista_clienti[i+1] = aux
                    ok = True
        '''
        self.selection_sort(self,key = lambda x:x.get_nume())
        return lista_clienti
    
    def __numarare_carti_pentru_id_client(self,cl_id):
        numar_inchirieri = 0
        dictionar_repo_inchirieri = self.__repoInchirieri.get_all()
        for cheie in dictionar_repo_inchirieri:
            cl_id_local = int(str(dictionar_repo_inchirieri[cheie]).split('_')[0])
            if cl_id == cl_id_local:
                numar_inchirieri += 1
        return numar_inchirieri
        
        
    def sortare_clienti_dupa_nume_apoi_carti(self):
        ok = True
        lista_clienti_sortat_nume = self.__sortare_clienti_dupa_nume()
        while ok:
            ok = False
            for i in range(0,len(lista_clienti_sortat_nume)-1):
                if lista_clienti_sortat_nume[i].get_nume() == lista_clienti_sortat_nume[i+1].get_nume():
                    nr_carti_i = self.__numarare_carti_pentru_id_client(lista_clienti_sortat_nume[i].get_id())
                    nr_carti_i_1 = self.__numarare_carti_pentru_id_client(lista_clienti_sortat_nume[i+1].get_id())
                    if nr_carti_i > nr_carti_i_1:
                        aux = lista_clienti_sortat_nume[i]
                        lista_clienti_sortat_nume[i] = lista_clienti_sortat_nume[i+1]
                        lista_clienti_sortat_nume[i+1] = aux
                        ok = True
        return lista_clienti_sortat_nume
    
    
    def __sortare_clienti_dupa_carti(self):
        lista_clienti = self.__mutare_clienti_din_dictionar_in_lista()
        ok =True
        while ok:
            ok = False
            for i in range(0,len(lista_clienti)-1):
                if self.__numarare_carti_pentru_id_client(lista_clienti[i].get_id()) < self.__numarare_carti_pentru_id_client(lista_clienti[i+1].get_id()):
                    ok = True
                    aux = lista_clienti[i]
                    lista_clienti[i] = lista_clienti[i+1]
                    lista_clienti[i+1] = aux
       
            
        return lista_clienti
    
    def raport_cei_mai_20(self):
        numar_clienti = int(len(self.__repoClienti.get_all())/5)#scos /5 pt sortare la tema
        lista_clienti = self.__sortare_clienti_dupa_carti()
        lista_nr_carti = []
        
        
            
        for i in range(0,len(lista_clienti)):
            lista_nr_carti.append(self.__numarare_carti_pentru_id_client(lista_clienti[i].get_id()))
            
        for i in range(0,len(lista_clienti)):
            lista_clienti[i] = lista_clienti[i].get_nume()
            
        return (lista_clienti[:numar_clienti],lista_nr_carti[:numar_clienti])
    
    #lista autorilor ordonata crescator dupa nr de Inchirieri
    def __autori_cu_nr_carti_inchiriate(self):
        dictionar_autor_nr_carti = {}
        repoInchirieri = self.__repoInchirieri.get_all()
        for cheie in repoInchirieri:
            inchiriere = repoInchirieri[cheie]
            carte = self.__repoCarti.cauta(Carte(int(str(inchiriere).split('_')[1]),None,None,None))
            autor = carte.get_autor()
                
            if autor in dictionar_autor_nr_carti:
                dictionar_autor_nr_carti[autor] += 1
            else:
                dictionar_autor_nr_carti[autor] = 1
        
        return dictionar_autor_nr_carti
    
           
    def __mutare_autori_din_dictionar_in_lista(self):
        dictionar_autor_nr_carti = self.__autori_cu_nr_carti_inchiriate()
        lista_autori_nr = []
        for cheie in dictionar_autor_nr_carti:
            lista_autori_nr.append([cheie,dictionar_autor_nr_carti[cheie]])
            
        
        return lista_autori_nr
     
            
    def __sortare_autori_cu_nr_carti(self):
        dictionar_autor_nr_carti = self.__mutare_autori_din_dictionar_in_lista()
        
        '''
        ok = True
        while ok:
            ok = False
            for i in range(0,len(dictionar_autor_nr_carti)-1):
                
                if dictionar_autor_nr_carti[i][1] > dictionar_autor_nr_carti[i+1][1]:
                    ok = True
                    aux = dictionar_autor_nr_carti[i]
                    dictionar_autor_nr_carti[i] = dictionar_autor_nr_carti[i+1]
                    dictionar_autor_nr_carti[i+1] = aux
        
        #self.selection_sort(dictionar_autor_nr_carti,key=lambda x:x[1])
        '''
        shake_sort(dictionar_autor_nr_carti, cmp = lambda x,y: x[1]<=y[1])
        
        
        return dictionar_autor_nr_carti
    
    def raport_autori(self):
        
        return self.__sortare_autori_cu_nr_carti()
                        
                            

        
        
                   