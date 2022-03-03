import os
import sys
import time

# This clears the console
def wash():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


# This prints out each letter one at a time
def write(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)
    print()
    time.sleep(0.5)


# Special version of write() for prompting choices
def write_no_pause(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)
    print()


# Special version of write() that doesn't add an extra line
def write_no_line(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)
    time.sleep(0.5)


# Special version of write() that allows for custom time
def write_custom(s, t):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(t)
    time.sleep(0.5)