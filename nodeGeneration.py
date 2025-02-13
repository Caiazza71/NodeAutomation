from generationTools import dPrint
from generationData  import GenerationData
from generationTools import Message
from sys             import argv
from os              import mkdir



class NodeGeneration:
    ## ---------------  DEBUG & Global  -----------------
    INFO_OUT, DEBUG_BASIC, DEBUG_VERBOSE = True, False, False
    FIND_FILE = True
    
    NODENAME = ""
    # ---------------------------------------------------
        
    
    # Used as Main function of program. Breaks down all args and executes 
    #      main program pieces one at a time
    def __init__(self, arg):
        fileName = ""
    
        # Breaks down every commandline arg and exits program if 
        #       the user enters an unexpected arg / variable
        for i in range(len(arg)):
            match arg[i].lower():                
                case "-d":      self.DEBUG_BASIC = True; print("found debug")
                case "--debug": self.DEBUG_BASIC = True; print("found debug")
    
                case "-dv":            self.DEBUG_BASIC, self.DEBUG_VERBOSE = True, True
                case "--debugverbose": self.DEBUG_BASIC, self.DEBUG_VERBOSE = True, True
                
                case "-q":       self.INFO_OUT = False
                case "--quiet": self.INFO_OUT = False
                
                case "-h":     self.__sendHelp(); return # return exits the class if help is called
                case "--help": self.__sendHelp(); return
                
                case "-f":     self.FIND_FILE = False; fileName = arg[i+1]; ++i #pulls next arg as filename and increments
                case "--file": self.FIND_FILE = False; fileName = arg[i+1]; ++i
                        
                case default: print(f"ERROR: Invalid Argument \"{arg[i]}\" found"); return # Exit Program
            
            
        dPrint(self.DEBUG_BASIC,"DEBUG: All Args Processed");       
             
        if not self.__inputFile(fileName): return # program exit if no file found
                 
        self.inputData = GenerationData(self.file,(self.INFO_OUT, self.DEBUG_BASIC, self.DEBUG_VERBOSE))
        
        if not self.__generateNode(): return      # program exit if generating the node fails
        
    def __sendHelp(self):
        print("help users by printing the args and explainations")
    
    
    # function for dynamic allocation
    def __inputFile(self, name):
        if not self.FIND_FILE: self.file = name; return True # simple passthrough of the function if name given
        
        #! Here we will need to search the current directory 
        
        
        self.file = "input.satsa"
        return True
    
    # Function that handles running the individual components of generation
    def __generateNode(self):
        
        # Setting the node name for generation of directories
        self.NODENAME = self.inputData.getNodeName()
        
        if not self.__generateFileStructure(): return False # program exit if mkdir fails
        
        
        
        
        return True # All Components executed successfully
        
    # Abstraction function to simplify making directories 
    #   with correct error checking
    def __makeDirectory(self, dirName):
        try: # Try making the directory
            mkdir(dirName)
            dPrint(self.DEBUG_VERBOSE, f"DEBUG: Directory '{dirName}' created successfully.")
        except FileExistsError:
            dPrint(self.DEBUG_VERBOSE,f"DEBUG: Directory '{dirName}' already exists.")
            return True
        except PermissionError:
            print(f"ERROR: Permission denied: Unable to create '{dirName}'.")
            return False
        except Exception as e:
            print(f"ERROR: {e} when creating directory")
            return False
        return True # Successfully Created
    
    def __generateFileStructure(self):
        # ---------------  Directory Creation  ---------------
        #           All directories for making the 
        #             node and all output files
        #
        self.DIRECTORIES = {"output"          :f"GeneratedFiles",
                            "matlab"          :f"GeneratedFiles/Matlab",
                            "node"            :f"GeneratedFiles/{self.NODENAME}",
                            "src"             :f"GeneratedFiles/{self.NODENAME}/src",
                            "custom_messages" :f"GeneratedFiles/{self.NODENAME}/src/custom_messages",
                            "msg"             :f"GeneratedFiles/{self.NODENAME}/src/custom_messages/msg",
                            "out"             :f"GeneratedFiles/{self.NODENAME}/src/custom_messages/out",
                            "build"           :f"GeneratedFiles/{self.NODENAME}/src/custom_messages/out/build",
                            "x64-Debug"       :f"GeneratedFiles/{self.NODENAME}/src/custom_messages/out/build/x64-Debug",
                            "sat_sim"         :f"GeneratedFiles/{self.NODENAME}/src/sat_sim",
                            "sat_sim(subDir)" :f"GeneratedFiles/{self.NODENAME}/src/sat_sim/sat_sim",
                            "resource"        :f"GeneratedFiles/{self.NODENAME}/src/sat_sim/resource",
                            "test"            :f"GeneratedFiles/{self.NODENAME}/src/sat_sim/test",
                            "controls"        :f"GeneratedFiles/{self.NODENAME}/src/sat_sim/sat_sim/controls"}
        # ---------------------------------------------------
        
        
        for currKey, currDir in self.DIRECTORIES.items():
            if not self.__makeDirectory(currDir): return False #exits program if MKDIR fails     
           
        return True #Tells program that dirs created successfully
    
    def __generateSetupFiles():
        pass
      
    def __generateMessageFiles():
        pass
    
    def __generatePythonFiles():
        # this will def need broken up, basic for pseudo code
        pass
    
if __name__ == "__main__": NodeGeneration(argv[1:]) # passing cmd line args to the __init__
