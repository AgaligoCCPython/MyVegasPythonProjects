import colorama
from colorama import Fore, Back, Style
import time
import sys
from turtle import delay
def slow_print(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

print(Fore.RED + "Hello world, My name is Malee!" + Style.RESET_ALL, end="\n")
#Ask player name ?
player = input("What is your name?")
#Answer 
slow_print("Hello " + player + ", hope you are happy!", delay=0.1)
#ask if player is fine
are_you_fine = input("Are you fine? (yes/no)")
if are_you_fine.lower() == "yes":
    slow_print("That's great to hear!", delay=0.1)
else:
    slow_print("I'm sorry to hear that. I hope things get better soon.", delay=0.1)

print(Fore.BLUE + "Let's do something cool!!" + Style.RESET_ALL ,end="\n")

print(Fore.GREEN + "H   H  EEEEE  L      L        OOO  " + Style.RESET_ALL,end="\n")
print(Fore.GREEN + "H   H  E      L      L       O   O " + Style.RESET_ALL,end="\n")
print(Fore.GREEN + "HHHHH  EEEEE  L      L      O     O" + Style.RESET_ALL,end="\n")
print(Fore.GREEN + "H   H  E      L      L       O   O " + Style.RESET_ALL,end="\n")
print(Fore.GREEN + "H   H  EEEEE  LLLLL  LLLLL    OOO  " + Style.RESET_ALL,end="\n")

like_it = input(Fore.CYAN + "Do you like it? (yes/no)" + Style.RESET_ALL)
if like_it.lower() == "yes":
    slow_print("Yay! I'm glad you like it!", delay=0.1)
else:
    slow_print("Oh no! I'm sorry to hear that.", delay=0.1 )

player_favorite_food = input(Fore.MAGENTA + "What is your favorite food?" + Style.RESET_ALL)
#Answer
slow_print("Oh, " + player_favorite_food + " sounds delicious!", delay=0.1)

player_favorite_color = input(Fore.YELLOW + "What is your favorite color? (Yellow/Blue/Red/Green/Black/White/Orange/Purple/etc.)" + Style.RESET_ALL)
if player_favorite_color.lower() == "yellow":
    slow_print("Yellow is a bright and cheerful color! I love yellow too!", delay=0.1)
else:
    slow_print(player_favorite_color + " is a nice color too!", delay=0.1)

player_favorite_animal = input(Fore.BLUE + "What is your favorite animal?" + Style.RESET_ALL)
if player_favorite_animal.lower() == "dog":
    slow_print("Dog is a loyal and loving animal! I love dogs too!", delay=0.1)
else:
    slow_print(player_favorite_animal + " is a great animal too!", delay=0.1)

player_favorite_hobby = input(Fore.RED + "What is your favorite hobby?" + Style.RESET_ALL)
if player_favorite_hobby.lower() == "reading":
    slow_print("Reading is a wonderful hobby! I love reading too!", delay=0.1)
else:
    slow_print(player_favorite_hobby + " sounds like a fun hobby too!", delay=0.1)

slow_print(Fore.GREEN + "It was nice talking to you, " + player + "! I hope you have a great day!" + Style.RESET_ALL, delay=0.1)
print(Fore.CYAN + " BBBBBBB    Y     Y  EEEEEEE   !!  " + Style.RESET_ALL, end="\n")    
print(Fore.CYAN + " B      B    Y   Y   E         !!  " + Style.RESET_ALL, end="\n")    
print(Fore.CYAN + " BBBBB B      Y Y    EEEEEE    !!  " + Style.RESET_ALL, end="\n")    
print(Fore.CYAN + " B     B       Y     E         !!  " + Style.RESET_ALL, end="\n")    
print(Fore.CYAN + " B      B      Y     E        !!!! " + Style.RESET_ALL, end="\n")    
print(Fore.CYAN + " BBBBBBB       Y     EEEEEEE  !!!! " + Style.RESET_ALL, end="\n")

