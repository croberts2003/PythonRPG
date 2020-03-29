# Python Text RPG - Carson Schmidt

from map_gen import ZONENAME, DESCRIPTION, EXAMINATION, SOLVED, UP, DOWN, LEFT, RIGHT, solved_places, zonemap
from inventory import player_inventory
import cmd
import textwrap
import sys
import os
import time
import random

build = "0.01"
screen_width = 100
# global variable controlling the time.sleep function length for faster debugging
run_time = 0.03
wait_time = 1

# Player Setup
class player:
    def __init__(self):
        self.name = ''
        self.role = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.invent = []
        self.location = 'b2'
        self.game_status = False
        self.inventory = []
myPlayer = player()

def type_writer(text):
    global run_time
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(run_time)
    return

# Title Setup
def title_screen_selections():
    option = input("> ")
    if option.lower() == "start":
        setup_game()
    elif option.lower() == "help":
        help_menu()
    elif option.lower() == "quit":
        sys.exit()
    while option.lower() not in ['start', 'help', 'quit']:
        print('Please enter a valid command.')
        option = input("> ")
        if option.lower() == "start":
            setup_game()
        elif option.lower() == "help":
            help_menu()
        elif option.lower() == "quit":
            sys.exit()

def title_screen():
    os.system('cls')  
    print('###############')
    print('# Ecto Hunter #')
    print('###############')
    print('   - Start -   ')
    print('   - Help  -   ')
    print('   - Quit  -   ')
    print('  Build ' + build)
    title_screen_selections()

def help_menu():
    os.system('cls')  
    print('###############')
    print('# Ecto Hunter #')
    print('###############')
    print('Use up, , down, left, right to move')
    print('Type your commands')
    print('Use look to insepect something')
    title_screen_selections()

rolemap = {
    'classical': {
        'description': 'The Classical monster hunter is \ntrained in the art of \nthe sabre and flintlock. Their \nstrenthgs are balanced.',
        'stats': ['100 HP', '50 MP'],
        'unlock': True
    },
    'bastion': {
        'description': 'The Bastion is a role \ndesigned to target hard-hitting \nbeasts. Trained to wield a \nclub and shotgun, their strenthgs \nare balanced towards combat and health.',
        'stats': ['150 HP', '20 MP'],
        'unlock': False
    },
    'lightning': {
        'description': 'Lightning hunters are known for \ntheir skills with the knife \nand musket. Their strenthgs are \nbalanced more towards incantations.',
        'stats': ['50 HP', '80 MP'],
        'unlock': False
    }
}

# game interactivity
def print_location():
    description = zonemap [myPlayer.location] [DESCRIPTION]
    print('\n' + ('#' * (4 + len(description))))
    print('# ' + myPlayer.location.upper() + (' ' * (len(description) - 2)) + ' #')
    print('# ' + zonemap [myPlayer.location] [DESCRIPTION] + ' #')
    print('#' * (4 + len(description)))

def prompt():
    print('\n' + "=========================")
    print('What would you like to do?')
    action = input('> ')
    acceptable_actions = [
        'move', 'go', 'travel', 'walk',
        'quit',
        'examine', 'inspect', 'interact', 'look',
        'inventory', 'backpack'
    ]
    while action.lower() not in acceptable_actions:
        print('Unkown action, try again.\n')
        action = input('> ')
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move()
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())
    elif action.lower() in ['inventory', 'backpack']:
        player_inventory()

def player_move():
    ask = 'Where would you like to move to?\n'
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location] [UP]
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location] [LEFT]
    elif dest in ['right', 'east']:
        destination = zonemap[myPlayer.location] [RIGHT]
    elif dest in ['down', 'south']:
        destination = zonemap[myPlayer.location] [DOWN]
    else:
        player_move()
    if destination == '':
        print ("That way is blocked.")
        main_game_loop()
    movement_handler(destination)

def movement_handler(destination):
    print('\n' + 'You have moved to ' + destination + '.')
    myPlayer.location = destination
    print_location()

def player_examine(action):
    if zonemap[myPlayer.location] [SOLVED]:
        print('You have already searched this zone.')
    else:
        #placeholder for function triggering npc, rand_event, or monster
        return

def main_game_loop():
    while myPlayer.game_status is False:
        prompt()
    # handle if anomaly has been discovered

# game functionality
def setup_game():
    global wait_time
    type_writer('The year is 1890. After \na failed lab experiment in \nGermany, mutated beings began plagueing \nthe land. Hunting and destroying \nthe beasts is humanities only option.')
    time.sleep(wait_time)
    os.system('cls')

    # request name
    question1 = "What is your name?\n"
    type_writer(question1)
    player_name = input('> ')
    myPlayer.name = player_name

    question2 = "What role are you most experienced in?\n"
    i = 0
    roles = ['classical', 'bastion', 'lightning']
    for _ in range(3):
        print(str(i + 1) + '. ' + roles[i])
        i = i + 1
    type_writer(question2)

    while True:
        player_role = input('> ')
        if player_role == 'classical' or player_role == '1':
            stats = rolemap['classical'] ['stats']
            myPlayer.hp = stats [0]
            myPlayer.mp = stats [1]
            player_role = 'classical'
            break
        elif player_role == 'bastion' or player_role == '2':
            stats = rolemap['bastion'] ['stats']
            myPlayer.hp = stats [0]
            myPlayer.mp = stats [1]
            player_role = 'bastion'
            break
        elif player_role == 'lightning' or player_role == '3':
            stats = rolemap['lightning'] ['stats']
            myPlayer.hp = stats [0]
            myPlayer.mp = stats [1]
            player_role = 'lightning'
            break
        else:
            print('Invalid Role, please try again.')
            continue
    myPlayer.role = str(player_role)
    print(str(player_role) + ' info: ' + rolemap[player_role] ['description'])
    myPlayer.role = player_role
    time.sleep(5 )
    os.system('cls')
    main_game_loop()

title_screen()
