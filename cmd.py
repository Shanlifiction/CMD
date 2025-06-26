import os

#global var tex current_dir
current_dir = "C:/"

#dics (giltiga commandon) key: CD & value: func ->
#dics
#dics

#class (error handle)
class HandleAll:
    def __init__(self, command):
        self.command_input = command
        self.command_split = []
        self.valid_commands = {
            "dir": [0, [0, 1]],    #0=func soon (utan parantes)
            "cd": [1, [1]],
            "cd..": [2, [0]],
            "cd/": [3, [0]],
            "md": [4, [i for i in range(1, 69)]],
            "rd": [5, [i for i in range(1, 69)]],
            "erase": [6, [i for i in range(1, 69)]], #same
            "del": [6, [i for i in range(1, 69)]],   #same
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
            "q": [13, [0]], #same
            "sigma": [14, [0]]
        }

    def command_exists(self):
        if self.command_split[0] in self.valid_commands:
            return True
        return False
    
    def command_valid_syntax(self):
        # antal args korrekt
        # räkna ut antal argument
        # self.command_split = ["cd", "Desktop"]  ->  1  (2 - 1)
        self.args = len(self.command_split) - 1
        if self.args not in self.valid_commands[self.command_split[0]][1]:
            return False
        return True

    def command_valid_args(self):
        return True

    def process_input(self):
        # '   '
        # ''
        # 'cd C:\'  ->  ["cd", "C:\"]
        if self.command_input.strip() == "":
            print("Please enter valid command.")
            return False
        
        # split command into list, where [0] is command 
        self.command_split = self.command_input.split()
        
        if not self.command_exists():
            print("Command does not exist.")
            return False
        
        if not self.command_valid_syntax():
            print("Invalid syntax.")
            return False
        
        if not self.command_valid_args():
            print("Invalid arguments.")
            return False
        
        print("Success:", self.command_input, " -> ", self.command_split)
        return True

    def call_command(self):
        ...
        #try/except
        #OBS    
        #valid path     #tex "move" finns commandot? & "fil.txt" "mapp/fil.txt" finns dessa två argument?
                                                                                #fungerar dom tillsammans?

def main():
    while True:
        command_input = (input(f"{current_dir}>")) #det är en string
        command1 = HandleAll(command_input)
        if command1.process_input():
            command1.call_command()

        #current_dir = "" #platsposition

main()
