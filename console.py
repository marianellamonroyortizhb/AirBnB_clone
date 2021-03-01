#!/usr/bin/python3

'''
HBNBCommand: contain the entry point of the command
'''
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    '''use cmd to receive a command'''
    prompt = '(hbnb) '

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'Quit command to exit the program'
        return True

    def do_create(self, arg):
        'allows create new instance'
        if len(arg) == 0:
            print("** class name missing **")
        else:
            list_arg = arg.split(' ')
            try:
                instance = eval(list_arg[0] + "()")
                instance.save()
                print(instance.id)
            except:
                print("** class doesn't exist **")

    def do_show(self, arg):
        'allows see an instance specific'
        if len(arg) == 0:
            print("** class name missing **")
        else:
            obj_stored = storage.all()
            list_arg = arg.split(' ')

            try:
                eval(list_arg[0])
            except:
                print("** class doesn't exist **")
                return None

            if len(list_arg) < 2:
                print("** instance id missing **")
                return None

            var = True
            for value in obj_stored.values():
                if value.id == list_arg[1]:
                    print(value)
                    var = False
            if var is True:
                print("** no instance found **")

    def do_destroy(self, arg):
        'Deletes an instance based on it s ID and save the changes'
        list_arg = arg.split()
        if not list_arg:
            print("** class name missing **")
            return None
        try:
            eval(list_arg[0])
        except:
            print("** class doesn't exist **")
            return None

        all_objs = storage.all()

        if len(list_arg) < 2:
                print("** instance id missing **")
                return None

        key = list_arg[0] + '.' + list_arg[1]

        if all_objs.get(key, False):
            all_objs.pop(key)
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        list_arg = arg.split()
        if len(list_arg) > 0:
            try:
                eval(list_arg[0])
            except:
                print("** class doesn't exist **")
                return None

        str_obj = '['
        all_objs = storage.all()
        size_objs = len(all_objs)
        cont = 0
        for value in all_objs.values():
            if not list_arg:
                str_obj += '"' + str(value) + '"'
                cont += 1
                if cont < size_objs:
                    str_obj += ", "
            elif value.__class__.__name__ == list_arg[0]:
                str_obj += '"' + str(value) + '"'
                cont += 1
                if cont < size_objs:
                    str_obj += ", "
        else:
            str_obj += ']'
            print(str_obj)

    def emptyline(self):
        '''it will be execute when press enter no arguments'''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
