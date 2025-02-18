# SATSA Node Automation Script
 Files and python code for ROS2 Node generation
 
 ## Project Structure:
This project and its respective files are broken down into three main directories that matter. 
### The main directory 
Contains the main python files and input.satsa and is the default location where the program will start searching for a file if only a name is given. 
### NodeTemplate
This directory contains all files needed when generating the nodes and any hardcoded text we might need in the node that doesnt need to change. These files can be changed by the user at their choosing for different functionality if needed, and will be placed in the node accordingly.
### GeneratedFiles
Most likely not present yet, GeneratedFiles will appear after running the nodeGeneration file and contains all the files needed for running the node. There are two main subudirectories that will be zipped for transportation to their respective places. First, Matlab will contain all the msg files needed that matlab will need to have for publishers, but when creating a simulink program these should be generated for you. They are provided just in case. Secondly is the node folder. This directory will have the name of whatever the "NodeName" variable is set to in the input.satsa (or whatever input file you use). Contained in this folder should be all the components of a ROS2 Node created from the input file and the NodeTemplate Files. Zipped by default, this directory can be left unzipped using the -u or --unzipped flag when running the program.