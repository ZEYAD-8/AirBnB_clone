#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""
import cmd
from shlex import split
from datetime import datetime
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand: Interactive Command-Line Interface

    This class defines a command-line interpreter for a hypothetical
    application (HBNB) with functionality to create, show, update,
    and delete instances of various classes.

    Attributes:
    - prompt: The command prompt displayed to the user.
    - classes: A dictionary mapping class names to their corresponding
    class objects.

    Methods:
    - do_quit: Command to exit the program.
    - emptyline: Overrides cmd module's emptyline method.
    - do_EOF: Command to exit the program on EOF (Ctrl-D).
    - do_create: Creates a new instance of a specified class.
    - do_show: Prints the string representation of an instance.
    - do_destroy: Deletes an instance based on class name and id.
    - do_all: Prints string representations of instances.
    - do_update: Updates an instance's attribute and saves changes.

    Usage Examples:
    (hbnb) cmd = HBNBCommand()
    (hbnb) cmd.cmdloop()
    """
    prompt = "(hbnb) "

    classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
               'Amenity': Amenity, 'City': City, 'Review': Review,
               'Place': Place}

    def do_quit(self, line):
        """
        Quit command to exit the program.

        Examples:
            (hbnb) quit
        """
        return True

    def emptyline(self):
        """
        Overriding emptyline method from cmd module so that
        """
        return False

    def do_EOF(self, line):
        """
        EOF command to exit the program.

        Examples:
            (hbnb) Ctrl-D
        """
        print()
        return True

    def do_create(self, line):
        """
        Create a new instance.

        Examples:
            (hbnb) create BaseModel
        """
        class_name = self.parseline(line)[0]

        if class_name is None:
            print("** class name missing **")
        elif class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = globals()[class_name]()
            print(new_instance.id)
            storage.save()

    def do_show(self, line):
        """
        Prints the string representation of an
        instance based on the class name and id.

        Examples:
            (hbnb) show BaseModel 1234-1234-1234
        """
        class_name, id, rest = self.parseline(line)

        if class_name is None:
            print("** class name missing **")
        elif class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif id is None or id == "":
            print("** instance id missing **")
        else:
            key = class_name + "." + id
            object_get = storage.all().get(key)
            if object_get is None:
                print("** no instance found **")
            else:
                print(object_get)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id.

        Examples:
            (hbnb) destroy BaseModel 1234-1234-1234
        """
        class_name, id, rest = self.parseline(line)

        if class_name is None:
            print("** class name missing **")
        elif class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif id is None:
            print("** instance id missing **")
        else:
            key = class_name + "." + id
            object_get = storage.all()(key)
            if object_get is None:
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all
        instances based or not on the class name.

        Examples:
            (hbnb) all
            (hbnb) all BaseModel
        """
        class_name = self.parseline(line)[0]
        instances = []

        if class_name is None:
            for key, obj in storage.all().items():
                instances.append(obj.__str__())
            print(instances)
        elif class_name not in globals():
            print("** class doesn't exist **")
        else:
            for key, obj in storage.all().items():
                if key.startswith(class_name):
                    instances.append(obj.__str__())
            print(instances)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        (save the change into the JSON file).

        Examples:
            (hbnb) update BaseModel 1234-1234-1234
                attribute_name "new value"
        """
        args = split(line)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            object_get = storage.all()[key]
            if object_get is None:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                setattr(object_get, args[2], args[3])
                setattr(self, "updated_at", datetime.now())
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
