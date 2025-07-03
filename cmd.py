
import os #för att kunna checka path:en
            #förstår tex "../"
import commands #importera modul
from commands import * #importera allt innehåll i separat fil

#global var
#current_dir = "" #platsposition #flyttad till commands filen

#dics (giltiga commandon) key "cd": value "func ->"

#class (error handle)
class HandleAll:
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
            "cls": [sh_cls, [0]],  #same
            "clear": [sh_cls, [0]], #same
            "exit": [sh_exit, [0]], #same
            "quit": [sh_exit, [0]], #same
            "q": [sh_exit, [0]] #same
        }

    def command_exists(self):
        if self.command_split[0] in self.valid_commands: #finns command i dicen?
            return True
        return False #annars avsluta och meddela 
    
    def command_arg_count(self):
        self.arg_count = len(self.command_split) - 1 #antal argument genom att kolla längden på listan och ta bort första
        if self.arg_count not in self.valid_commands[self.command_split[0]][1]: #[0] är första index i användarens command input 
                                                                #[1] är lista-i-lista index (på antal tillåtna args ihop med command) i dicen
            return False
        return True
    #antal argument är korrekt (cls är "solo", medan mkdir "skapar" (kan gå ihop med fler)
    
    def command_valid_args(self):
        self.args = [arg for arg in self.command_split] #listcomprehension ist för for-loop:en (nedan)
        # args = [] #skapa lista med argument
        # for arg in self.command_split:
        #     args.append(arg) #arg (från command_split) läggs till i args-listan
        command = self.args.pop(0) #pop "poppar ut" arg på första index-plats OCH sparar den i ny variabel

        if command == "echo":
            if self.arg_count == 3: 
                if self.args[1] != ">": #för att nå symbolen
                    return False
                if not os.path.exists(self.args[2]): #checkar att path:en finns
                    return False
            return True
        
        if command == "move" or command == "xcopy" or command == "copy":
            if not os.path.exists(arg[0]): #checkar att path
                return False
            return True

        for arg in self.args:
            if os.path.isabs(arg): #kollar om arg Är absolut
            #if arg in os.path.exists(arg): #"arg in" no need
                if not os.path.exists(arg): #om path:en ej FINNS SÅ return true/false
                    return False
            else: #ifall arg ej är absolut, men finns sökväg?
                #os.path.isabs(current_dir + "/" + arg) 
                if not os.path.exists(commands.current_dir + "/" + arg):
                    return False

        return True
    #argument (tex mappen) existerar osv
    #innehållet i commandot stämmer? Tex path/destination

    def process_input(self):
        #'     '
        #''
        #'cd C:\' -> ["cd", "C:\"]
        if self.command_input.strip() == "": #kollar om command har innehåll och tar bort ev mellanslag
            #print("Please enter command.") #borttagen pga användaren ska återkomma till programmet dirr
            return False
        
        #split command into a list
        self.command_split = self.command_input.split() 

    #nedan kan skrivas om till try/except
        if not self.command_exists(): #if-sats som kollar om commandot tex "move" EJ finns
            print("Command does not exist.")
            return False

        if not self.command_arg_count(): #tex "move" "fil.txt" -> "mapp/fil.txt" finns alla dessa argument och fungerar dom tillsammans?
            print("Invalid syntax.")
            return False
        
        if not self.command_valid_args(): #tex finns mappen som ska flyttas etc (?)
            print("Invalid arguments.")
            return False
        
        print(self.command_input, " -> ", self.command_split)
        return True  #annars avsluta och meddela 

    def call_command(self): #utför commandot (efter command är validerat)
        ...
        self.valid_commands[self.command_split[0]][0](self.args) #från [dic]+[list][0]+[0](self.args) funktionen 
                                                                #första [0] är argument i lista med split-funktionen
                                                                #andra [0] är funktionen till det kommandot
                                                                #self.args i parantensen är arg split-funktion utan command input
        #sh_dir()
        #sh_dir(self.args)
        #sh_dir(path=self.args[0], x="", y="")
        #sh_dir(self.args[0], "", "")


        #try/except
        #OBS
        #valid path

def main():
    commands.current_dir = os.getcwd()
    while True:
        command_input = (input(f"SH {commands.current_dir}> ")) #det är en string
        command1 = HandleAll(command_input) #skapar objekt/instans i klass HandleAll
        if command1.process_input() == True: #genom en process validerar commandet #skulle kunna vara try/except i process_input()
            command1.call_command() #gör jobbet (också genom en if-sats-process)


    
main()
#ska vi göra en cmd log?




