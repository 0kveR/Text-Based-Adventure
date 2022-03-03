
from colorama import Fore, Style, Back
import time
from PrintFunctions import wash, write, write_no_line, write_custom
import sys

def start_menu():
    wash()
    write_custom(Style.BRIGHT + "THE CATACOMBS" + Style.RESET_ALL + Style.DIM + " (Python Version)" + Style.RESET_ALL, 0.04)
    time.sleep(0.08)
    print()
    print()

    print(Fore.LIGHTGREEN_EX + "1. Play" + Style.RESET_ALL)
    time.sleep(0.3)

    print("2. Instructions")
    time.sleep(0.3)

    print("3. Settings")
    time.sleep(0.3)

    print("4. Info")
    time.sleep(0.3)

    print(Fore.RED + "5. Quit" + Style.RESET_ALL)
    print()
    choice = int(input('> '))

    if choice == 1:
        wash()
        write_no_line(Style.BRIGHT + "The State of the Kingdom" + Style.RESET_ALL)
        print(
            "o----------------------------------------------------------------------------------------------------------------------------o")

        # Exposition text
        write(
            "A long time ago, and I mean a \x1B[3mvery\x1B[0m long time ago, was a great king. Under his rule, the kingdom prospered! Then he died lol.")
        write(
            "The mournful citizens buried him along with his wealth beneath the city in what is now known as the Royal Catacombs.")
        write(
            "Money wasn't the only thing he was buried with, however. He also has an artifact known as the Founder's Crown.")
        write("The Catacombs used to be the personal graveyard of the royal family but were eventually abandoned.")
        write("Centuries have passed and the old tombs are overrun with all sorts of monsters.")
        write("Interest in the Catacombs has risen again with the coronation of the new king.")
        write(
            "He claims that the Founder's Crown must be retrieved in order to restore the legitimacy of the Royal Family.")
        write_no_line("A group of knights have been established in order to secure \"the bag.\"")

        print(
            "o----------------------------------------------------------------------------------------------------------------------------o")
        choice = -1
        write("1. Continue")
        choice = int(input('> '))

        if choice == 1:
            wash()

    elif choice == 2:
        wash()
        write_no_line(Style.BRIGHT + "Instructions" + Style.RESET_ALL)
        print(
            "o----------------------------------------------------------------------------------------------------------------------------o")

        write("Welcome to the CATACOMBS.")
        write(
            "Throughout the game, you will encounter enemies and be given a set of actions. The success rate of some of these actions will be based on your stats.")
        write("The higher your stats, the stronger you are.")
        write_no_line(
            "You will probably die. Do not worry, there are checkpoints scattered through the game and you will be notified when you reach one.")
        print(
            "o----------------------------------------------------------------------------------------------------------------------------o")
        choice = -1
        write("1. Return to menu")
        choice = int(input('> '))
        if choice == 1:
            start_menu()

    elif choice == 3:
        wash()
        write_no_line(Style.BRIGHT + "Settings" + Style.RESET_ALL)
        print(
            "o----------------------------------------------------------------------------------------------------------------------------o")

        choice = -1
        write("1. Return to menu")
        choice = int(input('> '))
        if choice == 1:
            start_menu()

    elif choice == 4:
        write_no_line(Style.BRIGHT + "About" + Style.RESET_ALL)
        print(
            "o----------------------------------------------------------------------------------------------------------------------------o")

        choice = -1
        write("1. Return to menu")
        choice = int(input('> '))
        if choice == 1:
            start_menu()

    elif choice == 24:
        write_custom(Back.MAGENTA + Fore.WHITE + "GOOD CHOICE GOOD CHOICE GOOD CHOICE" + Style.RESET_ALL, 0.03)
        start_menu()

    else:
        wash()
        write("Program Ended")
        sys.exit()