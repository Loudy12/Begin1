#Connor Loudermilk
#Room Adventure Project
#Dr.Lori
#April 24th, 2023

import os
import sys




#Welcome Screen
def prompt():
    print("\t\tWelcome to my Room Adventure game\n\n\
You must collect all six items before fighting the Zombie.\n\n\
Moves:\t'go {direction}' (travel north, south, east, or west)\n\
\t'get {item}' (add nearby item to inventory)\n")

    input("Press any key to continue... ")


#Clear
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


#Map Layout
rooms = {
    'Labratory Space': {'North': 'Corn Maze', 'South': 'Basement', 'East': 'Industrial Freezer'},
    'Corn Maze': {'South': 'Labratory Space', 'Item': 'Serum'},
    'Basement': {'North': 'Labratory Space', 'East': 'Server Room', 'Item': 'Ice Cold Beer'},
    'Industrial Freezer' : {'West': 'Labratory Space', 'North': 'Testing Room', 'East': 'Fighting Pit', 'Item': 'Bandages'},
    'Testing Room' : {'South': 'Industrial Freezer', 'East':'Bathroom', 'Item': 'Metal Pipe'},
    'Bathroom': {'West': 'Testing Room', 'Item': 'Black Mask'},
    'Server Room': {'West': 'Basement', 'Item': 'Big Mac'},
    'Fighting Pit': {'West': 'Industrial Freezer', 'Zombie': 'Elephant Zombie'}
    }

#vowels
vowels = ['a', 'e', 'i', 'o', 'u']


inventory = []


current_room = "Labratory Space"


msg = ""

clear()
prompt()

#play loop
while True:

    clear()

    #user info
    print(f"You are in the {current_room}\nInventory : {inventory}\n{'-' * 27}")

    
    print(msg)

    #items
    if "Item" in rooms[current_room].keys():

        nearby_item = rooms[current_room]["Item"]

        if nearby_item not in inventory:

            if nearby_item[-1] == 's':
                print(f"You see {nearby_item}")

            elif nearby_item[0] in vowels:
                print(f"You see an {nearby_item}")

            else:
                print(f"You see a {nearby_item}")
    
    #THE FREAKING ZOMBIE ELEPHANT
    if "Zombie" in rooms[current_room].keys():

        if len(inventory) < 6:
            print(f"You died in the fight with the  {rooms[current_room]['Zombie']}, find all 6 items!")
            break

        else:
            print(f"You beat the {rooms[current_room]['Zombie']}, and escaped!")
            break

    
    user_input = input("Enter your move:\n")

    #splits move into words
    next_move = user_input.split(' ')

    
    action = next_move[0].title()

    #reset item and direction
    item = "Item"
    direction = "null"

    
    if len(next_move) > 1:
        item = next_move[1:]
        direction = next_move[1].title()

        item = " ".join(item).title()

    # movement 
    if action == "Go":

        try:
            current_room = rooms[current_room][direction]
            msg = f"You travel {direction}"

        except:
            msg = "You can't go that way."
    
    #pick up
    elif action == "Get":
        try:
            if item == rooms[current_room]["Item"]:

                if item not in inventory:

                    inventory.append(rooms[current_room]["Item"])
                    msg = f"{item} retrieved!"

                else:
                    msg = f"You already have the {item}"
            
            else:
                msg = f"Can't find {item}"
        except:
            msg = f"Can't find {item}"
    
    #exit program
    elif action == "Exit":
        break

    #anything else doesnt work
    else:
        msg = "Invalid command"
        
        
        
        
        
        
        
#Works Cited
#https://www.makeuseof.com/python-text-adventure-game-create/
#Python for beginners
#https://www.youtube.com/watch?v=lI6S2-icPHE
#https://codereview.stackexchange.com/questions/209922/simple-text-escape-room-game
#ChatGPT
#https://www.bing.com/videos/search?q=room+adventure+python+games&&view=detail&mid=D0B2E211DA42D9E0562ED0B2E211DA42D9E0562E&&FORM=VRDGAR&ru=%2Fvideos%2Fsearch%3Fq%3Droom%2Badventure%2Bpython%2Bgames%26FORM%3DHDRSC6