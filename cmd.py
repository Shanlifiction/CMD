
#global var
current_dir = "" #current_dir = "" #platsposition

#dics (giltiga commandon) key "cd": value "func ->"

#class (error handle)
class HandleAll:
    def __init__(self, command):
        self.command_input = command
        self.command_split = [] #index [0] är commandot
        self.valid_commands = {
            "dir": (0, (1, 2, 3)),    #0=func soon (utan parantes)
            "cd": 1,
            "cd..": 2,
            "cd/": 3,
            "md": 4,
            "rd": 5,
            "erase": 6, #same
            "del": 6,   #same
            "remove": 6, #same
            "rename": 7,
            "xcopy": 8,
            "copy": 9,
            "move": 10,
            "echo": 11,
            "cls": 12,  #same
            "clear": 12, #same
            "exit": 13, #same
            "quit": 13, #same
            "q": 13, #same
        }

    def command_exists(self):
        if self.command_split[0] in self.valid_commands: #finns command i dicen?
            return True
        return False #annars avsluta och meddela 
    
    def command_valid_syntax(self):
        return True
    #innehållet stämmer?
    #antal argument är korrekt (cd är "solo", medan mkdir "skapar" (kan gå ihop med fler)
    #skrivet på korrekt sätt
    
    def command_valid_argzzz(self):
        return True
    #argument (tex mappen) existerar osv


    def process_input(self):
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
        
        return True  #annars avsluta och meddela 

        print(self.command_input, " -> ", self.command_split)

    def call_command(self): #utför commandot (efter command är validerat)
        ...


        #try/except
        #OBS
        #valid path


def main():
    while True:
        command_input = (input(f"{current_dir}>")) #det är en string
        command1 = HandleAll(command_input) #skapar objekt/instans i klass HandleAll
        if command1.process_input() == True: #genom en process validerar commandet
            command1.call_command() #gör jobbet (också genom en if-sats-process)
            

    
main()





