
import random
from colorama import Fore, Style
from PrintFunctions import wash, write, write_no_line, write_custom
from Player import Player
from Scenes import start_menu

cash_base = random.randint(21, 26)
p1 = Player("TEST", None, None, None, None, None, None, None, None, None, None, cash_base)
del cash_base

# Allows for foolproof class selection
def choose_class():
    choice = int(input('> '))

    if choice == 1:
        print()
        p1.print_class = Fore.BLUE + "Swordsman" + Style.RESET_ALL
        p1.character_class = "sword"
        write(
            Fore.LIGHTYELLOW_EX + "\"Ah a " + p1.print_class + Fore.LIGHTYELLOW_EX + " huh? We could always use a few of you on the Patrol. Alright, you can enter.\"" + Style.RESET_ALL)
        choice = -1

    elif choice == 2:
        print()
        p1.print_class = Fore.BLUE + "Archer" + Style.RESET_ALL
        p1.character_class = "arch"
        write(
            Fore.LIGHTYELLOW_EX + "\"Oh, an " + p1.print_class + Fore.LIGHTYELLOW_EX + "? Consider joining the Hunt. They need a few archers right now. Alright, you can enter.\"" + Style.RESET_ALL)
        choice = -1

    elif choice == 3:
        print()
        p1.print_class = Fore.BLUE + "Mage" + Style.RESET_ALL
        p1.character_class = "mage"
        write(
            Fore.LIGHTYELLOW_EX + "\"A " + p1.print_class + Fore.LIGHTYELLOW_EX + "? You might want to pay a visit to the Seer. Please enter.\"" + Style.RESET_ALL)
        choice = -1

    else:
        print(Fore.RED + "/Not a valid option. Try Again/" + Style.RESET_ALL)
        choose_class()


# Plays Intro Scene
def play_intro():
    wash()

    write(Style.BRIGHT + "Entrance to the Capital" + Style.RESET_ALL)
    write("On the 1st day of the new season, a hooded stranger rides into the capital in a wagon. No one notices them, it's the largest city in the kingdom after all.")
    write("No one is aware that this stranger is going to change everything.")
    write("Well they might. They may also quit the game before that ¯\\_(ツ)_/¯")
    write(Fore.LIGHTCYAN_EX + "\"We've arrived at the capital. The ride ends here.\" " + Style.RESET_ALL + "A voice says from the front of the wagon. It's the driver.")
    write("The stranger only nods and tosses a silver coin to the driver and gets off at the town gates.")
    write(Fore.LIGHTYELLOW_EX + "\"Halt. State your name.\"" + Style.RESET_ALL + " One of the guards lazily requests.")
    write("The stranger ponders for a moment and decides to claim they are called:")

    p1.name = (input('> '))

    print()

    write(Fore.LIGHTYELLOW_EX + "\"" + p1.name + ". Alright I think I've got it.\"" + Style.RESET_ALL + " The guard says as he scribbles something on his notepad. " + Fore.LIGHTYELLOW_EX + "\"What is your profession?\"" + Style.RESET_ALL)
    write("With barely a moment's hesitation, " + p1.name + " replies that they are: ")

    write("  1. A " + Fore.BLUE + "Swordsman" + Style.RESET_ALL + " in training.")
    write("  2. A novice " + Fore.BLUE + "Archer" + Style.RESET_ALL + ".")
    write("  3. A fledgeling " + Fore.BLUE + "Mage" + Style.RESET_ALL + ".")

    choose_class()

    write(" 1. Continue")
    choice = int(input('> '))
    if choice == 1:
        write_custom("Loading Area.....", 0.2)

    # Now we will determine the player's stats
    wash()
    write(Style.BRIGHT + "The Capital" + Style.RESET_ALL)
    write("Our protagonist is greeted by a bustling city. The sound of voices fill their ears as people rush by.")

    charisma_rating = 0
    strength_rating = 0
    speed_rating = 0
    intel_rating = 0
    defense_rating = 0
    concen_rating = 0

    if p1.character_class == "sword":
        write("Feeling a bit overwhelmed, " + p1.name + " decides to follow the guard's advice and visit the Patrol.")
        write_custom(".....", 0.2)
        print("")
        write("After stumbling around the city for a few hours, they finally arrive at the Patrol's headquarters.")
        write("They enter the building and walk up to the desk where a bearded man sits.")
        write(
            "The bearded man looks at " + p1.name + " with a concerned glance before asking " + Fore.LIGHTYELLOW_EX + "\"Are you sure you're in the right place?\"" + Style.RESET_ALL)

        choice = -1
        write("  1. " + Fore.BLUE + "\"Of course, I'm here to apply for the Patrol.\"" + Style.RESET_ALL)
        write("  2. " + Fore.BLUE + "\"Isn't this the Patrol's HQ?\"" + Style.RESET_ALL)

        choice = int(input('> '))

        if choice == 1:
            print()
            write(Fore.BLUE + "\"Of course, I'm here to apply for the Patrol.\" " + Style.RESET_ALL)
            charisma_rating += 1
            choice = -1
            write(
                Fore.LIGHTYELLOW_EX + "\"The application fee is " + Fore.GREEN + "5" + Fore.LIGHTYELLOW_EX + " crowns.\"" + Style.RESET_ALL)
            write(
                "Crowns are the main currency of the kingdom. Pennies are worth " + Fore.GREEN + "1" + Style.RESET_ALL + " crown. Silver coins are worth " + Fore.GREEN + "10" + Style.RESET_ALL + ". Gold coins are worth " + Fore.GREEN + "100" + Style.RESET_ALL + ".")
            write(p1.name + " checks their wallet and sees that they have " + Fore.GREEN + str(
                p1.cash) + Style.RESET_ALL + " crowns. They hand " + Fore.GREEN + "5" + Style.RESET_ALL + " pennies to the receptionist.")
            p1.cash -= 5

        else:
            print()
            write(Fore.BLUE + "\"Isn't this the Patrol's HQ?\"" + Style.RESET_ALL)
            choice = -1
            charisma_rating -= 1
            write(
                "The bearded man shoots you an annoyed glance and replies, " + Fore.LIGHTYELLOW_EX + "\"Yes it is. What do you want?\"" + Style.RESET_ALL)
            write(p1.name + " says, " + Fore.BLUE + "\"I want to apply.\"")
            write(
                Fore.LIGHTYELLOW_EX + "\"The application fee is " + Fore.GREEN + "7" + Fore.LIGHTYELLOW_EX + " crowns.\"" + Style.RESET_ALL)
            write(
                "Crowns are the main currency of the kingdom. Pennies are worth " + Fore.GREEN + "1" + Style.RESET_ALL + " crown. Silver coins are worth " + Fore.GREEN + "10" + Style.RESET_ALL + ". Gold coins are worth " + Fore.GREEN + "100" + Style.RESET_ALL + ".")
            write(p1.name + " checks their wallet and sees that they have " + Fore.GREEN + str(
                p1.cash) + Style.RESET_ALL + " crowns. They hand " + Fore.GREEN + "7" + Style.RESET_ALL + " pennies to the receptionist.")

            p1.cash -= 7

        write(
            Fore.LIGHTYELLOW_EX + "\"Hey you!\"" + Style.RESET_ALL + " The receptionist yells at a nearby officer, " + Fore.LIGHTYELLOW_EX + "\"We have another applicant!\"" + Style.RESET_ALL)
        write(
            "The officer, wearing light chainmail, begrudgingly gets out of his seat and says," + Fore.LIGHTYELLOW_EX + "\"Right, follow me.\"" + Style.RESET_ALL)
        write(
            p1.name + " follows the officer through the building until they reach an open space. 3 people, presumably applicants, are sitting in the shade.")
        write(
            Fore.LIGHTYELLOW_EX + "\"You'll have a practice spar with Louis here so we can see how strong you are.\"" + Style.RESET_ALL)
        write("One of the recruits stands up and grabs a wooden staff off of the shelf.")
        write(p1.name + " follows suit and gets a wooden sword.")
        write("The two stand on each end of the field with their weapons drawn and the match begins.")
        write("  1. Continue")
        choice = int(input('> '))

        if abs(choice) > 0:
            wash()

        write("Louis points his staff at " + p1.name + " and lunges forward to strike. " + p1.name + " decides to:")
        write("  1. Raise their sword to block the hit.")
        write("  2. Step to the right to dodge the hit.")
        choice = int(input('> '))

        if choice == 1:
            print()
            write(p1.name + " raises their sword to block the hit and takes a step back as the weapons collide.")
            strength_rating += 1
            choice = -1

        else:
            print()
            write(p1.name + " Steps to the side and avoids the hit.")
            speed_rating += 1
            choice = -1

        write("Louis sneers and jumps back.")
        write("In this moment, " + p1.name + " decides to:")
        write("  1. Raise their sword and slash downward.")
        write("  2. Rush towards Louis and try to stab them directly.")
        choice = int(input('> '))

        if choice == 1:
            print()
            write(p1.name + " raises their sword and slashes downward!")
            strength_rating += 1
            choice = -1
            write("Louis blocks the wooden sword with his staff.")
            write(p1.name + " chooses to:")
            write("  1. Press down with the sword.")
            write("  2. Fall back.")
            choice = int(input('> '))

            if choice == 1:
                print()
                choice = -1
                strength_rating += 1
                concen_rating += 1
                write("They press down with their sword.")
                write(
                    "Louis takes a deep breath and uses all his force to push " + p1.name + " and sends them flying backward.")

            else:
                print()
                choice = -1
                intel_rating += 1
                defense_rating += 1
                write(p1.name + " tries to retreat.")
                write(
                    "As " + p1.name + " tries to fall back, Louis unleashes a powerful kick that sends them flying backward.")

        else:
            print()
            choice = -1
            speed_rating += 1
            intel_rating += 1
            write(p1.name + " rushes towards Louis and tries to stab them directly.")
            write("Louis responds by pushing the blade to the side and gets ready to strike.")
            write("  1. Try to dodge.")
            choice = int(input('> '))

            if choice == 1:
                choice = -1
                write(p1.name + " tries to dodge just as the blade strikes them on the head!")

        print(Fore.RED + "You Died" + Style.RESET_ALL)

    elif p1.character_class == "arch":
        write(
            "Feeling a bit overwhelmed, " + p1.name + " decides to follow the guard's advice and and apply for the Hunt.")

    else:
        write("Feeling a bit overwhelmed, " + p1.name + " decides to follow the guard's advice and meet the Seer.")


# Time to actually run Python
start_menu()
play_intro()
