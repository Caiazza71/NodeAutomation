from message import Message



# This Class aims to be instantiated with a file name that follows the .satsa format 
# specified by the 
class GenerationData:
    #DEBUG Global
    INFO_OUT, DEBUG_BASIC, DEBUG_VERBOSE = True, True, False
    
    
    # Class variables
    __nodeName, __messages = "None", []       
    
    # getting file in and breaking into different parsing modes
    def __init__ (self, fileName):
        if self.DEBUG_BASIC: print("DEBUG: Starting Parsing") # debug
        
        #File Object Creation
        self.file = open(fileName, "r")
        
        # Reading the File and stripping out useful parts we want
        self.__getNodeName(); self.__createMessages()
        
    # Pulling in the NodeName
    def __getNodeName(self):
        exitChar = 0
        for line in self.file: # looping over every line in the file
            if line[0] != "#": # # char is a comment line
                if line[0:8] == "NodeName": self.__nodeName = line[11:-2] 
                elif line[0] == "-":# Exit char - denotes end of parsing section
                    exitChar += 1
                    if exitChar == 2: break
        
        if self.DEBUG_BASIC: print("DEBUG: Node Name Found:", self.__nodeName) # debug
    
    # Gets the types of a message and appends them to the sent object
    def __getMessageTypes(self, message):
        exitChar = 0
        for line in self.file:
            if line.__contains__("{") or line.__contains__("}"): # looking for exit chars
                exitChar += 1
                if exitChar == 2: break
                
            if line.__contains__("MessageType="): message.setPubSub(line[14:-1]) # Finding the type "Publish" or "Subscribe"
                
            else: message.addType(line.strip().split()) # adding the type and name to the message object
                
        if self.DEBUG_BASIC: print("DEBUG: Found Message:", message.getName(), "with", len(message.getTypes()), "Types and method", message.getPubSub()) # debug
        if self.DEBUG_VERBOSE: print("DEBUG: Address:", id(message), "\nDEBUG: Types:", message.getTypes())             # debug
        return message
    
    # Creating a message type once a new message name is found
    def __createMessages(self):
        exitChar = 0
        for line in self.file: # looping over every line in the file
            if line[0] != "#": # # char is a comment line
                if line[0:11] == "MessageName": # finds the start of a message
                    self.__messages.append(self.__getMessageTypes(Message(line[14:-2]))) # append and create new message
                elif line[0] == "-": # Exit char - denotes end of parsing section
                    exitChar += 1
                    if exitChar == 2: break
                    
                # * redundency could be added here: if a wrong char is found throws error
        
        if self.INFO_OUT: print("INFO: Messages Found:", self.__messages) # debug
        return
    
    # Public getters
    def getMessageNames(self): return self.__messages
    def getNodeName(self): return self.__NodeName
    def getMessages(self): return "WIP FUNCTION"
        


if (__name__=="__main__"):
    GenerationData("input.satsa")
