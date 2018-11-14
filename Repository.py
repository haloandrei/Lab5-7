'''
Created on Nov 6, 2018

@author: haloandrei
'''
from haloandrei.Movie import *
from haloandrei.Client import *
from copy import deepcopy

class Repository():
    MovieList = []
    ClientList = []
    RentalList = []
    
    @staticmethod
    def addMovie(movie):
        Repository.MovieList.append(movie)
    
    @staticmethod
    def addClient(client):
        Repository.ClientList.append(client)
        
    @staticmethod
    def addRental(rented):
        Repository.RentalList.append(rented)   
    
    @staticmethod
    def getMovieList():
        return deepcopy(Repository.MovieList[:])
    
    @staticmethod
    def getClientList():
        return deepcopy(Repository.ClientList[:])
    
    @staticmethod
    def getRentalList():
        return deepcopy(Repository.RentalList[:])
    
    @staticmethod
    def RemoveClient(id):
        indexInList = Repository.searchForId(id, Repository.ClientList)
        if indexInList != -1 :
            del Repository.ClientList[indexInList]

    @staticmethod
    def RemoveMovie(id):
        indexInList = Repository.searchForId(id, Repository.MovieList)
        if indexInList != -1 :
            del Repository.MovieList[indexInList]
    
    @staticmethod
    def searchForId(IdSearched, objectList):
        for objectFromList in objectList :
            if objectFromList.getId() == int(IdSearched) :
                return objectList.index(objectFromList)
        return -1

    @staticmethod
    def UpdateMovie(index, movie):
        idSmen = Repository.MovieList[index].getId()
        Repository.MovieList[index] = movie
        Repository.MovieList[index].setId(idSmen)
    
    @staticmethod
    def UpdateClient(index, client):
        idSmen = Repository.ClientList[index].getId()
        Repository.ClientList[index] = client
        Repository.ClientList[index].setClientId(idSmen)

    @staticmethod
    def searchInMoviesForId(id):
        return Repository.searchForId(id,Repository.MovieList)

    @staticmethod
    def searchInClientsForId(id):
        return Repository.searchForId(id,Repository.ClientList)
    
    @staticmethod
    def searchInRentalForClientId(IdSearched,objectList):
        for objectFromList in objectList :
            if objectFromList.getClientId() == int(IdSearched) :
                return objectList.index(objectFromList)
        return -1
    
    @staticmethod
    def searchInRentalForMovieId(IdSearched,objectList):
        for objectFromList in objectList :
            if objectFromList.getMovieId() == int(IdSearched) :
                return objectList.index(objectFromList)
        return -1
    
    @staticmethod
    def CheckIfMovieAvailable(id):
        if( Repository.searchInRentalForMovieId(id,Repository.RentalList)  == -1) : return True
        else : return False
    @staticmethod
    def CheckIfClientAvailable(id):
        
        if Repository.searchInRentalForClientId(id,Repository.RentalList) == -1 : return True
        
        else : return False

    @staticmethod
    def removeRental( DesiredMovieId):
        del Repository.RentalList[Repository.searchInRentalForMovieId(DesiredMovieId, Repository.RentalList)]
    
    
    
    
        
    
