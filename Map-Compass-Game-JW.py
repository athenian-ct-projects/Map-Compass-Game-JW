print("Hi! Welcome to the map and compass game!")
print("Today, your character will be the dollar sign and you are bringing the dollar sign to the destintation.")
print("enter your directions in capital letters!")
# first i am doing a "wall" for the $ to walk on it
class MapGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height


def draw_grid(graph, width=2):
    for y in range(graph.height):
        for x in range(graph.width):
            print("%%-%ds" % width % '.', end="")
        print()
        
def main():
    g = MapGrid(30, 15)
    draw_grid(g)


if __name__ == '__main__':
    main()
#grid is simply defined by its width and height The local width variable has to do with the spacing, so it’s more of an aesthetic thing
from random import randint, choice


class MapGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = [] 


def draw_grid(graph, width=2):
    for y in range(graph.height):
        for x in range(graph.width):
            if (x, y) in graph.walls:
                print("%%-%ds" % width % '#', end="")
            else:
                print("%%-%ds" % width % '.', end="")
        print()


def get_walls(g, pct=.3):
#pct is the percentage of the map covered by walls 
    out = []
    for i in range(int(g.height*g.width*pct)//2):

            x = randint(1, g.width-1)
            y = randint(1, g.height-2)
#To have the walls nicely distributed we first need to get the total number of tiles (width*height) and multiply by the percentage of those tiles we want to make into walls. 
#Then we iterate over half of that number and make two tiles in each loop;
#one slightly changed by some random noise so that we get a more cave-looking distribution with many wall tiles next to each other.

# i made two pieces of wall based on the same random x and y but adding a bit of noise in order to have passages and more cave-looking walls.

#Walls are defined as tiles that occupy one space on the grid; so they are represented in code as an (x, y) tuple, which the draw function will 
#display as a pound or hashtag symbol.Optionally, we added a function named get_walls to create a nice list of tiles for us.
            out.append((x, y))
            out.append((x + choice([-1, 0, 1]), y + choice([-1, 0, 1])))
            return out
#based on them we use the built in library random to generate a nicely distributed set of walls
from random import randint, choice
import subprocess
import platform
import time


class MapGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
        self.start = (0, 0)
        self.goal = (width-1, height-1)
        self.player = (0, 0)

    def move_player(self, d):
        x = self.player[0]
        y = self.player[1]
        pos = None

        if d[0] == 'E':
            pos = (x + 1, y)
        if d[0] == 'W':
            pos = (x - 1, y)
        if d[0] == 'N':
            pos = (x, y - 1)
        if d[0] == 'S':
            pos = (x, y + 1)

        if pos not in self.walls:
            self.player = pos

        if pos == self.goal:
            print("You made it to the end!")
#the code above are the directions for each different directions to go when you enter the corresponding directions

def draw_grid(g, width=2):
    for y in range(g.height):
        for x in range(g.width):
            if (x, y) in g.walls:
                symbol = '#'
            elif (x, y) == g.player:
                symbol = '$'
            elif (x, y) == g.start:
                symbol = '<'
            elif (x, y) == g.goal:
                symbol = '>'
            else:
                symbol = '.'
            print("%%-%ds" % width % symbol, end="")
        print()


def get_walls(g: MapGrid, pct=.25) -> list:
        out = []
        for i in range(int(g.height*g.width*pct)//2):

            x = randint(1, g.width-2)
            y = randint(1, g.height-2)

            out.append((x, y))
            out.append((x + choice([-1, 0, 1]), y + choice([-1, 0, 1])))
        return out


def clear():
    subprocess.Popen("cls" if platform.system() == "Windows" else "clear", shell=True)
    time.sleep(.01)

#the code below is to ask the people to enter the NORTH, WEST, SOUTH AND EAST to move the $
def main():
    g = MapGrid(10, 10)
    g.walls = get_walls(g)

    while g.player != g.goal:
        draw_grid(g)
        d = input("Which way? (N, E, S, W)")
        g.move_player(d)
        clear()
    print("You made it!")


if __name__ == '__main__':
    main()
