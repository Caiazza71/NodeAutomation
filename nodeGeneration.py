# Header Needed

# Imported Python Packages
from generationTools import dPrint
from generationTools import Message
from generationTools import sendHelp
from generationTools import makeDirectory
from generationData  import GenerationData
from shutil          import make_archive
from shutil          import rmtree
from sys             import argv
from os              import mkdir


#* Notes
    #* removing any nodes with the same name before execution could save the problem of the program not overwriting the zip archive if one exists

class NodeGeneration:
    ## ---------------  DEBUG & Global  -----------------
    INFO_OUT, DEBUG_BASIC, DEBUG_VERBOSE = True, False, False
    FIND_FILE = True
    
    ZIPPED = True 
    REMOVE = True
    
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
                case "-d":      self.DEBUG_BASIC = True;
                case "--debug": self.DEBUG_BASIC = True;
    
                case "-dv":            self.DEBUG_BASIC, self.DEBUG_VERBOSE = True, True
                case "--debugverbose": self.DEBUG_BASIC, self.DEBUG_VERBOSE = True, True
                
                case "-q":      self.INFO_OUT = False
                case "--quiet": self.INFO_OUT = False
                
                case "-h":     sendHelp(); return # return exits the class if help is called
                case "--help": sendHelp(); return
                
                case "-f":     self.FIND_FILE = False; fileName = arg[i+1]; ++i #pulls next arg as filename and increments
                case "--file": self.FIND_FILE = False; fileName = arg[i+1]; ++i
                
                case "-u":         self.ZIPPED = False; self.REMOVE = False
                case "--unzipped": self.ZIPPED = False; self.REMOVE = False
                
                case "-r":       self.REMOVE = False
                case "--remove": self.REMOVE = False
                        
                case default: print(f"ERROR: Invalid Argument \"{arg[i]}\" found, use -h or --help for correct argument types"); return # Exit Program
            
            
        dPrint(self.DEBUG_BASIC,"DEBUG: All Args Processed");       
             
        if not self.__inputFile(fileName): return # program exit if no file found
                 
        self.inputData = GenerationData(self.file,(self.INFO_OUT, self.DEBUG_BASIC, self.DEBUG_VERBOSE))
    
        if not self.__generateNode(): return      # program exit if generating the node fails        
        
        dPrint(self.INFO_OUT, "INFO: Node and Files created successfully.\nINFO: Nominally exiting program.")
        return # nominal program exit
    
    
    # function for dynamic allocation
    
    #! FUNCTION INCOMPLETE
    
    def __inputFile(self, name):
        if not self.FIND_FILE: self.file = name; return True # simple passthrough of the function if name given
        
        #! Here we will need to search the current directory 
        #* Test with and without text wrapped in quotes IE: "file.name" and file.name
        
        self.file = "input.satsa"
        return True
    
    # Function that handles running the individual components of generation
    def __generateNode(self):
        
        # Setting the node name for generation of directories
        self.NODENAME = self.inputData.getNodeName()
        
        if not self.__generateFileStructure(): return False # program exit if mkdir fails
        
        if not self.__generateMessageFiles(): return False # Program exit if file creation fails
        
        #if not self.__generateSetupFiles(): return False
        
        #if not self.__generatePythonFiles(): return False
        
        if not self.__zipPackages(): return False
        
        return True # All Components executed successfully

    def __zipPackages(self):
        try:
            # Code for Zipping the created Files into archives can be toggled using -u or --unzipped
            if self.ZIPPED: make_archive(self.DIRECTORIES["node"], "zip", self.DIRECTORIES["node"]); dPrint(self.DEBUG_BASIC, "DEBUG: Archive of Node directory Made")            
            if self.ZIPPED: make_archive(self.DIRECTORIES["matlab"], "zip", self.DIRECTORIES["matlab"]); dPrint(self.DEBUG_BASIC, "DEBUG: Archive of matlab directory Made")
                        
            dPrint(self.INFO_OUT, "INFO: Created files zipped successfully.")
        except Exception as e: 
            print(f"ERROR: Zipping folders Failed with error {e}")
            return False
        
        try:
            # Removing folder structure to leave only zipped folder, can be toggled using -r or --remove
            if self.REMOVE: rmtree(self.DIRECTORIES["node"]); dPrint(self.DEBUG_VERBOSE, "DEBUG: Node Directory Removed after Zipping")
            if self.REMOVE: rmtree(self.DIRECTORIES["matlab"]); dPrint(self.DEBUG_VERBOSE, "DEBUG: Matlab Directory Removed after Zipping")
            
            dPrint(self.DEBUG_BASIC, "DEBUG: Removed generated files successfully.")
        except Exception as e: 
            print(f"ERROR: Removing folders Failed with error {e}")
            return False
            
        return True
    
    def __generateFileStructure(self):
        # ---------------  Directory Creation  ---------------
        #           All directories for making the 
        #             node and all output files
        #
        self.DIRECTORIES = {"output"          : f"GeneratedFiles",
                            "matlab"          : f"GeneratedFiles/{self.NODENAME}_Matlab",
                            "matlab_messages" : f"GeneratedFiles/{self.NODENAME}_Matlab/custom_messages",
                            "node"            : f"GeneratedFiles/{self.NODENAME}",
                            "src"             : f"GeneratedFiles/{self.NODENAME}/src",
                            "custom_messages" : f"GeneratedFiles/{self.NODENAME}/src/custom_messages",
                            "msg"             : f"GeneratedFiles/{self.NODENAME}/src/custom_messages/msg",
                            "out"             : f"GeneratedFiles/{self.NODENAME}/src/custom_messages/out",
                            "build"           : f"GeneratedFiles/{self.NODENAME}/src/custom_messages/out/build",
                            "x64-Debug"       : f"GeneratedFiles/{self.NODENAME}/src/custom_messages/out/build/x64-Debug",
                            "sat_sim"         : f"GeneratedFiles/{self.NODENAME}/src/sat_sim",
                            "sat_sim(subDir)" : f"GeneratedFiles/{self.NODENAME}/src/sat_sim/sat_sim",
                            "resource"        : f"GeneratedFiles/{self.NODENAME}/src/sat_sim/resource",
                            "test"            : f"GeneratedFiles/{self.NODENAME}/src/sat_sim/test",
                            "controls"        : f"GeneratedFiles/{self.NODENAME}/src/sat_sim/sat_sim/controls"}
        # ---------------------------------------------------

        #! NEED TO CHECK FOR EXISTING DIRECTORIES HERE AND DELETE THE EXISTING ONES IF FOUND!!!
        
        for currKey, currDir in self.DIRECTORIES.items(): 
            if not makeDirectory(self.DEBUG_VERBOSE, currDir): return False #exits program if MKDIR fails     
           
        dPrint(self.INFO_OUT, "INFO: File Structure Created Successfully")
        
        return True #Tells program that dirs created successfully
    
    def __generateSetupFiles(self):
        pass
      
    def __generateMessageFiles(self):
        #messagelist =  # saving messages in list
        try:
            for message in self.inputData.getMessages():
                #Message in node folder
                filename = self.DIRECTORIES["msg"]+ "/" + message.getName() + '.msg' # creating .msg filename based off message names
                with open(filename, "w") as file:
                    for item in message.getTypes():
                        file.write(item[0] + ' ' + item[1] + "\n") # creating .msg file with inputted types
                        
                #message in matlab folder
                filename = self.DIRECTORIES["matlab_messages"]+ "/" + message.getName() + '.msg' # creating .msg filename based off message names
                with open(filename, "w") as file:
                    for item in message.getTypes():
                        file.write(item[0] + ' ' + item[1] + "\n") # creating .msg file with inputted types
                        
                dPrint(self.DEBUG_BASIC, f"DEBUG: Generated message file {message}.msg")
    
        except Exception as e: print(f"ERROR: Message Files Failed to Generate with error {e}"); return False
        dPrint(self.INFO_OUT, "INFO: Message Files Created")    
        
        return True
    
    def __generatePythonFiles(self):
        # this will def need broken up, basic for pseudo code
        pass
    
if __name__ == "__main__": NodeGeneration(argv[1:]) # passing cmd line args to the __init__
