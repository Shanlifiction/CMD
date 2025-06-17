#alla command funcs

#when command_validity_passed ->
def _move(source, destination): #parametrar kan också va skrivet med *arg
    print("move funtion", source, destination) #args[0], args[1] (args bra att användas till commands som kan skrivas på flera sätt)
                                                                            #och i relation till andra argument tex ">"

#dic /class #valid_commands["echo"]("text", ">", "fil.txt")     #**kwargs finnd också!
#           #call_command("echo", args)                         #valid_commands["echo"](abc="text", symbol=">", destination="fil.txt")                                    
