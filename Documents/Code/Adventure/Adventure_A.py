# map description
rows = 3
cols = 3
# message to print on arriving at location
message = ["you are in a sunny meadow with a river to the south.", "you are in a forest.", "you are in a forest.",
           "you are knee deep in a river.", "you are ankle deep in a river.", "you are in a forest.",
           "you are on the edge of a cliff.", "you are in a forest.", "you are in a forest."]
# item(s) at location
item = [[], [], [],
        [], ["pebble"], ["log"],
        ["sword"], [], []]
# monster at location
monster = ["", "", "",
           "", "", "",
           "", "wolf", ""]
# the reason a player *can't* move in a particular direction from location; "" allows movement
n = ["you've reached the edge of the world.", "you've reached the edge of the world.", "you've reached the edge of the world.",
     "", "", "",
     "there is a sheer drop to the river below.", "", ""]
e = ["", "", "you've reached the edge of the world.",
     "", "", "you've reached the edge of the world.",
     "", "", "you've reached the edge of the world."]
s = ["", "", "",
     "there is an unscalable cliff.", "", "",
     "you've reached the edge of the world.", "you've reached the edge of the world.", "you've reached the edge of the world."]
w = ["you've reached the edge of the world.", "", "",
     "ythe river gets too deep to follow.", "", "",
     "you've reached the edge of the world.", "", ""]

# starting conditions
location = [1, 1]
inventory = []

# function definitions
def error (): # prints an error message
    print "oh no! something's gone horribly wrong. please exit and try again."

def is_valid (): # checks that the map is valid
    valid = True
    for grid in [message, item, monster, n, e, s, w]:
        if len (grid) != rows*cols:
            valid = False
    return valid
    
def grid (loc): # returns a list index from a grid reference
    if loc[0] >=0 and loc[0] < rows and loc[1] >= 0 and loc[1] < cols:
        return loc[0]*cols + loc[1]
    else:
        error ()
        return -1

def move (compass): # moves to a new location, if possible
    global location
    
    if compass == 'n':
        if n[grid (location)]:
            print "you can't go that way; " + n[grid (location)]
        else:
            location[0] = location[0] - 1

    if compass == 'e':
        if e[grid (location)]:
            print "you can't go that way; " + e[grid (location)]
        else:
            location[1] = location[1] + 1

    if compass == 's':
        if s[grid (location)]:
            print "you can't go that way; " + s[grid (location)]
        else:
            location[0] = location[0] + 1

    if compass == 'w':
        if w[grid (location)]:
            print "you can't go that way; " + w[grid (location)]
        else:
            location[1] = location[1] - 1

    print message[grid(location)]

def take (item_name): # moves an item from the map to the inventory
    global item
    global inventory
    
    if item_name in item[grid (location)]:
        item[grid (location)].pop(item[grid (location)].index (item_name))
        inventory.append (item_name)
    else:
        print "that item isn't here!"

def drop (item_name): # moves an item from the inventory to the map
    global item
    global inventory

    if item_name in inventory:
        inventory.pop (inventory.index (item_name))
        item[grid (location)].append (item_name)
    else:
        print "you don't have that item!"

def kill (monster_name): # kills a monster
    global monster

    if monster_name[0:len (monster[grid (location)])] == monster[grid (location)]:
        item_name = monster_name[len (monster[grid (location)]) + 1:]
        if item_name[0:5] == "with ":
            if item_name[5:] in inventory:
                print monster[grid (location)] + " killed"
                monster[grid (location)] = ""
            else:
                print "you don't have that item!"
        else:
            print "kill " + monster[grid (location)] + " with what?"
    else:
        print "kill what?"

# main
def main ():
    print message[grid (location)]

    command = ''
    while command != 'x':
        if item[grid (location)] or monster[grid (location)]:
            print "in front of you is:"
        if item[grid (location)]:
            for i in item[grid (location)]:
                print i
        if monster[grid (location)]:
            print monster[grid (location)]
            
        command = raw_input ('>').lower ()
        if command[0:3] == "go ":
            command = command[3:]
            if command in ['n', 'e', 's', 'w', "north", "east", "south", "west"]:
                move (command[0])
            else:
                print "go where?"
        elif command in ['n', 'e', 's', 'w', "north", "east", "south", "west"]:
            move (command[0])
        elif command[0:4] == "take":
            if len (command) > 5 and command[4] == ' ':
                take (command[5:])
            else:
                print "take what?"
        elif command[0:4] == "drop":
            if len (command) > 5 and command[4] == ' ':
                drop (command[5:])
            else:
                print "drop what?"
        elif command[0:4] == "kill":
            if len (command) > 5 and command[4] == ' ':
                kill (command[5:])
            else:
                print "kill what?"
        elif command == "inv":
            print inventory
        elif command in ["exit", 'x']:
            print "goodbye"
        else:
            print "what?"

# check that the map is valid; run main ()
if is_valid ():
    print "map is valid. let's play"
    main ()
else:
    print "invalid map"
