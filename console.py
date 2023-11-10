#!/usr/bin/python3
"""This is the console for the AirBnB project"""
import cmd
import json
import readline
import sys
import shlex
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """this class about the console for airbnb project"""

    prompt = "(hbnb) "
    my_class = ["BaseModel"]
    my_ids = []

    def do_quit(self, line):
        """this commnad is used to close the console"""
        quit()

    def help_quit(self):
        """print help message for user"""
        print("quit the consloe")
        print("[USAGE]:\t quit")

    def do_EOF(self, line):
        """This command is  used to close the console"""
        quit()

    def help_EOF(self):
        """print help message for user"""
        print("quit the consloefrom keyboard or after reading a file")
        print("[USAGE]:\t Ctrl+D,Ctrl+Z")

    def emptyline(self):
        """this method is called when user input empty line"""

    def do_create(self, line):
        """ create new model"""
        if line is None:
            print("** class name missing **")
        elif line not in HBNBCommand.my_class:
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            print(obj.id)
            HBNBCommand.my_ids.append(obj)
            obj.save()  # TODO: ADD SAVE METHOD TO BASE CLASS

    def help_create(self):
        """print help message for user"""
        print("create new model")
        print("[USAGE]:\t create <class name>")

    def do_show(self, line):
        """print info about the class"""
        values = HBNBCommand.__spliter(line)
        if values["class_name"] is None:
            print("** class name missing **")
            return
        elif values["class_name"] not in HBNBCommand.my_class:
            print("** class doesn't exist **")
            return
        elif values["id"] is None:
            print("** instance id missing **")
            return

        for i in HBNBCommand.my_ids:
            if i.id == values["id"]:
                print(i)
        print("** instance id missing **")

    def help_show(self):
        """show help message for show command"""
        print("print info about the class")
        print("[USAGE]:\t show <class name> <id>")

    def do_destroy(self, line):
        """destroy the class"""
        values = HBNBCommand.__spliter(line)
        if values["class_name"] is None:
            print("** class name missing **")
            return
        elif values["class_name"] not in HBNBCommand.my_class:
            print("** class doesn't exist **")
            return
        elif values["id"] is None:
            print("** instance id missing **")
            return

        for i in HBNBCommand.my_ids:
            if i.id == values["id"]:
                del i
                return
        print("** instance id missing **")

    def help_destroy(self):
        """show help message for destroy command"""
        print("destroy the class")
        print("[USAGE]:\t destroy <class name> <id>")

    def do_all(self, line):
        keys = HBNBCommand.__spliter(line)
        if (len(keys.items())) == 0:
            return
        # TODO: IF **ALL** HAS NO ARGUMENTS

        if keys["class_name"] not in HBNBCommand.my_class:
            print("** class doesn't exist **")
        else:  # TODO: NOT FORGET TO SEARCH FOR JSON BASEMODEL
            for i in HBNBCommand.my_ids:
                print(i)

    def help_all(self):
        """show help message for all command"""
        print("print all the class")
        print("[USAGE]:\t all <class name>")

    @staticmethod
    def __spliter(line: str):

        kwrds = {}
        args = []
        try:
            args = line.split()
        except ValueError:
            return kwrds

        try:
            cls_name = args[0]
            kwrds["class_name"] = cls_name
        except IndexError:
            kwrds["class_name"] = None

        try:
            id = args[1]
            kwrds["id"] = id
        except IndexError:
            kwrds["id"] = None

        return kwrds


if __name__ == '__main__':
    HBNBCommand().cmdloop()
