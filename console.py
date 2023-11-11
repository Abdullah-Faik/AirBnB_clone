#!/usr/bin/python3
"""This is the console for the AirBnB project"""
import cmd
import json
import readline
import sys
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """this class about the console for airbnb project"""

    prompt = "(hbnb) "
    my_class = ["BaseModel"]

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
        print("quit the consloe from keyboard or after reading a file")
        print("[USAGE]:\t Ctrl+D,Ctrl+Z")

    def emptyline(self):
        """this method is called when user input empty line"""
        pass

    def do_create(self, line):
        """ create new model"""
        if line is None:
            print("** class name missing **")

        elif line not in HBNBCommand.my_class:
            print("** class doesn't exist **")

        else:
            obj = BaseModel()
            print(obj.id)
            storage.new(obj)

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

        try:
            print(str(storage.all()[
                  values["class_name"] + "." + values["id"]]))

        except KeyError:
            print("** no instance found **")

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

        try:
            del storage.all()[values["class_name"]+"."+values["id"]]
            storage.save()
            # storage.reload()

        except KeyError:
            print("** instance id missing **")

    def help_destroy(self):
        """show help message for destroy command"""
        print("destroy the class")
        print("[USAGE]:\t destroy <class name> <id>")

    def do_all(self, line):
        keys = HBNBCommand.__spliter(line)
        users = []
        if (len(keys.items())) == 0:
            return

        if keys["class_name"] is None:
            print([str(val) for val in storage.all().values()])
            return

        if keys["class_name"] not in HBNBCommand.my_class:
            print("** class doesn't exist **")
            return

        else:
            for key, val in storage.all().items():
                fword, _ = key.split(".")
                if fword == keys["class_name"]:
                    users.append(str(val))
        print(users)

    def help_all(self):
        """show help message for all command"""
        print("print all the class")
        print("[USAGE]:\t all <class name>")

    def do_update(self, line):
        """update the class argumens"""

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

        elif values["attr"] is None:
            print("** attribute name missing **")
            return

        elif values["value"] is None:
            print("** value missing **")
            return

        try:
            obj = storage.all()[values["class_name"]+"."+values["id"]]
            setattr(obj, values["attr"], values["value"])
            obj.save()

        except KeyError:
            print("** no instance found **")

    def help_update(self):
        """show help message for update command"""
        print("update the class argumens")
        print("[USAGE]:\t update <class name> <id> <attribute name> <value>")

    @staticmethod
    def __spliter(line: str):
        """split the line into args"""
        kwrds = {}
        args = []

        try:
            args = shlex.split(line)
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

        try:
            attr = args[2]
            kwrds["attr"] = attr
        except IndexError:
            kwrds["attr"] = None

        try:
            value = args[3]
            kwrds["value"] = value
        except IndexError:
            kwrds["value"] = None

        return kwrds

    @staticmethod
    def to_type(value):
        """convert the value to type"""
        if value.isdigit():
            return int(value)
        try:
            return float(value)
        except ValueError:
            return value


if __name__ == '__main__':
    HBNBCommand().cmdloop()
