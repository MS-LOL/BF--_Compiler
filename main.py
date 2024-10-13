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

print("Input the Filename with the extension that you wich to convert to BrainFuck")
InputFileName = input(":>")
print("Input the Filename that you wish to save as. It will automatically have the .bf file extension.")
OutputFileName = input(":>")

OutputFileName = OutputFileName + ".bf"

InputFile = open(InputFileName, "r")
OutputFile = open(OutputFileName, "x")
OutputFileCache = ""

for line in InputFile:
    line = line.strip() # Remove leading/trailing whitespace
    
    if line.startswith("//"):
        continue
    elif line.startswith("dpinc"):
        OpenBracket = line.index("(")
        CloseBracket = line.index(")")
        number = int(line[OpenBracket + 1:CloseBracket])
        OutputFileCache += ">" * number
        
    elif line.startswith("dpdec"):
        OpenBracket = line.index("(")
        CloseBracket = line.index(")")
        number = int(line[OpenBracket + 1:CloseBracket])
        OutputFileCache += "<" * number
        
    elif line.startswith("inc") and line.startswith("dpinc") == False:
        OpenBracket = line.index("(")
        CloseBracket = line.index(")")
        number = int(line[OpenBracket + 1:CloseBracket])  # Extract number
        OutputFileCache += "+" * number  # Repeat '+' number times)
        
    elif line.startswith("dec") and line.startswith("dpdec") == False:
        OpenBracket = line.index("(")
        CloseBracket = line.index(")")
        number = int(line[OpenBracket + 1:CloseBracket])
        OutputFileCache += "-" * number
        
    elif line.startswith("input"):
        OutputFileCache += ","
        
    elif line.startswith("output"):
        OutputFileCache += "."
        
    elif line.startswith("loop") and line.startswith("endloop") == False:
        OutputFileCache += "["
        
    elif line.startswith("endloop"):
        OutputFileCache += "]"
        


OutputFile.write(OutputFileCache)
OutputFile.close()

print(OutputFileCache)