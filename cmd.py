import os
import commands
from commands import *

# Classes for error handling
class CommandNotExistError(Exception):
    pass

class ArgCountError(Exception):
    pass

class CommandSyntaxError(Exception):
    pass

class PathNotExistError(Exception):
    pass

# raise Error("meddelande")

#class (error handle)
class HandleCommand:
    def __init__(self, command):
        self.command_input = command
        self.command_split = []
        self.valid_commands = {
            "dir": [sh_dir, [0, 1]],    #0=func soon (utan parantes)
            "cd": [sh_cd, [1]],
            "cd..": [sh_cddotdot, [0]],
            "cd/": [sh_cdslash, [0]],
            "md": [sh_md, [i for i in range(1, 69)]],
            "rd": [sh_rd, [i for i in range(1, 69)]],
            "erase": [sh_remove, [i for i in range(1, 69)]], #same
            "del": [sh_remove, [i for i in range(1, 69)]],   #same
            "remove": [sh_remove, [i for i in range(1, 69)]], #same
            "rename": [sh_rename, [2]],
            "xcopy": [sh_xcopy, [2]],
            "copy": [sh_copy, [2]],
            "move": [sh_move, [2]],
            "echo": [sh_echo, [1, 3]],
            "type": [sh_type, [1]],
            "cls": [sh_cls, [0]],  #same
            "clear": [sh_cls, [0]], #same
            "exit": [sh_exit, [0]], #same
            "quit": [sh_exit, [0]], #same
            "q": [sh_exit, [0]] #same
        }

    def command_exists(self):
        '''Determine if a command exists'''
        if not self.command_split[0] in self.valid_commands:  # command in self.valid_commands
            raise CommandNotExistError("Command does not exist.")
    
    def command_arg_count(self):
        '''Check if amount of arguments is correct'''
        # antal args korrekt
        # räkna ut antal argument
        # self.command_split = ["cd", "Desktop"]  ->  1  (2 - 1)
        self.arg_count = len(self.command_split) - 1
        if self.arg_count not in self.valid_commands[self.command_split[0]][1]:
            if self.command_split[0] == "echo":
                raise ArgCountError("Invalid amount of arguments.\nRemember to include '>' when outputting to a file.")
            raise ArgCountError("Invalid amount of arguments.")

    def command_valid_args(self):
        '''Check if the arguments provided are valid'''
        command = self.command_split[0]

        # if command is echo do something different
        if command == "echo":
            self.args[0] = self.command_split[1]  # set args[0] to raw input value
            if self.arg_count == 3:  # echo Hej > fil.txt
                self.args[1] = self.command_split[2]  # set args[1] to raw input value
                if self.args[1] != ">":
                    raise CommandSyntaxError("Syntax error. Missing '>'.")
            return
        
        # if command is move copy xcopy only check if source is a valid path
        if command == "move" or command == "copy" or command == "xcopy":  # move fil.txt mapp/fil.txt
            if not os.path.exists(self.args[0]):
                raise PathNotExistError(f"Path '{self.args[0]}' does not exist.")
            return

        if command == "md":
            # ignore checking arguments if command is 'md'
            return

        # otherwise check if arguments are valid paths / files
        for arg in self.args:
            if not os.path.exists(arg):
                raise PathNotExistError(f"Path '{arg}' does not exist.")

            '''
            if os.path.isabs(arg):
                print("absolut", arg)
                if not os.path.exists(arg):
                    return False
            else:
                print("relativ", arg, commands.current_dir + "\\" + arg)
                if not os.path.exists(commands.current_dir + "\\" + arg):
                    return False
            '''

    def process_input(self):
        '''Process and validate command + arguments'''
        # '   '
        # ''
        # 'cd C:\'  ->  ["cd", "C:\"]
        if self.command_input.strip() == "":
            # print("Please enter valid command.")
            return False
        
        # split command into list, where [0] is command 
        self.command_split = self.command_input.split()

        # create a list of all arguments and append to current_dir + normalize them
        self.args = [os.path.normpath(os.path.join(commands.current_dir, arg)) for arg in self.command_split]
        self.args.pop(0)  # pop out the command from self.args

        try:
            self.command_exists()
            self.command_arg_count()
            self.command_valid_args()
        except (CommandNotExistError, ArgCountError, CommandSyntaxError, PathNotExistError) as error:
            print(error)
            return False
        except Exception as error:
            print(f"Unexpected error. {error}")
            return False
        
        return True

    def call_command(self):
        # try except to catch unwanted errors
        try:
            self.valid_commands[self.command_split[0]][0](self.args)  # get the function from the dictionary and call it
        except Exception as error:
            print(error)

        # sh_md(self.args)
        # sh_dir()
        # sh_dir(self.args)

        
        # sh_dir(path=self.args[0], x="abc", y="def")
        # sh_dir(self.args[0], "abc", "def")  *args

def main():
    commands.current_dir = os.getcwd()  # get current directory
    while True:
        command_input = input(f"SH {commands.current_dir}> ") #det är en string
        command = HandleCommand(command_input)
        if command.process_input():
            command.call_command()

        #current_dir = "" #platsposition

main()
