#!/usr/bin/python3
""" the entry point of the command interpreter """

import cmd


class HBNBCommand(cmd.Cmd):
    """This defines the class that inherits from the cmd module"""
    intro = "Welcome to AirBnB_clone project"

    prompt = "(hbnb) "

    def do_quit(self, line):
        """exit the shell"""
        return True

    def do_EOF(self, line):
        """handles when an EOF is encountered"""
        print()
        return True

    def emptyline(self):
        pass

    def help_quit(self):
        """prints the help message for quit command"""
        print("exits the shell")

    def help_EOF(self):
        """prints the help message for the E-O-F command"""
        print("End of File")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
