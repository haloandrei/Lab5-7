class Client():
    
    CurrentId = 1
    
    def __init__(self, nameParameter):
        self.__clientId = Client.CurrentId
        self.__name = nameParameter
        Client.CurrentId += 1
    
    def getId(self):
        return self.__clientId


    def getName(self):
        return self.__name


    def setClientId(self, value):
        self.__clientId = value


    def setName(self, value):
        self.__name = value
        
    def ToString(self):
        return str(self.__clientId) + ' | ' + str(self.__name)