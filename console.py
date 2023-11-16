#!/usr/bin/python3
""" the entry point of the command interpreter """

import cmd


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
