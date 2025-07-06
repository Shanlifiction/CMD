import os
import shutil

current_dir = ""

#alla command funcs

#when command_validity_passed ->
def _move(source, destination): #parametrar kan också va skrivet med *arg
    print("move funtion", source, destination) #args[0], args[1] (args bra att användas till commands som kan skrivas på flera sätt)
                                                                            #och i relation till andra argument tex ">"

#dic /class #valid_commands["echo"]("text", ">", "fil.txt")     #**kwargs finnd också!
#           #call_command("echo", args)                         #valid_commands["echo"](abc="text", symbol=">", destination="fil.txt")                                    


def sh_dir(arguments):
    # { 'path': 'C:/', 'x': 'abc', 'y': 'def' }
    # ['C:/', 'abc', 'def']
    path = current_dir
    if len(arguments) != 0:
        path = arguments[0]
    # print path content
    for element in os.listdir(path):
        print(element)

def sh_cd(arguments):
    global current_dir
    current_dir = arguments[0]
    
    '''if os.path.isabs(arguments[0]):
        current_dir = arguments[0]
    else:
        # current_dir += "\\" + arguments[0]
        abs_path = os.path.join(current_dir, arguments[0])
        # print("bf", abs_path)
        abs_path = os.path.normpath(abs_path)
        # print("gf", abs_path)
        current_dir = abs_path'''

def sh_cddotdot(arguments):
    global current_dir
    current_dir = os.path.normpath(os.path.join(current_dir, ".."))

def sh_cdslash(arguments):
    global current_dir
    current_dir = os.path.normpath("C:\\")
    # current_dir = os.path.normpath("~")

def sh_md(arguments):
    for arg in arguments:
        os.mkdir(arg)

def sh_rd(arguments):
    for arg in arguments:
        # os.rmdir(arg)
        shutil.rmtree(arg)

def sh_remove(arguments):
    for arg in arguments:
        os.remove(arg)
    
def sh_rename(arguments):
    os.rename(arguments[0], arguments[1])

def sh_xcopy(arguments):
    shutil.copytree(arguments[0], arguments[1])

def sh_copy(arguments):
    shutil.copy(arguments[0], arguments[1])

def sh_move(arguments):
    shutil.move(arguments[0], arguments[1])

def sh_echo(arguments):
    if len(arguments) == 3:
        with open(arguments[2], "a") as file:
            file.write(arguments[0])
    else:
        print(arguments[0])

def sh_type(arguments):
    with open(arguments[0], "r") as file:
        content = file.read()
        print(content)

def sh_cls(arguments):
    os.system("cls")

def sh_exit(arguments):
    exit(0)
