import os
import commands
from commands import *

#global var tex current_dir

#dics (giltiga commandon) key: CD & value: func ->
#dics
#dics

#class (error handle)
class HandleAll:
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
            "cls": [sh_cls, [0]],  #same
            "clear": [sh_cls, [0]], #same
            "exit": [sh_exit, [0]], #same
            "quit": [sh_exit, [0]], #same
            "q": [sh_exit, [0]] #same
        }

    def command_exists(self):
        '''Determine if a command exists'''
        if self.command_split[0] in self.valid_commands:
            return True
        return False
    
    def command_arg_count(self):
        '''Check if amount of arguments is correct'''
        # antal args korrekt
        # räkna ut antal argument
        # self.command_split = ["cd", "Desktop"]  ->  1  (2 - 1)
        self.arg_count = len(self.command_split) - 1
        if self.arg_count not in self.valid_commands[self.command_split[0]][1]:
            return False
        return True

    def command_valid_args(self):
        '''Check if the arguments provided are valid'''
        # create a list of all arguments
        self.args = [os.path.normpath(os.path.join(commands.current_dir, arg)) for arg in self.command_split]
        # self.args = [arg for arg in self.command_split]
        command = self.args.pop(0)

        # if command is echo do something different
        if command == "echo":
            if self.arg_count == 3:  # echo Hej > fil.txt
                if self.args[1] != ">":
                    return False
                if not os.path.exists(self.args[2]):
                    return False
            return True
        
        # if command is move copy xcopy only check if source is a valid path
        if command == "move" or command == "copy" or command == "xcopy":  # move fil.txt mapp/fil.txt
            if not os.path.exists(self.args[0]):
                return False
            return True

        # otherwise check if arguments are valid paths / files
        # os.path.abspath()
        for arg in self.args:
            if not os.path.exists(arg):
                return False

            '''x = os.path.join(commands.current_dir, arg)
            print(f"{arg=}, {x=}, {os.path.normpath(x)}")
            if not os.path.exists(os.path.normpath(x)):
                return False
            continue
            if os.path.isabs(arg):
                print("absolut", arg)
                if not os.path.exists(arg):
                    return False
            else:
                print("relativ", arg, commands.current_dir + "\\" + arg)
                if not os.path.exists(commands.current_dir + "\\" + arg):
                    return False'''
        return True

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
        
        if not self.command_exists():
            print("Command does not exist.")
            return False
        
        if not self.command_arg_count():
            print("Invalid syntax.")
            return False
        
        if not self.command_valid_args():
            print("Invalid arguments.")
            return False
        
        # print("Success:", self.command_input, " -> ", self.command_split)
        return True

    def call_command(self):
        self.valid_commands[self.command_split[0]][0](self.args)  # get the function from the dictionary and call it

        # sh_dir()
        # sh_dir(self.args)
        # sh_dir(path=self.args[0], x="abc", y="def")
        # sh_dir(self.args[0], "abc", "def")  *args

        #try/except
        #OBS    
        #valid path     #tex "move" finns commandot? & "fil.txt" "mapp/fil.txt" finns dessa två argument?
                                                                                #fungerar dom tillsammans?

def main():
    commands.current_dir = os.getcwd()  # get current directory
    while True:
        command_input = input(f"SH {commands.current_dir}> ") #det är en string
        command1 = HandleAll(command_input)
        if command1.process_input():
            command1.call_command()

        #current_dir = "" #platsposition

main()
