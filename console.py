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
    Console.py : contains the entry
    point of the command interpreter
    """
    prompt = "(hbnb) "

    classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
               'Amenity': Amenity, 'City': City, 'Review': Review,
               'Place': Place}

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def emptyline(self):
        """
        Overriding emptyline method from cmd module so that
        """
        return False

    def do_EOF(self, line):
        """
        EOF command to exit the program
        """
        print()  # Print a newline before exiting
        return True

    def do_create(self, line):
        """
        Create a new instance.
        """
        # parseline to extract the class name from the
        # user input and then attempts to create an instance of that class.
        class_name = self.parseline(line)[0]

        if class_name is None:
            print("** class name missing **")
        elif class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            # globals is a function returns a dictionary.
            # The keys are the names of all global
            # variables, functions, classes in the current moment.
            # and the values are the class itself.
            # dictionary[key] -> value ((value = class))
            # dictionary["BaseModel"] = BaseModel()
            # instance = class()
            # new_instance = globals()[class_name]()
            new_instance = globals()[class_name]()
            # Note that we can NOT use eval() here becuase eval
            # takes a string containing a dictionary
            # that has the attributes of the instance we want to create
            # and therefore we can't use it with
            # class_name because it's a string that has only the name
            print(new_instance.id)
            # the new_instance is already added to the FileStorage.__objects
            # when the instance was initially created
            # and the call to save just saves what's in there to storage space
            storage.save()

    def do_show(self, line):
        """
        Prints the string representation of an
        instance based on the class name and id.
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
                # THIS LINE MAY CAUSE OR SOLVE PROBLEMS
                setattr(self, "updated_at", datetime.now())
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
