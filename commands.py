import os

current_dir = ""

#alla command funcs

#when command_validity_passed ->
def _move(source, destination): #parametrar kan också va skrivet med *arg
    print("move function", source, destination) #args[0], args[1] (args bra att användas till commands som kan skrivas på flera sätt)
                                                                            #och i relation till andra argument tex ">"

#dic /class #valid_commands["echo"]("text", ">", "fil.txt")     #**kwargs finns också!
#           #call_command("echo", args)                         #valid_commands["echo"](abc="text", symbol=">", destination="fil.txt")                                    

def sh_dir(arguments):
    #{'path':'C, 'x':"", 'y':""}
    #['C:/', "", ""]
    path = current_dir
    if len(arguments) != 0:
        path = arguments[0]
    
    #print pathway content
    for element in os.listdir(path):
        print(element)




def sh_cd():
    ...