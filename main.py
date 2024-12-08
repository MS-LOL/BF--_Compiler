print(r""" _______  ________                     ______                                 __ __                   
|       \|        \                   /      \                               |  \  \                  
| ▓▓▓▓▓▓▓\ ▓▓▓▓▓▓▓▓                  |  ▓▓▓▓▓▓\ ______  ______ ____   ______  \▓▓ ▓▓ ______   ______  
| ▓▓__/ ▓▓ ▓▓__    ______ ______     | ▓▓   \▓▓/      \|      \    \ /      \|  \ ▓▓/      \ /      \ 
| ▓▓    ▓▓ ▓▓  \  |      \      \    | ▓▓     |  ▓▓▓▓▓▓\ ▓▓▓▓▓▓\▓▓▓▓\  ▓▓▓▓▓▓\ ▓▓ ▓▓  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\
| ▓▓▓▓▓▓▓\ ▓▓▓▓▓   \▓▓▓▓▓▓\▓▓▓▓▓▓    | ▓▓   __| ▓▓  | ▓▓ ▓▓ | ▓▓ | ▓▓ ▓▓  | ▓▓ ▓▓ ▓▓ ▓▓    ▓▓ ▓▓   \▓▓
| ▓▓__/ ▓▓ ▓▓                        | ▓▓__/  \ ▓▓__/ ▓▓ ▓▓ | ▓▓ | ▓▓ ▓▓__/ ▓▓ ▓▓ ▓▓ ▓▓▓▓▓▓▓▓ ▓▓      
| ▓▓    ▓▓ ▓▓                         \▓▓    ▓▓\▓▓    ▓▓ ▓▓ | ▓▓ | ▓▓ ▓▓    ▓▓ ▓▓ ▓▓\▓▓     \ ▓▓      
 \▓▓▓▓▓▓▓ \▓▓                          \▓▓▓▓▓▓  \▓▓▓▓▓▓ \▓▓  \▓▓  \▓▓ ▓▓▓▓▓▓▓ \▓▓\▓▓ \▓▓▓▓▓▓▓\▓▓      
                                                                    | ▓▓                              
                                                                    | ▓▓                              
                                                                     \▓▓                              
""")

# To whoever decided to look at this code, I sincerely apologise for what you are about to see.


# Output Filename
print("Input the Filename with the extension that you wish to convert to BrainFuck")
InputFileName = input(":>")

# Input Filename
print("Input the Filename that you wish to save the code as. It will automatically have the .bf file extension.")
OutputFileName = input(":>")

# Check whether to print output to console
ValidInput = bool(False)
SeeOutputBoolean = bool()
while ValidInput != True:
    print("Do you wish to see the outputted code in this program? Y/n")
    UserInput = input(":>")
    if UserInput == "Y" or UserInput == "y":
        SeeOutputBoolean = True
        ValidInput = True
    elif UserInput == "N" or UserInput == "n":
        SeeOutputBoolean = False
        ValidInput = True
    else:
        print("Invalid input, try again.")

# Initialise the files
OutputFileName = OutputFileName + ".bf"
InputFile = open(InputFileName, "r")


# Prepare a string to print to and read from
InputFileCacheTemp = InputFile.read()
InputFileCache = InputFileCacheTemp
InputFile.close()
InputFile2 = open(InputFileName, "r")
OutputFileCache = ""
LinkedFileCache = """"""
# Close a file and open a new instance of it. I really hate myself for doing this.

# Prepare a Dictionary for the labels I guess
Labels = {}

# Declare a LineNumber variable which starts at 1
LineNumber = int(1)

"""
I plan on putting a section here that copies snippets/labels into the code.

This is so that the same code can be referenced in multiple places in the program.

Kinda like a function except you can't do branch instructions.

You can call snippets within snippets.

I guess keyword is label(Init), endlabel and copylabel(Init)

Do the labels actually get included in the program or are they removed from their original positon in the source code?

WARNING! DO NOT RECURSIVELY CALL SNIPPETS(MAKE 2 OR MORE SNIPPETS REFERENCE EACH OTHER OR MAKE 1 SNIPPET REFERENCE ITSELF)! BRAINFUCK-- AND BRAINFUCK DOES NOT SUPPORT BRANCH INSTRUCTIONS! THE COMPILER WILL GET STUCK!
"""

# Label handling code
for line in InputFile2:
    line = line.strip() # Remove leading/trailing whitespace

    if line.startswith("label"): # Next couple lines until corresponding "endlabel" are part of label
        # Get indexes of brackets in the line
        
        OpenBracket = line.index("(")
        CloseBracket = line.index(")")
        
        # Get the name inside the brackets as a string
        
        LabelName = str(line[OpenBracket + 1:CloseBracket])
        
        # Get the indexes of the label(labelnamehere) and endlabel keywords in the whole file
        
        StartLabelIndex = InputFileCache.find("label(" + LabelName + ")")
        EndLabelIndex = InputFileCache.find("endlabel", StartLabelIndex)
        LabelBody = InputFileCache[StartLabelIndex + len(line) + 1:EndLabelIndex - 1]
        Label = InputFileCache[StartLabelIndex:EndLabelIndex + InputFile.readline(LineNumber)]
        print(LabelBody)
        Labels[LabelName] = LabelBody
        if LabelName == "Main": #Main program, don't remove
            LinkedFileCache += LabelBody
            LinkedFileCache += "\n"


for line in LinkedFileCache:
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
        OutputFileCache += "+" * Number  # Repeat '+' number times
        
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
        # The code is somehow more broken than it already is.
        # Prints an error code, line number, and the line then exit the program.
        print("Fatal SyntaxError at line ", LineNumber, " in file ", InputFileName)
        print(line)
        input("Press enter to close program")
        exit
    LineNumber += 1

LinkedFile = open("Linked_" + InputFileName, "x")
OutputFile = open(OutputFileName, "x")

OutputFile.write(OutputFileCache)
OutputFile.close()
if SeeOutputBoolean == True:
    print(OutputFileCache)