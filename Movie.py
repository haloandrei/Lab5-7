class Movie():
    
    CurrentId = 1
    
    def __init__(self, titleParameter, descriptionParameter, generParameter):
        self.__movieId = Movie.CurrentId
        self.__title = titleParameter
        self.__description = descriptionParameter
        self.__genere = generParameter
        self.__timesRented = 0
        Movie.CurrentId += 1
    
    def getAmbiguous(self, Field):
        if(Field == 'id') : return self.getId()
        elif (Field == 'title') : return self.getTitle()
        elif (Field == 'description') : return self.getDescription()
        elif (Field == 'genere') : return self.getGenere()
        
    def getId(self):
        return self.__movieId
    
    def getTimesRented(self):
        return self.__timesRented
    
    def incTimesRented(self):
        self.__timesRented += 1

    def getTitle(self):
        return self.__title


    def getDescription(self):
        return self.__description


    def getGenere(self):
        return self.__genere


    def setId(self, value):
        self.__movieId = value


    def setTitle(self, value):
        self.__title = value


    def setDescription(self, value):
        self.__description = value


    def setGenere(self, value):
        self.__genere = value
    
    def ToString(self):
        return str(self.__movieId) + ' | ' + str(self.__title) + ' | ' + str(self.__description) + ' | ' + str(self.__genere) + ' | ' + str(self.__timesRented)
    
        