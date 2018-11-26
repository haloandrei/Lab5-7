class Client():
    
    CurrentId = 1
    
    def __init__(self, nameParameter):
        self.__clientId = Client.CurrentId
        self.__name = nameParameter
        self.__activity = 0
        Client.CurrentId += 1
    
    def getActivity(self):
        return self.__activity
    
    def incActivity(self, days):
        self.__activity += days
    
    def getAmbiguous(self, Field):
        if(Field == 'id') :
            return self.getId()
        elif (Field == 'name') :
            return self.getName()
        print (Field)
    def getId(self):
        return self.__clientId


    def getName(self):
        return self.__name


    def setClientId(self, value):
        self.__clientId = value


    def setName(self, value):
        self.__name = value
        
    def ToString(self):
        return str(self.__clientId) + ' | ' + str(self.__name) + ' | ' + str(self.__activity)