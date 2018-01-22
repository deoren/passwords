#!/usr/bin/env python2.7

# Purpose:
#
#   Generates random 108 char passwords by generating UUID and inserting random
#   "special" and uppercase characters.

# TODO:
#
# * Accept command line option to limit special chars used


import random
import string
import sys
import uuid


# sys.argv[0] is the name of this script
# sys.argv[1] is the first argument
try:

    # Force integer type since we are going to use in a string slice later
    max_password_length = int(sys.argv[1])
except:
    max_password_length = None

# Grab a UUID and convert to a string. We'll use this as our "base" string that
# we will further manipulate further modifications to.
new_password_base = str(uuid.uuid4())

# TODO: Refine this list
special_characters = [
    '~', '!', '"', '?', '$', '%', '^', '&', '(', '@', '#', ')',
    '+', '-', '*', '=', '_', '=', '>', '<',
]

# Going to dynamically build this
new_password_char_list = []
new_password = ''

for char in new_password_base:

    # Spin the bottle
    random.shuffle(special_characters)

    # Grab the first special character from the shuffled list
    new_password_char_list.append(char + special_characters[0])

    # Grab a random uppercase letter
    new_password_char_list.append(random.choice(string.ascii_uppercase))


# One last shuffle
random.shuffle(new_password_char_list)

# Convert list to string
new_password = ''.join(new_password_char_list)

# No matter the current length, we only want the first X characters to comply
# with command-line argument
print new_password[0:max_password_length]
