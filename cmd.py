
import os #för att kunna checka path:en
            #förstår tex "../"
import commands #importera modul
from commands import * #importera allt innehåll i separat fil

#global var
#current_dir = "" #platsposition #flyttad till commands filen

#dics (giltiga commandon) key "cd": value "func ->"

#class (specific error handle)
class CommandNotExistError(Exception):
    pass

class ArgCountError(Exception):
    pass

class CommandSyntaxError(Exception):
    pass

class PathNotExistError(Exception):
    pass

#class (error handle)
class HandleCommand:
    def __init__(self, command):
        self.command_input = command
        self.command_split = [] #index [0] är commandot
        self.valid_commands = {
            "dir": [sh_dir, [0, 1]],    #0=func soon (utan parantes på slutet av funtionen)
            "cd": [sh_cd, [1]],
            "cd..": [sh_cddotdot, [0]],
            "cd/": [sh_cdslash,[0]],
            "md": [sh_md, [i for i in range(1, 69)]],
            "rd": [sh_rd, [i for i in range(1, 69)]],
            "erase": [sh_remove, [i for i in range(1, 69)]], #same
            "del": [sh_remove, [i for i in range(1, 69)]], #same
            "remove": [sh_remove, [i for i in range(1, 69)]], #same
            "rename": [sh_rename, [2]],
            "xcopy": [sh_xcopy, [2]],
            "copy": [sh_copy, [2]],
            "move": [sh_move, [2]],
            "echo": [sh_echo, [1, 3]],
            "type": [sh_type,[1]],
            "cls": [sh_cls, [0]],  #same
            "clear": [sh_cls, [0]], #same
            "exit": [sh_exit, [0]], #same
            "quit": [sh_exit, [0]], #same
            "q": [sh_exit, [0]] #same
        }

    def command_exists(self):
        if not self.command_split[0] in self.valid_commands: #finns command i dicen?
            raise CommandNotExistError("Command does not exist.")
            #return True
        #return False #annars avsluta och meddela 
    
    def command_arg_count(self):
        self.arg_count = len(self.command_split) - 1 #antal argument genom att kolla längden på listan och ta bort första
        if self.arg_count not in self.valid_commands[self.command_split[0]][1]: #[0] är första index i användarens command input 
                                                                #[1] är lista-i-lista index (på antal tillåtna args ihop med command) i dicen
            if self.command_split[0] == "echo":
                raise ArgCountError("\tRemember to type '>'. \n\tExample: 'echo text > file.txt'")
            raise ArgCountError("Incorrect argument count.")
            #return False
        #return True
    #antal argument är korrekt (cls är "solo", medan mkdir "skapar" (kan gå ihop med fler)
    
    def command_valid_args(self):
        #self.args = [os.path.normpath(os.path.join(commands.current_dir, arg)) for arg in self.command_split] #listcomprehension (med aboslut sökväg) ist för for-loop:en (nedan)
            # args = [] #skapa lista med argument
            # for arg in self.command_split:
            #     args.append(arg) #arg (från command_split) läggs till i args-listan
        #self.args.pop(0) #"poppar ut" första index-platsen (alltså command-elementet) i listan
        command = self.command_split[0] #sparar command-elementer i ny variabel

        if command == "echo":
            self.args[0] = self.command_split[1] #raw data i listan (med commando först)
            if self.arg_count == 3: #om det är 3 element
                self.args[1] = self.command_split[2] #är > andra index i raw list
                if self.args[1] != ">": #för att nå symbolen
                    raise CommandSyntaxError("Syntax error. Missing '>'.")
                    #return False
                #if not os.path.exists(self.args[2]): #checkar att path:en finns #noneed
                    #return False
            return 
        
        if command == "move" or command == "xcopy" or command == "copy":
            if not os.path.exists(self.args[0]): #checkar att path finns
                return PathNotExistError(f"Path {self.args[0]} does not exist.")
                #return False
            return
        
        if command == "md": #om md så ignorera att kolla kommando
            return 

        for arg in self.args:
            #if os.path.isabs(arg): #kollar om arg Är absolut
            if not os.path.exists(arg): #om path:en ej FINNS SÅ return true/false
                raise PathNotExistError(f"Path '{arg}' does not exist.")
                #return False
            #else: #ifall arg ej är absolut, men finns sökväg?
                #os.path.isabs(current_dir + "/" + arg) 
                #if not os.path.exists(commands.current_dir + "/" + arg):
                    #return False
        #return True #nonneed eftersom programmet endast ska returna en error om något ej stämmer 
    #argument (tex mappen) existerar osv
    #innehållet i commandot stämmer? Tex path/destination

    def process_input(self):
        #'     '
        #''
        #'cd C:\' -> ["cd", "C:\"]
        if self.command_input.strip() == "": #kollar om command har innehåll och tar bort ev mellanslag
            #print("Please enter command.") #borttagen pga användaren ska återkomma till programmet dirr
            return False
        
        """ Split command into a list """
        self.command_split = self.command_input.split()

        """ Pop out first index to create args list """
        self.args = [os.path.normpath(os.path.join(commands.current_dir, arg)) for arg in self.command_split] #normalisera/joina path:en
        self.args.pop(0)

    #Try/except sektion följer:
        try:
            self.command_exists()
            self.command_arg_count()
            self.command_valid_args()
        except (CommandNotExistError, ArgCountError, CommandSyntaxError, PathNotExistError) as error: #"error" för att nå innehållet i meddelandet inom funktionerna i command_valid_args ovan
            print(error)
            return False
        except Exception as error:
            print(f"Unexpected error. {error}")
            return False

        """
        if not self.command_exists(): #if-sats som kollar om commandot tex "move" EJ finns
            print("Command does not exist.")
            return False

        if not self.command_arg_count(): #tex "move" "fil.txt" -> "mapp/fil.txt" finns alla dessa argument och fungerar dom tillsammans?
            print("Invalid syntax.")
            return False
        
        if not self.command_valid_args(): #tex finns mappen som ska flyttas etc (?)
            print("Invalid arguments.")
            return False

        """
        
        print(self.command_input, " -> ", self.command_split) #test-print:en
        return True  #annars avsluta och meddela 

    def call_command(self): #utför commandot (efter command är validerat)
        try:
            self.valid_commands[self.command_split[0]][0](self.args) #från [dic]+[list][0]+[0](self.args) funktionen 
                                                                #första [0] är argument i lista med split-funktionen
                                                                #andra [0] är funktionen till det kommandot
                                                                #self.args i parantensen är arg split-funktion utan command input
        except Exception as error:
            print(error)

            #sh_dir()
            #sh_dir(self.args)

        #alternativ:
        #sh_dir(path=self.args[0], x="", y="") #kwargs
        #sh_dir(self.args[0], "", "") #args



        #try/except ✔️
        #OBS ✔️
        #valid path ✔️


def main():
    commands.current_dir = os.getcwd()
    while True:
        command_input = (input(f"SH {commands.current_dir}> ")) #det är en string
        command = HandleCommand(command_input) #skapar objekt/instans i klass HandleCommand (som egentligen kan vara en variabel i loopen)
        if command.process_input() == True: #genom en process validerar commandet #skulle kunna vara try/except i process_input()
            command.call_command() #gör jobbet (också genom en if-sats-process)

main()




