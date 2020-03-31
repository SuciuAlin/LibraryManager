from teste.teste import Teste
from validare.validatoare import ValidatorCarte, ValidatorClient,\
    ValidatorInchiriere
from infrastructura.repos import Repo, FileRepo, RepoFileCl
from domeniu.enititati import Carte, Client, Inchiriere
from business.services import ServiceCarti, ServiceClienti, ServiceInchirieri
from prezentare.ui import Consola



teste = Teste()
teste.run_all_tests()

validCarte = ValidatorCarte()
validClient = ValidatorClient()
validInchiriere = ValidatorInchiriere()


repoCarti = FileRepo("carti.txt",Carte.read_carte,Carte.write_carte)
'''
repoCarti.adauga(Carte(1,"Luceafarul","O poezie lunga","Mihai Eminescu"))
repoCarti.adauga(Carte(2,"Plumb","O poezie trista","George Bacovia"))
repoCarti.adauga(Carte(3,"Testament","O poezie de viata","Tudor Arghezi"))
repoCarti.adauga(Carte(4,"Moara cu noroc","Nuvela politista","Ioan Slavici"))
repoCarti.adauga(Carte(5,"Ultima noapte de dragoste, întâia noapte de război","Interzis cardiacilor","Camil Petrescu"))
repoCarti.adauga(Carte(6,"Ion","Un roman al romanului","Liviu Rebreanu"))
repoCarti.adauga(Carte(7,"Iona","Balena","Mihai Eminescu"))
'''
#repoClienti = FileRepo("clienti.txt",Client.read_client,Client.write_client)

repoClienti = FileRepo("clienti.txt",Client.read_client,Client.write_client)

#format cnp: tip_an_an_luna_luna_ziua_ziua_6cifre random
'''repoClienti.adauga(Client(1,"Neculai Voiculet",1991206000001))
repoClienti.adauga(Client(2,"Traian Lupescu",1961206000003))
repoClienti.adauga(Client(3,"Remus Leonte",1951106000006))
repoClienti.adauga(Client(4,"Robert Ene",1931206000009))
repoClienti.adauga(Client(5,"Robert",9))
'''
repoInchirieri = FileRepo("inchirieri.txt",Inchiriere.read_inchiriere,Inchiriere.write_inchiriere)
#repoInchirieri.adauga(Inchiriere(Client(1,nume,CNP),Carte(1,titlu,descriere,autor)))
'''
repoInchirieri.adauga(Inchiriere(Client(1,None,None),Carte(1,None,None,None)))
repoInchirieri.adauga(Inchiriere(Client(1,None,None),Carte(2,None,None,None)))
repoInchirieri.adauga(Inchiriere(Client(1,None,None),Carte(4,None,None,None)))
repoInchirieri.adauga(Inchiriere(Client(1,None,None),Carte(6,None,None,None)))
repoInchirieri.adauga(Inchiriere(Client(2,None,None),Carte(1,None,None,None)))
repoInchirieri.adauga(Inchiriere(Client(2,None,None),Carte(3,None,None,None)))
repoInchirieri.adauga(Inchiriere(Client(3,None,None),Carte(4,None,None,None)))
repoInchirieri.adauga(Inchiriere(Client(3,None,None),Carte(5,None,None,None)))
repoInchirieri.adauga(Inchiriere(Client(3,None,None),Carte(6,None,None,None)))
repoInchirieri.adauga(Inchiriere(Client(4,None,None),Carte(1,None,None,None)))
repoInchirieri.adauga(Inchiriere(Client(4,None,None),Carte(2,None,None,None)))
repoInchirieri.adauga(Inchiriere(Client(4,None,None),Carte(3,None,None,None)))
repoInchirieri.adauga(Inchiriere(Client(4,None,None),Carte(4,None,None,None)))
repoInchirieri.adauga(Inchiriere(Client(4,None,None),Carte(5,None,None,None)))
repoInchirieri.adauga(Inchiriere(Client(4,None,None),Carte(6,None,None,None)))
'''
serviceCarti = ServiceCarti(repoCarti,validCarte)
serviceClienti = ServiceClienti(repoClienti,validClient)
serviceInchirieri = ServiceInchirieri(repoClienti,repoCarti,repoInchirieri,validInchiriere)



ui = Consola(serviceCarti,serviceClienti,serviceInchirieri)
ui.run()
