# class for managing messages as objects for easier access 

class Message:
        
        def __init__(self, name): self.__name = name; self.__types = []; __pubSub = "N"
        def __repr__(self): return self.__name # debug message representation
        def __str__(self): return self.__name  # string representation
        
        def getName(self):  return self.__name
        
        def addType(self, newType): self.__types.append(newType) # newType is an array of type and name
        def getTypes(self): return self.__types
        
        def setPubSub(self, ps): self.__pubSub = ps # needs to be "P" or "S"
        def getPubSub(self): return self.__pubSub