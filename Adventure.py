
import random
import colorama
from colorama import Fore, Style, Back
import sys
import time
import os

# Dictionary for Stat names
stat_names = {
  "stre": "Strength",
  "defe": "Defense",
  "speed": "Speed",
  "inte": "Intelligence",
  "conc": "Concentration",
  "cha": "Charisma"
}

# Creating values for stats
player_name = "TESTNAME"
print_class = Fore.BLUE + "Swordsman" + Style.RESET_ALL
character_class = "sword"
gender = "M"

stre = 0 
defe = 0 
speed = 0
inte = 0
conc = 0
cha = 0
mana = 0
cash = random.randint(21, 26)

def set_name(s):
  global player_name
  player_name = s

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
  print(">", end='')

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

# This opens the main menu and allows for the start of the game
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
  print(">", end='')
  choice = int(input())
  
  if choice == 1:
    wash()
    write_no_line(Style.BRIGHT + "The State of the Kingdom" + Style.RESET_ALL)
    print("------------------------------------------------------------------------------------------------------------------------------")
    
    # Exposition text
    write("A long time ago, and I mean a \x1B[3mvery\x1B[0m long time ago, was a great king. Under his rule, the kingdom prospered! Then he died lol.")
    write("The mournful citizens buried him along with his wealth beneath the city in what is now known as the Royal Catacombs.")
    write("Money wasn't the only thing he was buried with, however. He also has an artifact known as the Founder's Crown.")
    write("The Catacombs used to be the personal graveyard of the royal family but were eventually abandoned.")
    write("Centuries have passed and the old tombs are overrun with all sorts of monsters.")
    write("Interest in the Catacombs has risen again with the coronation of the new king.")
    write("He claims that the Founder's Crown must be retrieved in order to restore the legitimacy of the Royal Family.")
    write_no_line("A group of knights have been established in order to secure \"the bag.\"")
    
    print("------------------------------------------------------------------------------------------------------------------------------")
    choice = -1
    write_no_pause("1. Continue")
    choice = int(input())
    
    if choice == 1:
      wash()
  
  elif choice == 2:
    wash()
    write_no_line(Style.BRIGHT + "Instructions" + Style.RESET_ALL)
    print("------------------------------------------------------------------------------------------------------------------------------")

    write("Welcome to the CATACOMBS.")
    write("Throughout the game, you will encounter enemies and be given a set of actions. The success rate of some of these actions will be based on your stats.")
    write("The higher your stats, the stronger you are.")
    write_no_line("You will probably die. Do not worry, there are checkpoints scattered through the game and you will be notified when you reach one.")
    print("------------------------------------------------------------------------------------------------------------------------------")
    choice = -1
    write_no_pause("1. Return to menu")
    choice = int(input())
    if choice == 1:
      start_menu()
  
  elif choice == 3:
    wash()
    write_no_line(Style.BRIGHT + "Settings" + Style.RESET_ALL)
    print("------------------------------------------------------------------------------------------------------------------------------")

    choice = -1
    write_no_pause("1. Return to menu")
    choice = int(input())
    if choice == 1:
      start_menu()
  
  elif choice == 4:
    write_no_line(Style.BRIGHT + "About" + Style.RESET_ALL)
    print("------------------------------------------------------------------------------------------------------------------------------")

    choice = -1
    write_no_pause("1. Return to menu")
    choice = int(input())
    if choice == 1:
      start_menu()
  
  else:
    wash()
    write("Program Ended")
    sys.exit()

# Allows for foolproof class selection
def choose_class():
  choice = int(input())
  global print_class
  global character_class

  if choice == 1:
    print()
    print_class = Fore.BLUE + "Swordsman" + Style.RESET_ALL
    character_class = "sword"
    write(Fore.LIGHTYELLOW_EX + "\"Ah a " + print_class + Fore.LIGHTYELLOW_EX + " huh? We could always use a few of you on the Patrol. Alright, you can enter.\"" + Style.RESET_ALL)
    choice = -1
  
  elif choice == 2:
    print()
    print_class = Fore.BLUE + "Archer" + Style.RESET_ALL
    character_class = "arch"
    write(Fore.LIGHTYELLOW_EX + "\"Oh, an " + print_class + Fore.LIGHTYELLOW_EX + "? Consider joining the Hunt. They need a few archers right now. Alright, you can enter.\"" + Style.RESET_ALL)
    choice = -1
  
  elif choice == 3:
    print()
    print_class = Fore.BLUE + "Mage" + Style.RESET_ALL
    character_class = "mage"
    write(Fore.LIGHTYELLOW_EX + "\"A " + print_class + Fore.LIGHTYELLOW_EX + "? You might want to pay a visit to the Seer. Please enter.\"" + Style.RESET_ALL)
    choice = -1
  
  else:
    print(Fore.RED + "/Not a valid option. Try Again/" + Style.RESET_ALL)
    choose_class()

# Plays Intro Scene
def play_intro():
  global player_name
  global character_class
  global cash

  wash()
  write(Style.BRIGHT + "Entrance to the Capital" + Style.RESET_ALL)
  write("On the 1st day of the new season, a hooded stranger rides into the capital in a wagon. No one notices them, it's the largest city in the kingdom after all.")
  write("No one is aware that this stranger is going to change everything.")
  write("Well they might. They may also quit the game before that ¯\\_(ツ)_/¯")
  write(Fore.LIGHTCYAN_EX + "\"We've arrived at the capital. The ride ends here.\" " + Style.RESET_ALL + "A voice says from the front of the wagon. It's the driver.")
  write("The stranger only nods and tosses a silver coin to the driver and gets off at the town gates.")
  write(Fore.LIGHTYELLOW_EX + "\"Halt. State your name.\"" + Style.RESET_ALL + " One of the guards lazily requests.")
  write_no_pause("The stranger ponders for a moment and decides to claim they are called:")
  
  set_name(input())
  
  print()
  
  write(Fore.LIGHTYELLOW_EX + "\"" + player_name + ". Alright I think I've got it.\"" + Style.RESET_ALL + " The guard says as he scribbles something on his notepad. " + Fore.LIGHTYELLOW_EX + "\"What is your profession?\"" + Style.RESET_ALL)
  write("With barely a moment's hesitation, " + player_name + " replies that they are: ")
  
  write("  1. A " + Fore.BLUE + "Swordsman" + Style.RESET_ALL + " in training.")
  write("  2. A novice " + Fore.BLUE + "Archer" + Style.RESET_ALL + ".")
  write_no_pause("  3. A fledgeling " + Fore.BLUE + "Mage" + Style.RESET_ALL + ".")
  
  choose_class()
  
  write_no_pause(" 1. Continue")
  choice = int(input())
  if choice == 1:
    write_custom("Loading Area.....", 0.2)
  
  # Now we will determine the player's stats
  wash()
  write(Style.BRIGHT + "The Capital" + Style.RESET_ALL)
  write("Our protagonist is greeted by a bustling city. The sound of voices fill their ears as people rush by.")

  if character_class == "sword":
    write("Feeling a bit overwhelmed, " + player_name + " decides to follow the guard's advice and visit the Patrol.")
    time.sleep(1)
    write("After stumbling around the city for a few hours, they finally arrive at the Patrol's headquarters.")
    write("They enter the building and walk up to the desk where a bearded man sits.")
    write("The bearded man looks at " + player_name + " with a concerned glance before asking " + Fore.LIGHTYELLOW_EX + "\"Are you sure you're in the right place?\"" + Style.RESET_ALL)

    charisma_rating = 0
    choice = -1
    write("  1. " + Fore.BLUE + "\"Of course, I'm here to apply for the Patrol.\"" + Style.RESET_ALL)
    write_no_pause("  2. " + Fore.BLUE + "\"Isn't this the Patrol's HQ?\"" + Style.RESET_ALL)

    choice = int(input())

    if choice == 1:
      print()
      write(Fore.BLUE + "\"Of course, I'm here to apply for the Patrol.\" " + Style.RESET_ALL)
      charisma_rating += 1
      choice = -1
      write(Fore.LIGHTYELLOW_EX + "\"The application fee is " + Fore.GREEN + "5" + Fore.LIGHTYELLOW_EX + " crowns.\"" + Style.RESET_ALL)
      write("Crowns are the main currency of the kingdom. Pennies are worth " + Fore.GREEN + "1" + Style.RESET_ALL + " crown. Silver coins are worth " + Fore.GREEN + "10" + Style.RESET_ALL + ". Gold coins are worth " + Fore.GREEN + "100" + Style.RESET_ALL + ".")
      write(player_name + " checks their wallet and sees that they have " + Fore.GREEN + str(cash) + Style.RESET_ALL + " crowns. They hand " + Fore.GREEN + "5" + Style.RESET_ALL + " pennies to the receptionist.")
      cash -= 5

    else:
      print()
      write(Fore.BLUE + "\"Isn't this the Patrol's HQ?\"" + Style.RESET_ALL)
      choice = -1
      charisma_rating -= 1
      write("The bearded man shoots you an annoyed glance and replies, " + Fore.LIGHTYELLOW_EX + "\"Yes it is. What do you want?\"" + Style.RESET_ALL)
      write(player_name + " says, " + Fore.BLUE + "\"I want to apply.\"")
      write(Fore.LIGHTYELLOW_EX + "\"The application fee is " + Fore.GREEN + "7" + Fore.LIGHTYELLOW_EX + " crowns.\"" + Style.RESET_ALL)
      write("Crowns are the main currency of the kingdom. Pennies are worth " + Fore.GREEN + "1" + Style.RESET_ALL + " crown. Silver coins are worth " + Fore.GREEN + "10" + Style.RESET_ALL + ". Gold coins are worth " + Fore.GREEN + "100" + Style.RESET_ALL + ".")
      write(player_name + " checks their wallet and sees that they have " + Fore.GREEN + str(cash) + Style.RESET_ALL + " crowns. They hand " + Fore.GREEN + "7" + Style.RESET_ALL + " pennies to the receptionist.")
      cash -= 7
    write(Fore.LIGHTYELLOW_EX + "\"Hey you!\"" + Style.RESET_ALL + " The receptionist yells at a nearby officer," + Fore.LIGHTYELLOW_EX + "\"We have another applicant!\"" + Style.RESET_ALL)
    write("The officer, wearing light chainmail, begrudgingly gets out of his seat and says," + Fore.LIGHTYELLOW_EX + "\"Right, follow me.\"" + Style.RESET_ALL)
    write(player_name + " follows the officer through the building until they reach an open space. 3 people, presumably applicants, are sitting in the shade.")
    write("")
    # write(Fore.LIGHTYELLOW_EX + "\"You will have a practice spar with Louis here.\"")

  elif character_class == "arch":
    write("Feeling a bit overwhelmed, " + player_name + " decides to follow the guard's advice and and apply for the Hunt.")
  
  else:
    write("Feeling a bit overwhelmed, " + player_name + " decides to follow the guard's advice and meet the Seer.")

# Time to actually run Python
#start_menu()
play_intro()
