
#global var tex current_dir
#global var
#global var
current_dir = ""

#dics (giltiga commandon) key: CD & value: func ->
#dics
#dics

#class (error handle)
class HandleAll:
    def __init__(self):
        self.command_input = ""
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

    def process_input():
        ...
        #try/except
        #OBS    
        #valid path     #tex "move" finns commandot? & "fil.txt" "mapp/fil.txt" finns dessa två argument?
                                                                                #fungerar dom tillsammans?

def main():
    while True:
        command_input = (input(f"{current_dir}>")) #det är en string
    #current_dir = "" #platsposition

main()





