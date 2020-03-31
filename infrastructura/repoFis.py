from infrastructura.repos import Repo
import os
f = open("stocare.txt","r")
class RepoFisier(Repo):
    def __init__(self,val,path):
        Repo.__init__(self,val)
        self.__path = path
        self.__entitati = f.read()
        #self.__
        #idrpath = os.getcwd()
        
    def adauga(self,s):
        Repo.adauga(self,s)
#        self.__scrie_in_fisier
        
        