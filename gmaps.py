#! /usr/bin/python3
import sys
import webbrowser

try:   # try/except block for importing pyperclip module
    import pyperclip
except ImportError:   # If pyperclip was not found, error is displayed to the user and program terminates
    print('Error - pyperclip module not found, check README for help!\nExiting...')
    sys.exit()


# Taking user's input for wishful location and storing it into sys.argv
try:   # try/except block for catching if user hits CTRL+C or CTRL+D
    sys.argv = input('Enter address and city: ')
except (KeyboardInterrupt, EOFError):
    print("Exiting...")
    sys.exit(0)


# openGMaps is the main function
def openGMaps(args):
    while True:
        try:
            if len(args) > 1:   # If length of arguments is greater than 1
                # Address variable is created where it stores all joined arguments together (user's input)
                address = ''.join(args[:])

            else:   # Otherwise when nothing is entered
                # it asks the user if it shall copy first item from his clipboard and store it into address variable
                copy = input("Copy location from clipboard? [Y/N]:")

                if copy.lower() in ["yes", "y"]:
                    address = pyperclip.paste()
                else:   # if user says anything else,loop breaks and function ends
                    break

            # Out of all control-flow statements webbrowser's open function is called which will
            # open a browser with starting URL and append address variable to that URL
            webbrowser.open('https://www.google.com/maps/place/' + address)

            # Asks user if he wants to continue and stores the answer in again variable
            again = input('Do you want to continue? [Y/N]:')

            if again.lower() in ["yes", "y"]:  # If answer is yes
                args = input('Enter another location: ')   # parameter args prompts user again for a location
                continue   # Jumps back to start of loop with newly assigned args

            else:   # If anything else is typed,loop breaks and function ends
                break

        except (KeyboardInterrupt, EOFError):   # If user hits CTRL+C or CTRL+D
            print("Exiting...")
            sys.exit(0)


# Calling openGMaps with sys.argv as the argument.
openGMaps(sys.argv)

# After function is over,goodbye message is printed and script ends
print("Goodbye...")
