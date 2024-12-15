def user_options_yes_or_no(message: str):
    yes_or_no_verification_loop = bool(False)
    yes_or_no = input(message + " reply with True, yes, Y, or False, no, N: ")
    while yes_or_no_verification_loop == False:
        if (yes_or_no.lower() == "true") or (yes_or_no.lower() == "yes") or (yes_or_no.lower() == "n"):
            yes_or_no_verification_loop = True
            return True
        elif (yes_or_no.lower() == "false") or (yes_or_no.lower() == "no") or (yes_or_no.lower() == "n"):
            yes_or_no_verification_loop = True
            return False
        else:
            print("invalid input, try again")