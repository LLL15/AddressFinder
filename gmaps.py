#! /usr/bin/python3
# Imports needed modules
import sys, webbrowser

try: # try/except for importing pyperclip module
    import pyperclip
except ImportError: # If pyperclip was not found, error is displayed to user and program exits
    print('!Error - pyperclip module not found, check README for help!\nExiting...')
    sys.exit()


# openGMaps function is where it all happens
def openGMaps(args):
    while True:

        if len(args) > 1: # If len of args is greater than 1
            # It creates address variable where it stored all joined arguments (user's input)
            address = ''.join(args[:])

        else:
            # Then it assumes that the user's wishful location is in his clipboard
            # so it stores the first thing on his clipboard into address variable.
            address = pyperclip.paste()

        # Out of all control-flow statements webbrowser's open function is called which will
        # open a browser with starting URL and append address variable to that URL
        webbrowser.open('https://www.google.com/maps/place/' + address)

        # Asks user if he wants to continue and stores the answer in again variable
        again = input('Do you want to continue? (yes/no):')

        if again == 'yes': # If answer is yes, variable args is assigned again but with different value
            args = input('Enter another address and city: ')
            continue # Also it comes back at the start of while loop and does all the work again.
        else:
            break # If anything else is typed as the answer, loop breaks.


# Taking user's input for wishful location and storing it in sys.argv
sys.argv = input('Enter address and city: ')
# Calling openGMaps with sys.argv as the argument.
openGMaps(sys.argv)

# When loop breaks, godbye message is printed and program is over.
print('Godbye!')

