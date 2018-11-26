'''
Created on Nov 7, 2018

@author: haloandrei
'''
from haloandrei.Repository import *
from haloandrei.Movie import *
from haloandrei.Client import *
from haloandrei.Rental import *
from _datetime import datetime, timedelta

def addMovie(movie):
    Repository.addMovie(movie)
    
def addClient(client):
    Repository.addClient(client)
    
def getMovieList():
    return Repository.getMovieList()
def getClientList():
    return Repository.getClientList()

def removeMovie(iD):
    Repository.RemoveMovie(iD)

def removeClient(iD):
    Repository.RemoveClient(iD)

def updateMovie(iD,movie):
    index = Repository.searchInMoviesForId(iD)
    #needs index validation
    Repository.UpdateMovie(index, movie)

def updateClient(iD,client):
    index = Repository.searchInClientsForId(iD)
    #needs index validation
    Repository.UpdateClient(index, client)
    

def addRental(rented):
    Repository.addRental(rented)

def getRental():
    return Repository.getRentalList()


def getMovieById(id):
    index = Repository.searchInMoviesForId(id)
    return Repository.getMovieByIndex(index)

def getClientById(id):
    index = Repository.searchInClientsForId(id)
    return Repository.getClientByIndex(index)


def RentMovie(DesiredMovieId, ClientId, RentDate, DueDate):
    if Repository.CheckIfMovieAvailable(DesiredMovieId) == True :
        if isClientLate(ClientId) == 0:
            movie = getMovieById(DesiredMovieId)
            movie.incTimesRented()
            rented = Rental(DesiredMovieId, ClientId, RentDate, DueDate, -1) 
            addRental(rented)
        else : print('Client overDue')
    else : print('Movie taken')
    
def getMostActiveClient():
    clientList = getClientList()
    clientList = sortDecreasingClients(clientList)
    return clientList

def getMostRentedMovie():
    movieList = getMovieList()
    movieList = sortDecreasingMovies(movieList)
    return movieList

def getLateRentals():
    RentalList = getRental()
    LateRentalList = []
    for rental in RentalList:
        if datetime.now().date() - rental.getDueDate() > timedelta(days = 0):
            LateRentalList.append(rental)
    return LateRentalList

def isMovieRented(DesiredMovieId):
    Rentals = getRental()
    for rental in Rentals:
        if rental.getMovieId() == DesiredMovieId : return 1
    return 0

def isClientLate(ClientId):
    RentalList = getRental()
    
    for rental in RentalList:
        if str(rental.getClientId()) == str(ClientId):
            if datetime.now().date() - rental.getDueDate() > timedelta(days = 0):
                return 1
    return 0

def sortDecreasingRentals(List):
    if List != None:
        for index1 in range(0 ,len(List) - 1 ):
            for index2 in range(index1+1,len(List) ):
                if List[index1].getDueDate() > List[index2].getDueDate():
                    List[index1],List[index2] = List[index2],List[index1]   
    return List

def sortDecreasingMovies(List):
    if List != None:
        for index1 in range(0 ,len(List) - 1 ):
            for index2 in range(index1+1,len(List) ):
                if List[index1].getTimesRented() < List[index2].getTimesRented():
                    List[index1],List[index2] = List[index2],List[index1]   
    return List

def sortDecreasingClients(List):
    if List != None:
        for index1 in range(0 ,len(List) - 1 ):
            for index2 in range(index1+1,len(List) ):
                if List[index1].getActivity() < List[index2].getActivity():
                    List[index1],List[index2] = List[index2],List[index1]   
    return List

def ReturnMovie(ClientId,DesiredMovieId,ReturnDate):
    #if Repository.CheckIfClientAvailable(ClientId) == True :
    client = getClientById(ClientId)
    rental = Repository.getRentalByMovieId(DesiredMovieId)
    date = ReturnDate - rental.getRentedDate() 
    date = date.days + 1
    client.incActivity(date)
    Repository.returnRental(DesiredMovieId,ReturnDate)

def SearchFieldMovie(field,searched):
    FieldList = {'1':'id','2':'title', '3': 'description', '4':'genere'}
    foundList = []
    for movie in getMovieList():
        if str(movie.getAmbiguous(FieldList[field])).lower().find(searched.lower()) != -1 :
            foundList.append(movie)
    return foundList
 

def SearchFieldClient(field,searched):
    FieldList = {'1':'id','2':'name'}
    foundList = []
    for client in getClientList():
        if str(client.getAmbiguous(FieldList[field])).lower().find(searched.lower()) != -1 :
            foundList.append(client)
    return foundList
            