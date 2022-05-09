import os
import sys

class Path:
    def help(self,command=None):
    #dictionary about the commands with small explanation about them
        help_list={"cd":"Change the current default directory to.\n     If the argument is not present, report the current directory.\n     If the directory does not exist an appropriate error should be reported.\n",
               "clear":"Clear the screen",
               "dir":"List the contents of directory and subdirectories in a directory.",
               "quit":"Quit the shell.",
               "copy":"Copies one or more files to another location",
               "del":"Deletes one or more files.",
               "help":"Provides Help information for commands.",
               "md":"Creates a directory.","rd":"Removes a directory.",
               "rename":"Renames a file.","type":"Displays the contents of a text file.",
               "import":"import text file(s) from your computer.",
               "export":"export text file(s) to your computer."
               }
            
        if command in help_list :
            print(command + " - "+help_list[command])
    
        elif command==None:
            for commnd , description in help_list.items(): 
                print("{} - {}".format(commnd,description))



    def init(self):
        print("(c) Shell project. All rights reserved to kerolus gerges).\n\n")
        while True:
            #Get input from user whatever the command lower or upper case (not key sensetive)
            self.path = input('F:\>').lower().split()
            #if the user doesn`t write any command and press enter the shell will go in new line waiting for a command to execute
            if len(self.path) == 0:
                continue
            #if the user type "Quit" the shell will quit 
            if self.path[0] == "quit":
                quit()
            
                
        
            #if the user type "Clear" the shell will clear the screen
            elif self.path[0] == "clear":
                os.system("cls")
                print("(c) Shell project. All rights reserved to (kerolus gerges).\n")
        
            #if the user type "Help" by default the shell will say to you all the commands
            elif self.path[0] == "help":
                if len(self.path) == 1:
                    self.help()
            #but if the user give another attribute the shell will give a small brief about the specific attribute
                elif len(self.path) > 1:
                    if self.path[1] == "cd":
                        self.help("cd")
                    elif self.path[1] == "clear":
                        self.help("clear")
                    elif self.path[1] == "dir":
                        self.help("dir")
                    elif self.path[1] == "copy":
                        self.help("copy")
                    elif self.path[1] == "quit":
                        self.help("quit")
                    elif self.path[1] == "type":
                        self.help("type")
                    elif self.path[1] == "rd":
                        self.help("rd")
                    elif self.path[1] == "del":
                        self.help("del")
                    elif self.path[1] == "help":
                        self.help("help")
                    elif self.path[1] == "md":
                        self.help("md")
                    elif self.path[1] == "rename":
                        self.help("rename")
                    elif self.path[1] == "import":
                        self.help("import")
                    elif self.path[1] == "export":
                        self.help("export")
                    
            #if the user give unvalid command the shell will give a message that the command is not recognized 
            else:
                print('"{}" is not recognized as an internal or external command\n'.format(self.path[0]))

                

