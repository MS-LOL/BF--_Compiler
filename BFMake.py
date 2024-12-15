
import re

#
# Function to strip leading and trailing whitespace from each line and remove empty lines
#

def strip_whitespace(lines):
    return [line.strip() for line in lines if line.strip()]

#
# Function to remove both single-line and multi-line comments from the code
#

def remove_comments(lines):
    # Remove single-line comments (starting with //)
    no_single_line = [re.sub(r'//.*', '', line) for line in lines]
    # Remove multi-line comments (enclosed in /* */)
    return re.sub(r'/\*.*?\*/', '', "\n".join(no_single_line), flags=re.S).split("\n")

#
# Function to parse and extract labels and their content from the source code
#

def parse_labels(lines):
    labels = {}  # Dictionary to store label names and their corresponding content
    current_label = None  # Variable to track the current label being processed
    label_content = []  # Temporary storage for the content of the current label
    non_label_lines = []  # Lines that are not part of any label

    for line in lines:
        if line.startswith("label("):
            # Start of a new label, extract its name
            current_label = re.match(r'label\((.+?)\)', line).group(1)
            label_content = []  # Reset the content for the new label
        elif line.startswith("endlabel"):
            # End of the current label, store its content in the dictionary
            labels[current_label] = label_content
            current_label = None  # Reset the current label tracker
        elif current_label:
            # Add lines to the current label's content
            label_content.append(line)
        else:
            # Lines outside labels
            non_label_lines.append(line)

    return labels, non_label_lines

#
# Function to replace `copylabel` references with the corresponding label content
#

def replace_copylabels(lines, labels):
    output = []  # List to store the resolved code
    for line in lines:
        if line.startswith("copylabel("):
            # Extract the label name from the `copylabel` statement
            label_name = re.match(r'copylabel\((.+?)\)', line).group(1)
            if label_name in labels:
                # Replace `copylabel` with the content of the referenced label
                output.extend(labels[label_name])
            else:
                raise ValueError(f"Undefined label: {label_name}")
        else:
            # If not a `copylabel`, keep the line as is
            output.append(line)
    return output

# Function to translate the BF-- instructions into Brainfuck code
def translate_to_brainfuck(lines):
    # Mapping of BF-- instructions to Brainfuck symbols
    instruction_map = {
        "inc": "+",
        "dec": "-",
        "dpinc": ">",
        "dpdec": "<",
        "input": ",",
        "output": ".",
        "loop": "[",
        "endloop": "]",
    }
    brainfuck = []  # List to store the translated Brainfuck code
    for line in lines:
        match = re.match(r'(\w+)\((\d+)\)', line)  # Match instructions with arguments, e.g., `inc(3)`
        if match:
            instr, count = match.groups()
            if instr in instruction_map:
                # Append the corresponding Brainfuck symbol repeated `count` times
                brainfuck.append(instruction_map[instr] * int(count))
        elif line in instruction_map:
            # Handle standalone instructions like `loop` and `endloop`
            brainfuck.append(instruction_map[line])
    return "".join(brainfuck)  # Combine all Brainfuck symbols into a single string

# Main compilation function that orchestrates all steps
def compile_bf(source_code, linked_code_filename: str, verbose_mode = True, linker_only = False):

    # Split the source code into lines
    # lines = source_code.split("\n")

    # Remove leading/trailing whitespace and empty lines
    lines = strip_whitespace(lines)

    # Remove single-line and multi-line comments
    lines = remove_comments(lines)

    # Extract labels and their content from the code, separating non-label lines
    labels, non_label_lines = parse_labels(lines)

    # Resolve `copylabel` references to actual label content
    linked_lines = replace_copylabels(non_label_lines, labels)

    # Write the intermediate representation (after label resolution) to a file
    with open(linked_code_filename, "w") as linked_code:
        linked_code.write("\n".join(linked_lines))

    # Print the linked file content to the console
    if verbose_mode == True:
        print("Linked file content:")
        print("\n".join(linked_lines))
    
    # Translate the intermediate representation to Brainfuck code
    if linker_only == False:
        compiled_code = translate_to_brainfuck(linked_lines)
        # Save the compiled Brainfuck code to a file
        compiled_code_filename = linked_code_filename.replace("Linked_", "Compiled").replace(".bfmm", "") + ".bf"
        with open(compiled_code_filename, "x") as compiled_code_file:
            compiled_code_file.write(compiled_code)
        return compiled_code
    else:
        return linked_code

#
# Wrapper function to allow importing as a module
# Use this function when calling the program from another script.
#

def run_compiler(source_code_filename: str, compiled_code_filename: str, is_verbose: bool, linker_only: bool):
    
    # Print the title message if the compiler is running in verbose mode.
    if is_verbose == True:
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
    
    # Linked code filename
    linked_code_filename = "Linked_" + source_code_filename


    # Open the two files needed. The source code and compiled code files and prepare them to be fed to the compile_bf function
    compiled_code = open(compiled_code_filename, "x")
    source_code = open(source_code_filename, "r")


    compiled_code.write(compile_bf(source_code.read(), linked_code_filename, is_verbose, linker_only))
    if is_verbose == True:
        print("Compiled Brainfuck code:")
        print(compiled_code)
    return compiled_code

# Example usage (comment this section when importing as a module)
def run_demo():
    example_source_code = """
    label(Main)
        dpinc(3)
        inc(3)
        copylabel(Add)
    endlabel

    label(Add)
        dpinc(1)
        loop
            dec(1)
            dpdec(1)
            inc(1)
            dpinc(1)
        endloop
        dpdec(1)
    endlabel
    """

    # Compile the source code and write the linked representation to "linked_DemoProgram.bfmm"
    compiled_code = compile_bf(example_source_code, "Linked_DemoProgram.bfmm", True, False)
    compiled_code_file = open("DemoProgramCompiled.bf", "x")
    compiled_code_file.read(compiled_code)
