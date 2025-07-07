""" PYTHON CMD PROJECT """

### import modules ###
import os #för att kunna checka path:en (används normpath (förstår tex "../"), join & exist) 
import commands #importera vår egen modul
from commands import * #importera allt innehåll i separat fil

#global var
#current_dir = "" #platsposition #flyttad till commands filen

#dics (giltiga commandon) key "cd": value "func ->"

### class (specific error handle), inherits from Exception ###
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
        self.command_input = command #användarens inmatning
        self.command_split = [] #self.sommand_input.split() #index [0] är commandot 
        self.valid_commands = { #bibliotek som innehåller alla giltiga commands respektive funktioner
            #"kommando": [sh_funktion, [antal giltiga element, ...]]
            "sigma": [sh_dir, [1]],    #sh_dir
            "dir": [sh_dir, [0, 1]],   #sh_dir
            "cd": [sh_cd, [1]],
            "cd..": [sh_cddotdot, [0]],
            "cd/": [sh_cdslash,[0]],
            "md": [sh_md, [i for i in range(1, 69)]],
            "rd": [sh_rd, [i for i in range(1, 69)]],
            "erase": [sh_remove, [i for i in range(1, 69)]],    #sh_remove
            "del": [sh_remove, [i for i in range(1, 69)]],      #sh_remove
            "remove": [sh_remove, [i for i in range(1, 69)]],   #sh_remove
            "rename": [sh_rename, [2]],
            "xcopy": [sh_xcopy, [2]],
            "copy": [sh_copy, [2]],
            "move": [sh_move, [2]],
            "echo": [sh_echo, [1, 3]],
            "type": [sh_type,[1]],
            "cls": [sh_cls, [0]],   #sh_cls
            "clear": [sh_cls, [0]], #sh_cls
            "exit": [sh_exit, [0]], #sh_exit
            "quit": [sh_exit, [0]], #sh_exit
            "q": [sh_exit, [0]]     #sh_exit
        }

### check if command exists ###
    def command_exists(self):
        '''Determine if a command exists'''
        if not self.command_split[0] in self.valid_commands: #om commandot (self.command_split[0]) EJ finns i dicen (self.alid_commands)
            raise CommandNotExistError("Command does not exist.") #ge felmeddelande
            #return True
        #return False #annars avsluta och meddela 
    
### check if amount arguments provided is matches the command ### 
    def command_arg_count(self):
        '''Check if amount of arguments is correct'''
        self.arg_count = len(self.command_split) - 1 #antal argument genom att kolla längden på listan och ta bort första
        if self.arg_count not in self.valid_commands[self.command_split[0]][1]: #[0] är första index i användarens command input 
                                                                #[1] är lista-i-lista index (på antal tillåtna args ihop med command) i dicen
            if self.command_split[0] == "echo": #om command "echo"
                raise ArgCountError("\tRemember to type '>'. \n\t\tExample: 'echo text > file.txt'") #ge speciellt felmeddelande
            raise ArgCountError("Incorrect argument count.")
            #return False
        #return True
    #antal argument är korrekt (cls är "solo", medan mkdir "skapar" (kan gå ihop med fler)
    
### check if argument(s) is valid to the command(s) in the system ###
    def command_valid_args(self):
        '''Check if the arguments provided are valid'''
        #self.args = [os.path.normpath(os.path.join(commands.current_dir, arg)) for arg in self.command_split] #listcomprehension (med aboslut sökväg) ist för for-loop:en (nedan)
            # args = [] #skapa lista med argument
            # for arg in self.command_split:
            #     args.append(arg) #arg (från command_split) läggs till i args-listan
        #self.args.pop(0) #"poppar ut" första index-platsen (alltså command-elementet) i listan
        command = self.command_split[0] #sparar command-elementet i ny variabel

        #om command är echo gör annorlunda
        if command == "echo":
            self.args[0] = self.command_split[1] #raw data i listan (med commando först)
            if self.arg_count == 3: #om det är 3 element
                self.args[1] = self.command_split[2] # ">" andra index i raw data list
                if self.args[1] != ">": #för att nå symbolen
                    raise CommandSyntaxError("Syntax error. Missing '>'.")
                    #return False
                #if not os.path.exists(self.args[2]): #checkar att path:en finns #noneed
                    #return False
            return 
        
        #om command är move/xcopy/copy kontrollera sökvägen
        if command == "move" or command == "xcopy" or command == "copy":
            if not os.path.exists(self.args[0]): #checkar att path finns
                return PathNotExistError(f"Path {self.args[0]} does not exist.")
                #return False
            return
        
        #om md så ignorera att validera kommando
        if command == "md": 
            return 

        #om ingen av ovanstående undantag så kontrollera att args är giltiga sökvägar/destination/mapp/fil
        for arg in self.args:
            #if os.path.isabs(arg): #kollar om arg Är absolut
            if not os.path.exists(arg): #om path:en ej FINNS SÅ return true/false
                raise PathNotExistError(f"Path '{arg}' does not exist.")
                #return False
            """
            #else: #ifall arg ej är absolut, men finns sökväg?
                #os.path.isabs(current_dir + "/" + arg) 
                #if not os.path.exists(commands.current_dir + "/" + arg):
                    #return False
            """
        #return True #nonneed eftersom programmet endast ska returna en error om något ej stämmer 
    #argument (tex mappen) existerar osv
    #innehållet i commandot stämmer? Tex path/destination

### process command input ###
    def process_input(self):
        ''' Process and validate command + arguments '''
        #'     '
        #''
        #'cd C:\' -> ["cd", "C:\"]
        if self.command_input.strip() == "": #kollar om command har innehåll och tar bort ev mellanslag
            #print("Please enter command.") #borttagen pga användaren ska återkomma till programmet dirr
            return False
        
        """ Split command into a list """
        self.command_split = self.command_input.split()

        """ Pop out first index to create args list """
        self.args = [os.path.normpath(os.path.join(commands.current_dir, arg)) for arg in self.command_split] #normalisera/joina path:en och skapa args-lista
        self.args.pop(0) #ta bort första elementet i listan så den endast innehåller arguments

    #try/except sektion följer:
        try:
            #validera commmand genom dessa funktioner
            self.command_exists()
            self.command_arg_count()
            self.command_valid_args()
        except (CommandNotExistError, ArgCountError, CommandSyntaxError, PathNotExistError) as error: #"error" för att nå innehållet i meddelandet inom funktionerna ovan
            print(f"{type(error).__name__}: {error}\n") #printa felmeddelandet med specifik information om error
            return False
        except Exception as error:
            print(f"Unexpected error. \n{type(error).__name__}: {error}\n") #oväntat fel (kan vara externt problem)
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
    
### finally call and execute the command ###
    def call_command(self): #utför commandot (efter command är validerat)
        '''Excute the command'''
        try:
            self.valid_commands[self.command_split[0]][0](self.args) #från [dic]+[list][0]+[0](self.args) funktionen 
                                                                #första [0] är argument i lista med split-funktionen
                                                                #andra [0] är funktionen till det kommandot (se vår CMD modulen)
                                                                #self.args i parantensen är arg split-funktion utan command input
        except Exception as error:
            print(f"{type(error).__name__}: {error}\n")

            #sh_dir()
            #sh_dir(self.args)

        #alternativ:
        #sh_dir(path=self.args[0], x="", y="") #kwargs
        #sh_dir(self.args[0], "", "") #args


        #try/except ✔️
        #OBS ✔️
        #valid path ✔️

### main function containing while True-loop ###
def main():
    commands.current_dir = os.getcwd() #hämta den aktiva arbetskatalogen (alltså, där man står i det läget)
    while True:
        command_input = (input(f"SH {commands.current_dir}> ")) #det är en string
        command = HandleCommand(command_input) #skapar objekt/instans i klass HandleCommand (som egentligen kan vara en variabel i loopen)
        if command.process_input() == True: #genom en process valideras commandet #skulle kunna vara try/except i process_input()
            command.call_command() #gör jobbet (också genom en if-sats-process)

main()