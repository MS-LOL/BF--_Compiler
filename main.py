print(r""" _______  ________                         ______                                 __ __                   
|       \|        \   __       __         /      \                               |  \  \                  
| ▓▓▓▓▓▓▓\ ▓▓▓▓▓▓▓▓  |  \     |  \       |  ▓▓▓▓▓▓\ ______  ______ ____   ______  \▓▓ ▓▓ ______   ______  
| ▓▓__/ ▓▓ ▓▓__    __| ▓▓__ __| ▓▓__     | ▓▓   \▓▓/      \|      \    \ /      \|  \ ▓▓/      \ /      \ 
| ▓▓    ▓▓ ▓▓  \  |    ▓▓  \    ▓▓  \    | ▓▓     |  ▓▓▓▓▓▓\ ▓▓▓▓▓▓\▓▓▓▓\  ▓▓▓▓▓▓\ ▓▓ ▓▓  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\
| ▓▓▓▓▓▓▓\ ▓▓▓▓▓   \▓▓▓▓▓▓▓▓\▓▓▓▓▓▓▓▓    | ▓▓   __| ▓▓  | ▓▓ ▓▓ | ▓▓ | ▓▓ ▓▓  | ▓▓ ▓▓ ▓▓ ▓▓    ▓▓ ▓▓   \▓▓
| ▓▓__/ ▓▓ ▓▓        | ▓▓     | ▓▓       | ▓▓__/  \ ▓▓__/ ▓▓ ▓▓ | ▓▓ | ▓▓ ▓▓__/ ▓▓ ▓▓ ▓▓ ▓▓▓▓▓▓▓▓ ▓▓      
| ▓▓    ▓▓ ▓▓         \▓▓      \▓▓        \▓▓    ▓▓\▓▓    ▓▓ ▓▓ | ▓▓ | ▓▓ ▓▓    ▓▓ ▓▓ ▓▓\▓▓     \ ▓▓      
 \▓▓▓▓▓▓▓ \▓▓                              \▓▓▓▓▓▓  \▓▓▓▓▓▓ \▓▓  \▓▓  \▓▓ ▓▓▓▓▓▓▓ \▓▓\▓▓ \▓▓▓▓▓▓▓\▓▓      
                                                                        | ▓▓                              
                                                                        | ▓▓                              
                                                                         \▓▓                              
""")

print("Input the Filename with the extension that you wish to convert to BrainFuck")
InputFileName = input(":>")
print("Input the Filename that you wish to save the code as. It will automatically have the .bf file extension.")
OutputFileName = input(":>")
ValidInput = bool(False)
SeeOutputBoolean = bool()
while ValidInput != True:
    print("Do you wish to see the outputted code in this program? Y/n")
    SeeOutput = input(":>")
    if SeeOutput == "Y" or SeeOutput == "y":
        SeeOutputBoolean = True
        ValidInput = True
    elif SeeOutput == "N" or SeeOutput == "n":
        SeeOutputBoolean = False
        ValidInput = True
    else:
        print("Invalid input, try again.")
OutputFileName = OutputFileName + ".bf"
InputFile = open(InputFileName, "r")
OutputFile = open(OutputFileName, "x")
OutputFileCache = ""
LineNumber = int(1)

"""
I plan on putting a section here that copies snippets/labels into the code.

This is so that the same code can be referenced in multiple places in the program.

Kinda like a function except you can't do branch instructions.

You can call snippets within snippets.

I guess keyword is label(Init), endlabel and copylabel(Init)

WARNING! DO NOT RECURSIVELY CALL SNIPPETS(MAKE 2 OR MORE SNIPPETS REFERENCE EACH OTHER OR MAKE 1 SNIPPET REFERENCE ITSELF)! BRAINFUCK++ AND BRAINFUCK DOES NOT SUPPORT BRANCH INSTRUCTIONS! THE COMPILER WILL GET STUCK!
"""

for line in InputFile:
    line = line.strip() # Remove leading/trailing whitespace
    
    if line.startswith("//"):
        continue
    elif line.startswith("dpinc"):
        OpenBracket = line.index("(")
        CloseBracket = line.index(")")
        Number = int(line[OpenBracket + 1:CloseBracket])
        OutputFileCache += ">" * Number
        
    elif line.startswith("dpdec"):
        OpenBracket = line.index("(")
        CloseBracket = line.index(")")
        Number = int(line[OpenBracket + 1:CloseBracket])
        OutputFileCache += "<" * Number
        
    elif line.startswith("inc") and line.startswith("dpinc") == False:
        OpenBracket = line.index("(")
        CloseBracket = line.index(")")
        Number = int(line[OpenBracket + 1:CloseBracket])  # Extract number
        OutputFileCache += "+" * Number  # Repeat '+' number times)
        
    elif line.startswith("dec") and line.startswith("dpdec") == False:
        OpenBracket = line.index("(")
        CloseBracket = line.index(")")
        Number = int(line[OpenBracket + 1:CloseBracket])
        OutputFileCache += "-" * Number
        
    elif line.startswith("input"):
        OutputFileCache += ","
        
    elif line.startswith("output"):
        OutputFileCache += "."
        
    elif line.startswith("loop") and line.startswith("endloop") == False:
        OutputFileCache += "["
        
    elif line.startswith("endloop"):
        OutputFileCache += "]"
    elif line == "":
        # The line is empty, no reason to stay here.
        # Really, nothing to do.
        # Please just look away.
        continue
    else:
        # The code is fucked somehow.
        # Prints an error code, line number, and the line then exit the program.
        print("Fatal SyntaxError at line ", LineNumber, " in file ", InputFileName)
        print(line)
        input("Press enter to close program")
        exit
    LineNumber += 1


OutputFile.write(OutputFileCache)
OutputFile.close()
if SeeOutputBoolean == True:
    print(OutputFileCache)