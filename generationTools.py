# File for holding all development tools and smaller functions for NodeGeneration

from os import mkdir


# Debug Print that simplifies debug code when printing to console
def dPrint(boolean,statement):
    if boolean: print(statement)

# Abstraction function to simplify making directories 
#   with correct error checking
def makeDirectory(DEBUG_VERBOSE, dirName):
    try: # Try making the directory
        mkdir(dirName)
        dPrint(DEBUG_VERBOSE, f"DEBUG: Directory '{dirName}' created successfully.")
    except FileExistsError:
        dPrint(DEBUG_VERBOSE,f"DEBUG: Directory '{dirName}' already exists.")
        return True
    except PermissionError:
        print(f"ERROR: Permission denied: Unable to create '{dirName}'.")
        return False
    except Exception as e:
        print(f"ERROR: {e} when creating directory")
        return False
    return True # Successfully Created Dir

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
        
# help function abstracted into tools for program reabability
def sendHelp():
        print("\n")
        print( "                --- Welcome to the SATSA ROS2 Node Generation Software --- \n",
               "   This help mode is aimed to guide users through the different flags and program run states\n", 
               "                         avalible to you when using this script.\n")
        
        print("\nRunning The Program:",
              "\n   By Default the program searches the current directory for an input.satsa",
              "\n   file. If you are generating multiple nodes with different file names use",
              "\n   the -f flag for designating the input file name.\n",
              "\n   EX: nodeGeneration.py -f \"My File Name\"\n")
        
        print( "%-10s %-15s %s" % ("Runtime Flags:","", "Usage:") )
        print( "%-9s %-16s   " % ("Short:","Full:") )
        print( "%-9s %-16s %s" % ("-h","--help", "Outputs this help page for program functionality") )
        print( "%-9s %-16s %s" % ("-d","--debug", "Prints basic debug output for program tracing.") )
        print( "%-9s %-16s %s" % ("-dv","--debugverbose", "Prints all debug output possible, helpful for locating precise program faults.") )
        print( "%-9s %-16s %s" % ("-q","--quiet", "Removes all console output when Generating Nodes including INFO.") )
        print( "%-9s %-16s %s" % ("-f","--file", "Allows for user defined input file names to replace default input.satsa") )
        print( "%-9s %-16s %s" % ("-u","--unzipped", "Stops the program from zipping and removing the output code folders.") )
        print( "%-9s %-16s %s" % ("-r","--remove", "Stops the program from removing the directory of the generated files after zipping") )
