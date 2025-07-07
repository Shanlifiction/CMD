""" PYTHON CMD PROJECT """

### import modules ###
import os  # path.normpath(), path.join(), path.exists()
import commands  # importera vår egna modul
from commands import *  # importera vår egna modul igen :)

### classes for error handling, inherits from Exception ###
class CommandNotExistError(Exception):
    pass

class ArgCountError(Exception):
    pass

class CommandSyntaxError(Exception):
    pass

class PathNotExistError(Exception):
    pass

### class to process the command input ###
class HandleCommand:
    def __init__(self, command):
        self.command_input = command  # använderans inmatning
        self.command_split = []  # self.command_input.split(), [0] är kommandot
        self.valid_commands = {  # dict som innehåller alla giltiga kommandon respektive deras funktioner
        #   "kommando": [sh_funktion, [antal giltiga argument, ...]]
            "sigma": [sh_dir, [0, 1]],  # sh_dir
            "dir": [sh_dir, [0, 1]],    # sh_dir
            "cd": [sh_cd, [1]],
            "cd..": [sh_cddotdot, [0]],
            "cd/": [sh_cdslash, [0]],
            "md": [sh_md, [i for i in range(1, 69)]],
            "rd": [sh_rd, [i for i in range(1, 69)]],
            "erase": [sh_remove, [i for i in range(1, 69)]],   # sh_remove
            "del": [sh_remove, [i for i in range(1, 69)]],     # sh_remove
            "remove": [sh_remove, [i for i in range(1, 69)]],  # sh_remove
            "rename": [sh_rename, [2]],
            "xcopy": [sh_xcopy, [2]],
            "copy": [sh_copy, [2]],
            "move": [sh_move, [2]],
            "echo": [sh_echo, [1, 3]],
            "type": [sh_type, [1]],
            "cls": [sh_cls, [0]],    # sh_cls
            "clear": [sh_cls, [0]],  # sh_cls
            "exit": [sh_exit, [0]],  # sh_exit
            "quit": [sh_exit, [0]],  # sh_exit
            "q": [sh_exit, [0]]      # sh_exit
        }

    ### check if the command exists ###
    def command_exists(self):
        '''Determine if a command exists'''
        # kommandot är self.command_split[0], ex 'cd'
        if not self.command_split[0] in self.valid_commands:  # kolla om kommandot finns i self.valid_commands
            raise CommandNotExistError("Command does not exist.")  # ge error ifall kommandot inte finns
    
    ### check if the amount of arguments provided matches the command ###
    def command_arg_count(self):
        '''Check if amount of arguments is correct'''
        self.arg_count = len(self.command_split) - 1  # räknar ut antal argument
        if self.arg_count not in self.valid_commands[self.command_split[0]][1]:  # matchar antal argument mot listan av korrekta antal argument
            if self.command_split[0] == "echo":  # om kommandot är 'echo' ge speciellt error meddelande
                raise ArgCountError("Invalid amount of arguments.\nRemember to include '>' when outputting to a file.\n\tExample: 'echo text > file.txt'")
            raise ArgCountError("Invalid amount of arguments.")

    ### check if the arguments provided are valid ###
    def command_valid_args(self):
        '''Check if the arguments provided are valid'''
        command = self.command_split[0]

        # om kommandot är 'echo' gör annorlunda
        if command == "echo":
            self.args[0] = self.command_split[1]  # sätt self.args[0] till råa datan i self.command_split
            if self.arg_count == 3:  # ex 'echo Hej > fil.txt'
                self.args[1] = self.command_split[2]  # sätt self.args[1] till råa datan i self.command_split
                if self.args[1] != ">":
                    raise CommandSyntaxError("Syntax error. Missing '>'.")
            return  # vi är klara avsluta funktionen
        
        # om kommandot är 'move', 'copy', 'xcopy', kolla bara om self.args[0] är en giltig sökväg
        if command == "move" or command == "copy" or command == "xcopy":  # ex 'move fil.txt mapp/fil.txt'
            if not os.path.exists(self.args[0]):
                raise PathNotExistError(f"Path '{self.args[0]}' does not exist.")
            return  # vi är klara avsluta funktionen

        # vi vill inte göra något med argumenten ifall kommandot är 'md' så vi avslutar tidigt
        if command == "md":
            return

        # om det inte är några undantag vill vi kolla att alla argument är giltiga sökvägar
        for arg in self.args:
            if not os.path.exists(arg):
                raise PathNotExistError(f"Path '{arg}' does not exist.")
            
            '''
            gammal kod

            if os.path.isabs(arg):
                if not os.path.exists(arg):
                    return False
            else:
                if not os.path.exists(commands.current_dir + "\\" + arg):
                    return False
            '''

    ### process the command input ###
    def process_input(self):
        '''Process and validate command + arguments'''
        
        # om användaren inte har skrivit något kommando avsluta funktionen
        if self.command_input.strip() == "":
            return False
        
        # splitta self.command_input till self.command_split
        self.command_split = self.command_input.split()

        # skapa en lista med alla argument
        # joina dom med current_dir och normalisera dom i processen
        self.args = [os.path.normpath(os.path.join(commands.current_dir, arg)) for arg in self.command_split]
        self.args.pop(0)  # ta bort [0] eftersom det är kommandot och vi vill bara ha argumenten

        # fånga errors vi tidigare kan ha slängt
        try:
            # validera kommandot genom dessa funktioner     
            self.command_exists()
            self.command_arg_count()
            self.command_valid_args()
        except (CommandNotExistError, ArgCountError, CommandSyntaxError, PathNotExistError) as error:
            print(f"{type(error).__name__}: {error}\n")  # printa felmeddelandet till terminalen
            return False
        except Exception as error:
            print(f"Unexpected error.\n{type(error).__name__}: {error}\n")  # ett oväntat fel
            return False
        
        return True  # allt bra :)

    ### finally call the command ###
    def call_command(self):
        '''Execute the command'''
        # try except för att fånga oväntade fel
        try:
            # kalla på funktionen som vi hämtar från dictionaryn via kommandot som key
            self.valid_commands[self.command_split[0]][0](self.args)
        except Exception as error:
            print(f"{type(error).__name__}: {error}\n")  # printa felmeddelandet till terminalen

        # sh_dir(self.args)
        # sh_cd(self.args)
        # sh_md(self.args)

### main function ###
def main():
    commands.current_dir = os.getcwd()  # hämta den aktiva arbetskatalogen
    while True:
        command_input = input(f"SH {commands.current_dir}> ")  # ta in input från användaren
        command = HandleCommand(command_input)  # skapa en instans av HandleAll
        if command.process_input():  # processera användarens input
            command.call_command()  # om allt är bra utför kommandot

main()
