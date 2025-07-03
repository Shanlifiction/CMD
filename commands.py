import os

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
    ...

def sh_cdslash(arguments):
    ...

def sh_md(arguments):
    ...

def sh_rd(arguments):
    ...

def sh_remove(arguments):
    ...

def sh_rename(arguments):
    ...

def sh_xcopy(arguments):
    ...

def sh_copy(arguments):
    ...

def sh_move(arguments):
    ...

def sh_echo(arguments):
    ...

def sh_cls(arguments):
    ...

def sh_exit(arguments):
    ...
