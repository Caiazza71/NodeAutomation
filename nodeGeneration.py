from generationData import GenerationData
from message        import Message
from sys            import argv



class NodeGeneration:
    #DEBUG Global
    INFO_OUT, DEBUG_BASIC, DEBUG_VERBOSE = True, False, False
    VALID_ARGUMENTS_SHORT = ["--d", "--dv", "--i", "--h", "--f"] # output modes, directory given instead of found,
    VALID_ARGUMENTS_LONG  = ["-debug", "-debugverbose", "-noinfo", "-help", "-file"]
    FIND_FILE = True
    
    def __checkArguments(arguments):
        # ERROR if they use both debugs
        # Error if the use an incorrect arg and maybe call sendHelp()
        
        return False # false means it fails and args not valid
    
    def __sendHelp():
        print("help users by printing the args and explainations")
    
    def __init__(self, arg):
        if not self.__checkArguments(): return # Ensure valid Arguments
        fileName = ""
        
        for i in range(len(arg)):
            if arg[i].lower() == "--d" or arg[i].lower() == "-debug": self.DEBUG_BASIC = True
            if arg[i].lower() == "--dv" or arg[i].lower() == "-debugverbose": self.DEBUG_BASIC, self.DEBUG_VERBOSE = True
            if arg[i].lower() == "--i" or arg[i].lower() == "-noinfo": self.INFO_OUT = False
            if arg[i].lower() == "--h" or arg[i].lower() == "-help": self.__sendHelp(); return # return exits the class if help is called
            if arg[i].lower() == "--f" or arg[i].lower() == "-file": self.FIND_FILE = False; fileName = arg[i+1]; ++i
                 
        if not self.__inputFile(fileName): return # Allows for program exit if no file found
                 
        inputData = GenerationData(self.file,(self.INFO_OUT, self.DEBUG_BASIC, self.DEBUG_VERBOSE))
    
    # function for dynamic allocation
    def __inputFile(self, name):
        if not self.FIND_FILE: self.file = name; return True # simple passthrough of the function if name given
        
        # Here we will need to search the current directory 
        
        return "input.satsa"
    
    def __generateNode():
        pass
    
    def __generateFileStructure():
        pass
    
    def __generateSetupFiles():
        pass
    
    def __generateMessageFiles():
        pass
    
    def __generatePythonFiles():
        # this will def need broken up, basic for pseudo code
        pass
    
if __name__ == "__main__": NodeGeneration(argv) # passing cmd line args to the __init__