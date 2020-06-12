from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def peek(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)

def traverse_maze(player):
    # What we will return
    traversal_path = []  # List of tuples
    
    opposite_direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

    # rooms we have visited and rooms ahead
    visited_rooms = set() 
    s = Stack()

    cur_room = player.current_room

    # added two initially because I instantly pop one. Probably not good practice.
    # s.push(cur_room) # current, room and direction traveled

    while len(visited_rooms) != 500:
        # Cur room id

        if cur_room.id not in visited_rooms:
            visited_rooms.add(cur_room.id)

        prev_room = cur_room

        # choose a direction
        for direction in cur_room.get_exits():
            if cur_room.get_room_in_direction(direction).id not in visited_rooms: 
                # updates
                s.push(opposite_direction[direction])
                player.travel(direction)
                traversal_path.append(direction)
                visited_rooms.add(player.current_room.id)

                cur_room = player.current_room
                break # so we don't actually loop over the other exits. Just the first unexplored
        
        # This is what makes us traverse. Means it wasn't updated in loop above.
        if cur_room == prev_room:
            direction = s.pop()
            player.travel(direction)
            traversal_path.append(direction)

            cur_room = player.current_room


        # Choose a random direction to travse
            # keep track of forks in the road, so when we get to a dead end we can traverse to an unexplored fork

    return list(traversal_path)

    # We are going to somewhat arbitrarily default to W, N, E, then S
    # If we're at an impass where we can go W, then we will go N, and so on.
    # We are mixing DFT and BFS. THe BFS will keep track of paths to old impasses
        # if we get to a dead end we will use the first in queue, which will be shortest list
        # to find the closest impass and move in the appropriate direction.
    
    # populate




if __name__ == "__main__":
    
    world = World()


    # You may uncomment the smaller graphs for development and testing purposes.
    # map_file = "maps/test_line.txt"
    # map_file = "maps/test_cross.txt"
    # map_file = "maps/test_loop.txt"
    # map_file = "maps/test_loop_fork.txt"
    map_file = "maps/main_maze.txt"

    # Loads the map into a dictionary
    room_graph=literal_eval(open(map_file, "r").read())
    world.load_graph(room_graph)

    # Print an ASCII map
    # world.print_rooms()

    player = Player(world.starting_room)
    trav_path = [x for x in traverse_maze(player)]
    print(trav_path)
    print('length: ' + str(len(trav_path)))
    # print(len(t))
    # visited_rooms = set()
    # print(player.current_room.get_room_in_direction('n'))
    # print(player.current_room.get_exits())
    # print('==========')
    # player.travel('n')
    # print(player.current_room.id)

    # traverse_maze(player)

    ###############################
    # # Test the graph class
    # g = Graph()

    # g.add_vertex(305)
    # g.add_vertex(306)

    # g.add_edge(305, 306, 'n')

    # print(g.vertices)
    # print('--------')
    # print(g.get_neighbors(305))