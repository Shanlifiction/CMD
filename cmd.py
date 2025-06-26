
#global var
current_dir = "" #current_dir = "" #platsposition

#dics (giltiga commandon) key "cd": value "func ->"

#class (error handle)
class HandleAll:
    def __init__(self, command):
        self.command_input = command
        self.command_split = [] #index [0] är commandot
        self.valid_commands = {
            "dir": [0, [0, 1]],    #0=func soon (utan parantes på slutet av funtionen)
            "cd": [1, [1]],
            "cd..": [2, [0]],
            "cd/": [3,[0]],
            "md": [4, [i for i in range(1, 69)]],
            "rd": [5, [i for i in range(1, 69)]],
            "erase": [6, [i for i in range(1, 69)]], #same
            "del": [6, [i for i in range(1, 69)]], #same
            "remove": [6, [i for i in range(1, 69)]], #same
            "rename": [7, [2]],
            "xcopy": [8, [2]],
            "copy": [9, [2]],
            "move": [10, [2]],
            "echo": [11, [1, 3]],
            "cls": [12, [0]],  #same
            "clear": [12, [0]], #same
            "exit": [13, [0]], #same
            "quit": [13, [0]], #same
            "q": [13, [0]] #same
        }

    def command_exists(self):
        if self.command_split[0] in self.valid_commands: #finns command i dicen?
            return True
        return False #annars avsluta och meddela 
    
    def command_valid_syntax(self):
        self.args = len(self.command_split) - 1 #antal argument genom att kolla längden på listan
        if self.args not in self.valid_commands[self.command_split[0]][1]: #[0] är första index i användarens command input 
                                                                #[1] är andra index (lista på antal tillåtna args ihop med command) i dicen
            return False
        return True
    #antal argument är korrekt (cls är "solo", medan mkdir "skapar" (kan gå ihop med fler)
    
    def command_valid_argzzz(self):
        return True
    #argument (tex mappen) existerar osv
    #innehållet stämmer?
    #skrivet på korrekt sätt

    def process_input(self):
        #'     '
        #''
        #'cd C:\' -> ["cd", "C:\"]
        if self.command_input.strip() == "": #kollar om command har innehåll och tar bort ev mellanslag
            print("Please enter valid command.")
            return False
        
        #split command into a list
        self.command_split = self.command_input.split() 

        if not self.command_exists(): #if-sats som kollar om commandot tex "move" EJ finns
            print("Command does not exist.")
            return False

        if not self.command_valid_syntax(): #tex "move" "fil.txt" -> "mapp/fil.txt" finns alla dessa argument och fungerar dom tillsammans?
            print("Invalid syntax.")
            return False
        
        if not self.command_valid_argzzz(): #tex finns mappen som ska flyttas etc (?)
            print("Here we go again.")
            return False
        
        print(self.command_input, " -> ", self.command_split)
        return True  #annars avsluta och meddela 

    def call_command(self): #utför commandot (efter command är validerat)
        ...


        #try/except
        #OBS
        #valid path


def main():
    while True:
        command_input = (input(f"{current_dir}>")) #det är en string
        command1 = HandleAll(command_input) #skapar objekt/instans i klass HandleAll
        if command1.process_input() == True: #genom en process validerar commandet #skulle kunna vara try/except i process_input()
            command1.call_command() #gör jobbet (också genom en if-sats-process)


    
main()





