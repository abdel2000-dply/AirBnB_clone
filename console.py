#!/usr/bin/python3

import cmd
from models.engine import storage

class HBNBCommands(cmd.Cmd):
    """This defines the class that inherits from the cmd module"""
    intro = "Welcome to AirBnB_clone project"

    prompt = "(hbnb) "

    def do_quit(self, line):
        """exit the shell"""
        return True
    def do_EOF(self, line):
        """handles when an EOF is encountered"""
        return True
    def emptyline(self):
        pass
    def help_quit(self):
        """prints the help message for quit command"""
        print("quit command to exit the program")

    def help_EOF(self):
        """prints the help message for the E-O-F command"""
        print("End of File reached")

    def do_create(self, line):
        '''creates a new instance of BaseModel and saves it to the json file
        '''
        if line == " "or line is None:
            print("** class name missing **")

        elif line not in storage.classes():
            print("** class doesn't exist **")

        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)




if __name__=="__main__":
    HBNBCommands().cmdloop()


