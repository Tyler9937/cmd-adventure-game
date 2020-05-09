class Player:
    def __init__(self, name):
        self.name = name
        self.loc = 'outside'
        self.locc = room['outside']

    def room_obj(self):
        return room[self.loc]

    def change_room(self,cord):
        return self.loc


class Room:
    def __init__(self, loc, desc):
        self.loc = loc
        self.desc = desc




# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


def move(choose):
    if choose == 'n':
        new_room = room['outside'].n_to = room['foyer']
    elif choose == 's':
        new_room = room
    elif choose == 'e':
        new_room = room
    elif choose == 'w':
        new_room = room
    return new_room
    

while True:
    print('start of adventure game!')
    p_name = input('Please enter your name')
    p_gamer = Player(p_name)
    print('you are in room: ',p_gamer.room_obj().loc)
    print('room desc ', p_gamer.room_obj().desc)
    choose = input('what do you want to do, n_to e_to s_to w_to or q to quit')
    if choose == 'q':
        print('bye')
        exit()
    p_gamer.loc = move(choose)
    print(p_gamer.loc.loc)















def spawn_block(pb_cord, doors):
    x, y = pb_cord
    if doors == 1:
        rand = random.randrange(0, len(top))
        nb_doors = top[rand]
        nb_cords = (x, y-1)
        if nb_cords not in room_dict.values():
            return nb_doors, nb_cords
        else:
            return 0, 0
    elif doors == 3:
        rand = random.randrange(0, len(right))
        nb_doors = right[rand]
        nb_cords = (x-1, y)
        if nb_cords not in room_dict.values():
            return nb_doors, nb_cords
        else:
            return 0, 0
    elif doors == 2:
        rand = random.randrange(0, len(bottom))
        nb_doors = bottom[rand]
        nb_cords = (x, y+1)
        if nb_cords not in room_dict.values():
            return nb_doors, nb_cords
        else:
            return 0, 0
    else:
        rand = random.randrange(0, len(left))
        nb_doors = left[rand]
        nb_cords = (x+1, y)
        if nb_cords not in room_dict.values():
            return nb_doors, nb_cords
        else:
            return 0, 0


spawned_list = []
open_doors = 4

new_block = 0
while new_block < 5:
    dict_list = []
    for block in room_dict:
        dict_list.append(block)
    for block in dict_list:
        if block not in spawned_list:
            if len(room_dict[block].doors) != 1:
                for i, door in enumerate(room_dict[block].doors):
                    nb_doors, nb_cords = spawn_block(
                        room_dict[block].cords, door)
                    if nb_doors != 0 and nb_cords != 0:

                        room_dict.update(
                            {f'r{i+1}': Room(nb_doors.doors, nb_cords)})
                        spawned_list.append(block)
                        print(nb_doors.doors, nb_cords)

                else:
                    pass
    new_block += 1


#for i in room_dict:
#    print(i)
#    print(room_dict[i].doors, room_dict[i].cords)



view = curses.initscr()
view.addstr(3, 2, u'\u2588')
view.addstr(3, 3, u'\u2588')
view.addstr(3, 4, u'\u2588')
view.addstr(3, 5, u'\u2588')
view.addstr(3, 6, u'\u2588')
view.addstr(3, 7, u'\u2588')
view.addstr(3, 8, u'\u2588')
view.addstr(3, 9, u'\u2588')
#bottom
view.addstr(6, 2, u'\u2588')
view.addstr(6, 3, u'\u2588')
view.addstr(6, 4, u'\u2588')
view.addstr(6, 5, u'\u2588')
view.addstr(6, 6, u'\u2588')
view.addstr(6, 7, u'\u2588')
view.addstr(6, 8, u'\u2588')
view.addstr(6, 9, u'\u2588')
#left
view.addstr(4, 2, u'\u2588')
view.addstr(5, 9, u'\u2588')
view.addstr(4, 9, u'\u2588')
view.addstr(5, 2, u'\u2588')
view.addstr(4, 1, u'\u2588')
view.addstr(5, 10, u'\u2588')
view.addstr(4, 10, u'\u2588')
view.addstr(5, 1, u'\u2588')

view.addstr(3, 1, u'\u2588')
view.addstr(6, 10, u'\u2588')
view.addstr(3, 10, u'\u2588')
view.addstr(6, 1, u'\u2588')

view = curses.initscr()
view.addstr(3, 2, u'\u2588')
view.refresh()
# full block 2588
#lower half 2584
#left block 258C
#right block 2590
# upper half 2580
view.refresh()
time.sleep(15)

sys.exit()
