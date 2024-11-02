


class Parser:
    # Class variables
    nodeName = "None"
    messages = []
    
    # Default
    def __init__ (self, fileName):
        print("DEBUG: Starting Parsing")
        
        #File Object Creation
        self.file = open(fileName)
        
        # Reading the File
        self.__getNodeName()
        self.__createMessages()
        
    # Private Functions
    def __getNodeName(self):
        print("DEBUG: Node Name Found ", self.NodeName)
        pass
    
    def __getMessage(self):
        messageName = ""
        messageTypes = []
        
        print("DEBUG: Node Name Found ", messageName)
        return
    
    def __createMessages(self):
        
        
        print("DEBUG: Node Name Found ", self.messages)
        return
    
    # Public getters
    def getMessages(self): return self.messages
    def getNodeName(self): return self.NodeName
        




if (__name__=="__main__"):
    Parser("input.satsa")
