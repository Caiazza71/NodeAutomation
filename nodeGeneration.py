from generationData import GenerationData
from message        import Message
from sys            import argv



class NodeGeneration:
    #DEBUG Global
    INFO_OUT, DEBUG_BASIC, DEBUG_VERBOSE = True, False, False
    VALID_ARGUMENTS_SHORT = ["-d", "-dv", "-i", "-h", "-f"] # output modes, directory given instead of found,
    VALID_ARGUMENTS_LONG  = ["--debug", "--debugverbose", "--noinfo", "--help", "--file"]
    FIND_FILE = True

    
    def __sendHelp(self):
        print("help users by printing the args and explainations")
    
    def __init__(self, arg):
        fileName = ""
    
        for i in range(len(arg)):
            match arg[i].lower():                
                case "-d":      self.DEBUG_BASIC = True; print("found debug")
                case "--debug": self.DEBUG_BASIC = True; print("found debug")
    
                case "-dv":            self.DEBUG_BASIC, self.DEBUG_VERBOSE = True, True
                case "--debugverbose": self.DEBUG_BASIC, self.DEBUG_VERBOSE = True, True
                
                case "-i":       self.INFO_OUT = False
                case "--noinfo": self.INFO_OUT = False
                
                case "-h":     self.__sendHelp(); return # return exits the class if help is called
                case "--help": self.__sendHelp(); return
                
                case "-f":     self.FIND_FILE = False; fileName = arg[i+1]; ++i #pulls next arg as filename and increments
                case "--file": self.FIND_FILE = False; fileName = arg[i+1]; ++i
                        
                case default: print(f"ERROR: Invalid Argument \"{arg[i]}\" found"); return
            
            
        if self.DEBUG_BASIC: print("DEBUG: All Args Processed");       
                 
        if not self.__inputFile(fileName): return # Allows for program exit if no file found
                 
        self.inputData = GenerationData(self.file,(self.INFO_OUT, self.DEBUG_BASIC, self.DEBUG_VERBOSE))
        self.__generateMessageFiles()
        
    
    # function for dynamic allocation
    def __inputFile(self, name):
        if not self.FIND_FILE: self.file = name; return True # simple passthrough of the function if name given
        
        #! Here we will need to search the current directory 
        
        
        self.file = "input.satsa"
        return True
    
    def __generateNode():
        pass
    
    def __generateFileStructure():
        pass
    
    def __generateSetupFiles():
        pass
    
    def __generateMessageFiles(self): # update once dir structure is built
        messagelist = self.inputData.getMessages() # saving messages in list
        for message in messagelist:
            filename = message.getName() + '.msg' # creating .msg filename based off message names
            with open(filename, "w") as file:
                for item in message.getTypes():
                    file.write(item[0] + ' ' + item[1] + "\n") # creating .msg file with inputted types

    def __generatePythonFiles():
        # this will def need broken up, basic for pseudo code
        pass
    
if __name__ == "__main__": NodeGeneration(argv[1:]) # passing cmd line args to the __init__
