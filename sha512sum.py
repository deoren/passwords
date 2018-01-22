#!/usr/bin/env python3

# Purpose: Prompt user for input and generate a sha512 hash from it

# References
#
#   http://www.java2s.com/Code/Python/GUI-Tk/Getinputvaluefromadialog.htm
#   http://www.tutorialspoint.com/python/python_command_line_arguments.htm
#   http://sweetme.at/2014/01/22/how-to-get-user-input-from-the-command-line-in-a-python-script/
#   http://stackoverflow.com/questions/16179875/command-line-input-in-python

import hashlib

response = input("Please enter the string to create a sha512 has from: ").encode('utf-8')

checksum = hashlib.sha512(response).hexdigest()

print(checksum)
