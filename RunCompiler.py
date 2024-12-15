import BFMake as BFMake
import YesOrNoUserInput as YesOrNoUserInput


source_code_filename = input("Input the filename of the Source Code with the file extension: ")

compiled_code_filename = input("Input the name of the file you wish to save the Brainfuck code in with the file extension: ")
compiled_code_file = open(compiled_code_filename, "x")

is_verbose = YesOrNoUserInput.user_options_yes_or_no("Do you wish to run the compiler in verbose mode?")

linker_only = YesOrNoUserInput.user_options_yes_or_no("Do you wish to run the linker only?")
if linker_only == True:
    BFMake.run_compiler(source_code_filename, compiled_code_filename, is_verbose, linker_only)
else:
    compiled_code_file.write(BFMake.run_compiler(source_code_filename, compiled_code_filename, is_verbose, linker_only))