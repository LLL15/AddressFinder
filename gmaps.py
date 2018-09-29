#! /usr/bin/python3
import sys, webbrowser

try:
    import pyperclip
except ImportError:
    print('!Error - pyperclip module not found, check README for help!\nExiting...')
    sys.exit()

sys.argv = input('Enter address and city: ')

if len(sys.argv) > 1:
    address = ''.join(sys.argv[:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)


