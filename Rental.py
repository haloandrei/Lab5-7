'''
Created on Nov 6, 2018

@author: haloandrei
'''

class Rental():
    CurrentId = 1
    
    def __init__(self, movieIdParameter, clientIdParameter, rentedDateParameter, dueDateParameter, returnedDateParameter):
        #<rentalID>, <movieId>, <clientId>, <rented date>, <due date>, <returned date>
        self.__rentalId = Rental.CurrentId
        self.__movieId = movieIdParameter
        self.__clientId = clientIdParameter
        self.__rentedDate = rentedDateParameter
        self.__dueDate = dueDateParameter
        self.__returnDate = returnedDateParameter
        Rental.CurrentId += 1
 
    def getRentalId(self):
        return self.__rentalId


    def getMovieId(self):
        return self.__movieId


    def getClientId(self):
        return self.__clientId


    def getRentedDate(self):
        return self.__rentedDate


    def getDueDate(self):
        return self.__dueDate


    def getReturnDate(self):
        return self.__returnDate


    def setRentalId(self, value):
        self.__rentalId = value


    def setMovieId(self, value):
        self.__movieId = value


    def setClientId(self, value):
        self.__clientId = value


    def setRentedDate(self, value):
        self.__rentedDate = value


    def setDueDate(self, value):
        self.__dueDate = value


    def setReturnDate(self, value):
        self.__returnDate = value
        
    def ToString(self):
        return str(self.__rentalId) + '|' +  str(self.__movieId) + '|' +  str(self.__clientId) + '|' +  str(self.__rentedDate) + '|' +  str(self.__dueDate) + '|' +  str(self.__returnDate) 