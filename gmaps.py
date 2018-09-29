#! /usr/bin/python3
import sys

try:
    import pyperclip, webbrowser
except ImportError:
    print('!Error - One or multiple modules not found, check README for help!\nExiting...')
    sys.exit()

sys.argv = input('Enter address and city: ')

if len(sys.argv) > 1:
    address = ''.join(sys.argv[:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)


