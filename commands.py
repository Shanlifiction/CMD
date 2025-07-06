import os
import shutil

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

def sh_cd(arguments):
    global current_dir
    current_dir = arguments[0]
"""
    if os.path.isabs(arguments[0]): #absolut väg
        current_dir = arguments[0] #absolut sökväg (args)ersätter
    else: #relativ 
       current_dir += "/" + arguments[0] #adderar
"""

def sh_cddotdot(arguments):
    global current_dir
    current_dir = os.path.normpath(os.path.join(current_dir, ".."))

def sh_cdslash(arguments):
    global current_dir
    current_dir = os.path.normpath("/Users")

def sh_md(arguments):
    global current_dir
    for arg in arguments:
        os.mkdir(arg)

def sh_rd(arguments):
    global current_dir
    for arg in arguments:
        #os.rmdir(arg)
        shutil.rmtree(arg)

def sh_remove(arguments):
    global current_dir
    for arg in arguments:
        os.remove(arg)

def sh_rename(arguments):
    os.rename(arguments[0], arguments[1]) #[0] första arg i self.args-listan osv

def sh_xcopy(arguments):
    shutil.copytree(arguments[0], arguments[1])

def sh_copy(arguments):
    shutil.copy(arguments[0], arguments[1])

def sh_move(arguments):
    shutil.move(arguments[0], arguments[1])

def sh_echo(arguments):
    if len(arguments) == 3:
        with open (arguments[2], "a") as file:
            file.write(arguments[0])
    else:
        #if arguments[1] != ">":
        print(arguments[0])

def sh_type(arguments):
    with open (arguments[0], "r") as file: #öppna filen
        content = file.read() #läs innehåll OCH skapa varibel
        print(content) #type ut innehåll

def sh_cls(arguments):
    os.system("clear")

def sh_exit(arguments):
    #os.system("exit")
    exit()