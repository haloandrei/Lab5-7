'''
Created on Nov 7, 2018

@author: haloandrei
'''
from haloandrei.Repository import *
from haloandrei.Movie import *
from haloandrei.Client import *
from haloandrei.Rental import *

def addMovie(movie):
    Repository.addMovie(movie)
    
def addClient(client):
    Repository.addClient(client)
    
def getMovieList():
    return Repository.getMovieList()
def getClientList():
    return Repository.getClientList()

def removeMovie(id):
    Repository.RemoveMovie(id)

def removeClient(id):
    Repository.RemoveClient(id)

def updateMovie(id,movie):
    index = Repository.searchInMoviesForId(id)
    #needs index validation
    Repository.UpdateMovie(index, movie)

def updateClient(id,client):
    index = Repository.searchInClientsForId(id)
    #needs index validation
    Repository.UpdateClient(index, client)
    

def addRental(rented):
    Repository.addRental(rented)

def getRental():
    return Repository.getRentalList()

def RentMovie(DesiredMovieId, ClientId, RentDate, DueDate):
    if Repository.CheckIfMovieAvailable(DesiredMovieId) == True :
        rented = Rental(DesiredMovieId, ClientId, RentDate, DueDate, -1) 
        addRental(rented)
    else : print('movie taken!!!')

def ReturnMovie(ClientId,DesiredMovieId,ReturnDate):
    if Repository.CheckIfClientAvailable(ClientId) == True :
        Repository.removeRental(DesiredMovieId)
    