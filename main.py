import matplotlib.pyplot as plt
import random


class Room:
    def __init__(self, doors, cords=(0, 0), r_name='name', r_desc='desc', up=(0, 0), down=(0, 0), right=(0, 0), left=(0, 0)):
        self.doors = doors
        self.cords = cords
        self.r_name = r_name
        self.r_desc = r_desc
        self.up = up
        self.down = down
        self.right = right
        self.left = left


room_dict = {
    (0,0): Room([1,3,2,4], (0,0), 'Sleep Pod', 'The place where you sleep',(0,1),(0,-1),(1,0),(-1,0))
}


room_types = ['Spawn','US Lab','Jappense Lab', 'Airlock','Pantry','Med Bay','Fittness','Escape Pod','Command Center','Research Lab','Sleeping Pod','Bathroom','Window Bay','Storage','Tunnel']
room_attributes = ['Leaking Air', 'Locked Door','Crafting Bench','Dark Room', 'Light Room']
room_items = ['Space Suit', 'light saber', 'robot friend','flash light','alien gun','3d printer','cloths','med-kit','gravity boots', 'prostetic leg','procetic arm', 'prostetic eye', 'pressure senser', 'siri earpiece','states watch', 'ointment','sex toys']
event_types = ['Alien Attack', 'AI Attack', 'Meteor Strick', 'Space Pirates','Disease Epidemic', 'Reasource Lost', 'Fire', 'Gase Leak']
enemy_types = ['Boss', 'Alien', 'Robot','Space Pirate', 'Infected Crewmember']

spawn = Room([1,3,2,4])
b = Room([2])
l = Room([4])
rl = Room([3,4])
r = Room([3])
rb = Room([3,2])
t = Room([1])
tb = Room([1,2])
tl = Room([1,4])
tr = Room([1,3])

top = [t,tb,tl,tr]
right = [rl,r,rb,tr]
left = [l,rl,tl]
bottom = [b,rb,tb]


def spawn_block(pb_cord, doors):
    x,y = pb_cord
    
    if doors == 1:
        rand = random.randrange(0, len(bottom))
        nb_doors = bottom[rand]
        nb_cords = (x,y+1)
        return nb_doors, nb_cords

    elif doors == 3:
        rand = random.randrange(0, len(left))
        nb_doors = left[rand]
        nb_cords = (x+1, y)
        return nb_doors, nb_cords

    elif doors == 2:
        rand = random.randrange(0, len(top))
        nb_doors = top[rand]
        nb_cords = (x, y-1)
        return nb_doors, nb_cords

    else:
        rand = random.randrange(0, len(right))
        nb_doors = right[rand]
        nb_cords = (x-1, y)
        return nb_doors, nb_cords

def r_move_func(cords, door_list, direction):
    x,y = cords
    door_list = door_list.doors
    if direction == 'up':
        if 1 in door_list:
            return (x,y+1)
    if direction == 'down':
        if 2 in door_list:
            return (x, y-1)
    if direction == 'right':
        if 3 in door_list:
            return (x+1, y)
    if direction == 'left':
        if 4 in door_list:
            return (x-1, y)


continue_gen = True
flagged = set({})
while continue_gen == True:
    door_count = 0

    iter_list = []
    for b in room_dict:
        iter_list.append(b)

    for block in iter_list:
        
        if len(room_dict[block].doors) != 1:
            for i, door in enumerate(room_dict[block].doors):
                nb_doors, nb_cords = spawn_block(room_dict[block].cords, door)
                repeat = False
                for value in room_dict.values():
                    if nb_cords == value.cords:
                        repeat = True
                        flagged.add((block, door))


                if repeat == False:
                    room_dict.update({nb_cords: Room(nb_doors.doors, nb_cords, 'name', 'desc', r_move_func(nb_cords, nb_doors, 'up'), r_move_func(nb_cords, nb_doors, 'down'), r_move_func(nb_cords, nb_doors, 'right'), r_move_func(nb_cords, nb_doors, 'left'))})  # str(int(max(room_dict, key=int))+1):

                    if len(nb_doors.doors) != 1:
                        door_count += len(nb_doors.doors)

    if door_count == 0:
        continue_gen = False

import math
dist_list = []
for cord in room_dict:
    x,y =cord
    x1 = 0
    y1 = 0
    x2 = x
    y2 = y
    max_dis = 0
    dist = math.sqrt((x2-x1)**2+(y2-y1)**2)
    if dist >= max_dis:
        max_dis = dist
        max_cord = cord



class Player:
    def __init__(self, name):
        self.name = name
        self.loc = (0,0)



def player_move():
    in_room = True
    while in_room == True:
        ask = 'where whould yo ulike to move'
        dest = input(ask)
        if dest == 'up':
            destination = room_dict.get(p_gamer.loc).up
            if destination != None:
                movement_handler(destination)
                in_room = False
            else:
                print('there is a wall there try again')
        elif dest == 'down':
            destination = room_dict.get(p_gamer.loc).down
            if destination != None:
                movement_handler(destination)
                in_room = False
            else:
                print('there is a wall there try again')
        elif dest == 'right':
            destination = room_dict.get(p_gamer.loc).right
            if destination != None:
                movement_handler(destination)
                in_room = False
            else:
                print('there is a wall there try again')
        elif dest == 'left':
            destination = room_dict.get(p_gamer.loc).left
            if destination != None:
                movement_handler(destination)
                in_room = False
            else:
                print('there is a wall there try again')


def movement_handler(destination):
    print('you have moved to ', destination)
    p_gamer.loc = destination

for i in room_dict:
    print(i)
    x, y = i
    plt.scatter(x,y)
    print(room_dict[i].doors, room_dict[i].cords)

print('lenth ', len(room_dict))
print('max: ',max_cord)


plt.ylabel('some numbers')
plt.show()
import sys
game_over = False
while True:
    print('start of adventure game!')
    p_name = input('Please enter your name')
    p_gamer = Player(p_name)
    print('you are in room: ', p_gamer.loc)
    while game_over == False:
        player_move()
        print('you are in room: ', p_gamer.loc)
        if p_gamer.loc == max_cord:
            print('congrats! you made it to the escape pod')
            print('game over')
            game_over = True
            sys.exit()







