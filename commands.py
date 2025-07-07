import os
import shutil

current_dir = ""

def sh_dir(arguments):
    path = current_dir
    if len(arguments) != 0:
        path = arguments[0]
    for element in os.listdir(path):
        print(element)

def sh_cd(arguments):
    global current_dir
    current_dir = arguments[0]
    
    '''
    gammal kod

    if os.path.isabs(arguments[0]):
        current_dir = arguments[0]
    else:
        # current_dir += "\\" + arguments[0]
        abs_path = os.path.join(current_dir, arguments[0])
        # print("bf", abs_path)
        abs_path = os.path.normpath(abs_path)
        # print("gf", abs_path)
        current_dir = abs_path
    '''

def sh_cddotdot(arguments):
    global current_dir
    current_dir = os.path.normpath(os.path.join(current_dir, ".."))

def sh_cdslash(arguments):
    global current_dir
    if os.name == "nt":  # windows
        current_dir = os.path.normpath("C:\\")
    if os.name == "posix":  # mac / linux
        current_dir = os.path.normpath("/Users")

def sh_md(arguments):
    for arg in arguments:
        os.mkdir(arg)

def sh_rd(arguments):
    for arg in arguments:
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
    if os.name == "nt":
        os.system("cls")
    if os.name == "posix":
        os.system("clear")

def sh_exit(arguments):
    exit(0)
