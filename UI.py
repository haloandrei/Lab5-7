'''
Created on Nov 6, 2018

@author: haloandrei
'''
from haloandrei.Business import *
from haloandrei.Movie import *
from haloandrei.Client import *
from datetime import datetime
import datetime
from _ctypes_test import func

def PrintMenu():
    print('~~~~~~~~~~~~[Movie Rental]~~~~~~~~~~~~~~ \n 1.add \n 2.remove \n 3.update \n 4.list \n 5.rent \n 6.return \n 7.search \n 8.statistics')
    
def ConsoleEngine():
    while True:
        try:
            PrintMenu()
            command = input('\n>')
            if (command == 'x') : return
            if ValidateCommand(command,9) == True :
                CallFunctions(command)
            else :
                print('wrong input')
        except:
            pass
def PrintChoiceBetweenMovieAndClient():
    print(' 1. for movie \n 2. for client \n')
    
def ReadClientUI():
    print('Inset Client name\n')
    name = input('\n>')
    client = Client(name)
    return client

def addClientUI():
    
    client = ReadClientUI()
    addClient(client)

def ReadMovieUI():
    print('Inset Title\n')
    title = input('\n>')
    print('Insert Description\n')
    description = input('\n>')
    print('Insert Genere')
    genere = input('\n>')
    movie = Movie(title,description,genere)
    return movie

def addMovieUI():
   
    movie = ReadMovieUI()
    addMovie(movie)

def addUI():
    PrintChoiceBetweenMovieAndClient()
    Functions = {'1':addMovieUI, '2':addClientUI}
    command = input('\n>')
    if ValidateCommand(command, 2) == True :

        Functions[command]()
    else : print('invalid input')


def listUI():
    PrintChoiceBetweenMovieAndClient()
    command = input('\n>')
    if(command == '1') :
        MovieList = getMovieList()
        for movie in MovieList :
            print(movie.ToString())
    elif (command == '2') :
        ClientList = getClientList()
        for Client in ClientList :
            print(Client.ToString())

def removeUI():
    PrintChoiceBetweenMovieAndClient()
    command = input('\n>')
    if(command == '1') :
        idOfRemoved = input('\nDelete movie with Id:\n>')
        removeMovie(idOfRemoved)
    elif(command == '2') :
        idOfRemoved = input('\nDelete client with Id:\n>')
        removeClient(idOfRemoved)
        
def updateUI():
    PrintChoiceBetweenMovieAndClient()
    command = input('\n>')
    if(command == '1') :
        idOfUpdate = input('\nUpdate movie with Id:\n>')
        movie = ReadMovieUI()
        updateMovie(idOfUpdate,movie)
    elif(command == '2') :
        idOfUpdate = input('\nUpdate client with Id:\n>')
        client = ReadClientUI()
        updateClient(idOfUpdate,client)


def DisplayRentalsUI():
    RentalList = getRental()
    for Rental in RentalList :
            print(Rental.ToString())


def SearchFieldMovieUI():
    print('[Select Field]\n1. id\n2. title\n3. description\n4. genere')
    return input('>')


def SearchFieldClientUI():
    print('[Select Field]\n1. id\n2. name')
    return input('>')



def SearchUI():
    PrintChoiceBetweenMovieAndClient()
    command = input('\n>')
    if(command == '1') :
        field = SearchFieldMovieUI()
        searched = input('search for:\n>')
        Result = SearchFieldMovie(field,searched)
        for movie in Result :
            print(movie.ToString())  
    elif(command == '2'):
        field = SearchFieldClientUI()
        searched = input('search for:\n>')
        Result = SearchFieldClient(field,searched)
        for client in Result :
            print(client.ToString())  


def LateRentalsUI():
    LateRentalList = sortDecreasingRentals(getLateRentals())
    if (LateRentalList != None) :
        for rental in LateRentalList:
            print (rental.ToString())

def MostActiveClientUI():
    clientList = getMostActiveClient()
    for client in clientList:
        print(client.ToString())

def MostRentedMovieUI():
    movieList = getMostRentedMovie()
    for movie in movieList:
        print(movie.ToString())


def GenerateStatisticsUI():
    print('1. Most rented movie\n2. Most active client\n3. All rentals\n4.Late rentals')
    functionList = {'1':MostRentedMovieUI, '2':MostActiveClientUI, '3':DisplayRentalsUI, '4':LateRentalsUI}
    statistic = input('choose a statistic: \n>')
    if statistic in functionList :
        functionList[statistic]()
    
    

def CallFunctions(command):
    Functions = {'1':addUI, '2':removeUI, '3':updateUI, '4':listUI, '5':RentMovieUI, '6':ReturnMovieUI, '7':SearchUI, '8':GenerateStatisticsUI}
    if command in Functions :
        Functions[command]()
    
def ValidateCommand(command,NumberOfCommands):
    if (int(command) > 0) and (int(command) <= NumberOfCommands):
        return True
    else : return False
    

def RentMovieUI():
    ClientId = input('Insert Client Id \n>')
    DesiredMovieId = input('Insert Movie Id \n')
    RentDate = datetime.datetime.now()
    RentDate = RentDate.date()
    DueDate = RentDate + datetime.timedelta(days = 3)
    #rent = Rental(DesiredMovieId, ClientId, RentDate, DueDate, -1)

    RentMovie(DesiredMovieId, ClientId, RentDate, DueDate)

def ReturnMovieUI():
    ClientId = input('Insert Client Id \n>')
    DesiredMovieId = input('Insert Movie Id \n')
    ReturnDate = datetime.datetime.now()
    ReturnDate = ReturnDate.date()
    ReturnMovie(ClientId,DesiredMovieId,ReturnDate)
    
def initialiseValues():
    NameList = ['Another','Bothersome','Counter','Awesome', 'Ultimate','Final','Fantastic','The']
    SecondNameList = ['Party','Father','Test','Chicks','Alien Invasion', 'Anihiliation','Blow']
    DescriptionList = ['The best movie of the month','Must watch','Full of suspense','You won t regret this','Time well spent!']
    GenereList = ['action','comedy','drama','thriller','documentary','romance','adventure']
    movie = Movie('moby','a whale','action')
    addMovie(movie)
    movie = Movie('moby','a whale','action')
    addMovie(movie)
    movie = Movie('Bohemian Rapsody','Queen`s story','documentary')
    addMovie(movie)
    movie = Movie('Die','meh','horror')
    addMovie(movie)
    movie = Movie('Creed','pew pew','action')
    addMovie(movie)
    movie = Movie('Fast and Furious','car pew pew','action')
    addMovie(movie)
    movie = Movie('I am Legend','Will Smith movie','action')
    addMovie(movie)
    movie = Movie('MIB','Will','action')
    addMovie(movie)
    movie = Movie('Green Mile','Tom hanks and the Big Black guy','drama')
    addMovie(movie)
    movie = Movie('World`s end','British comedy, dry, as i like my women','comedy')
    addMovie(movie)
    movie = Movie('Jump Street 21','cops in uni','action')
    addMovie(movie)
    movie = Movie('Jump Street 22','cops in high','action')
    addMovie(movie)
    client = Client('Nicu')
    addClient(client)
    client = Client('Baton')
    addClient(client)
    client = Client('Mikey')
    addClient(client)
    client = Client('Dascalu')
    addClient(client)
    client = Client('Ciprian Porumbescu')
    addClient(client)
    client = Client('Nicu Alifantis')
    addClient(client)
    client = Client('Antrenament Botez Simulator')
    addClient(client)
    client = Client('Emeric')
    addClient(client)
    client = Client('Alternosfera')
    addClient(client)
    client = Client('Dora')
    addClient(client)
    client = Client('Tequila')
    addClient(client)
    client = Client('Vihart')
    addClient(client)
    RentMovie(2, 3, datetime.date(2018, 4, 23), datetime.date(2018, 4, 28))
    RentMovie(3, 4, datetime.date(2018, 5, 3), datetime.date(2018, 5, 9))
    RentMovie(6, 5, datetime.date(2018, 6, 13), datetime.date(2018, 6, 20))
