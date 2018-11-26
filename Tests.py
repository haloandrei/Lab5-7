'''
Created on Nov 21, 2018

@author: haloandrei
'''
import unittest
from haloandrei.Business import *
from datetime import datetime

class TestBusiness(unittest.TestCase):
    
    
    def setUp(self):
        self.__title = 'Bohemian Rapsody'
        self.__description = 'Movie about Queen'
        self.__genere = 'Documentary'
        self.__movie = Movie(self.__title,self.__description,self.__genere)
        self.__name = 'Dani Mocanu'
        self.__client = Client( self.__name)
        self.__rentalDate =  datetime(2018, 5, 4)
        self.__returnDate =  datetime(2018, 7, 3)
        self.__dueDate = datetime(2018, 7, 4)
        #print(self.__dueDate.strftime("%a"))
        self.__rental = Rental( self.__movie.getId(), self.__client.getId(), self.__rentalDate, self.__dueDate, self.__returnDate)
    
    def test_addMovie(self):
        addMovie(self.__movie)
        self.assertEqual(self.__movie, getMovieById(2))
    
    def test_addClient(self):
        addClient(self.__client)
        self.assertEqual(self.__client, getClientById(2))
    
    def test_RentMovie(self):
        addMovie(self.__movie)
        addClient(self.__client)
        RentMovie(1, 1, datetime(2018, 4, 23), datetime(2018, 4, 28))
        rental = getRental()[0]
        self.assertEqual(rental.getRentalId(),2)
    
    def test_getMostActiveClient(self):
        client = getMostActiveClient()
        self.assertEqual(client.getId(), 1)
        
    def test_getMostRentedMovie(self):
        movie = getMostRentedMovie()
        self.assertEqual(movie.getId(), 1)
if __name__ == '__main__':
        unittest.main()