
#global var tex current_dir
#global var
#global var
current_dir = ""

#dics (giltiga commandon) key: CD & value: func ->
#dics
#dics

#class (error handle)
class HandleAll:
    def __init__(self, command):
        self.command_input = command
        self.command_split = []
        self.valid_commands = {
            "dir": 0,    #0=func soon (utan parantes)
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
        if self.command_split[0] in self.valid_commands:
            return True
        return False
    
    def command_valid_syntax(self):
        return True

    def process_input(self):
        # '   '
        # ''
        # 'cd C:\'  ->  ["cd", "C:\"]
        if self.command_input.strip() == "":
            print("Please enter valid command.")
            return
        
        # split command into list, where [0] is command 
        self.command_split = self.command_input.split()
        
        if not self.command_exists():
            print("Command does not exist.")
            return
        
        if not self.command_valid_syntax():
            print("Invalid syntax.")
            return
        
        print(self.command_input, " -> ", self.command_split)



        #try/except
        #OBS    
        #valid path     #tex "move" finns commandot? & "fil.txt" "mapp/fil.txt" finns dessa två argument?
                                                                                #fungerar dom tillsammans?

def main():
    while True:
        command_input = (input(f"{current_dir}>")) #det är en string
        command1 = HandleAll(command_input)
        command1.process_input()


        #current_dir = "" #platsposition

main()
