#!/usr/bin/python3
""" the entry point of the command interpreter """

import cmd
from models.engine import storage


class HBNBCommand(cmd.Cmd):
    """This defines the class that inherits from the cmd module"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        pass
<<<<<<< HEAD
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



'''    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg not in storage.classes:
            print("** class doesn't exist **")
	else
'''

if __name__ == '__main__':
    HBNBCommand().cmdloop()
