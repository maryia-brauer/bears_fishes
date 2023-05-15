import turtle
import random


class World:
    def __init__(self, mX, mY):
        self.__maxX = mX
        self.__maxY = mY
        self.__thingList = []
        self.__grid = []

        for aRow in range(self.__maxY):
            row = []
            for aCol in range(self.__maxX):
                row.append(None)
            self.__grid.append(row)

        self.__wTurtle = turtle.Turtle()
        self.__wScreen = turtle.Screen()
        self.__wScreen.setworldcoordinates(0, 0, self.__maxX - 1,
                                           self.__maxY - 1)
        self.__wScreen.addshape("Bear.gif")
        self.__wScreen.addshape("Fish.gif")
        self.__wTurtle.hideturtle()

    def draw(self):
        self.__wScreen.tracer(0)
        self.__wTurtle.forward(self.__maxX - 1)
        self.__wTurtle.left(90)
        self.__wTurtle.forward(self.__maxY - 1)
        self.__wTurtle.left(90)
        self.__wTurtle.forward(self.__maxX - 1)
        self.__wTurtle.left(90)
        self.__wTurtle.forward(self.__maxY - 1)
        self.__wTurtle.left(90)
        for i in range(self.__maxY - 1):
            self.__wTurtle.forward(self.__maxX - 1)
            self.__wTurtle.backward(self.__maxX - 1)
            self.__wTurtle.left(90)
            self.__wTurtle.forward(1)
            self.__wTurtle.right(90)
        self.__wTurtle.forward(1)
        self.__wTurtle.right(90)
        for i in range(self.__maxX - 2):
            self.__wTurtle.forward(self.__maxY - 1)
            self.__wTurtle.backward(self.__maxY - 1)
            self.__wTurtle.left(90)
            self.__wTurtle.forward(1)
            self.__wTurtle.right(90)
        self.__wScreen.tracer(1)

    def addThing(self, aThing, x, y):
        aThing.setX(x)
        aThing.setY(y)
        self.__grid[y][x] = aThing  # add life-form to grid
        aThing.setWorld(self)
        self.__thingList.append(aThing)  # add to list of life-forms
        aThing.appear()

        def delThing(self, aThing):
            aThing.hide()
        self.__grid[aThing.getY()][aThing.getX()] = None
        self.__thingList.remove(aThing)

    def moveThing(self, oldX, oldY, newX, newY):
        self.__grid[newY][newX] = self.__grid[oldY][oldX]
        self.__grid[oldY][oldX] = None

    def getMaxX(self):
        return self.__maxX

    def getMaxY(self):
        return self.__maxY

    def getThing(self, x, y):
        if x >= self.__maxX or y >= self.__maxY:
            return None
        return self.__grid[y][x]

    def getNeighbors(self, x, y):
        res = []
        if self.__grid[(y - 1) % self.__maxY][x]:
            res.append(self.__grid[(y - 1) % self.__maxY][x])
        if self.__grid[(y + 1) % self.__maxY][x]:
            res.append(self.__grid[(y + 1) % self.__maxY][x])
        if self.__grid[y][(x - 1) % self.__maxX]:
            res.append(self.__grid[y][(x - 1) % self.__maxX])
        if self.__grid[y][(x + 1) % self.__maxX]:
            res.append(self.__grid[y][(x + 1) % self.__maxX])
        return res


def update(self):
    for aThing in self.__thingList:
        aThing.update()

    # Remove dead bears from list and grid
    for aThing in self.__thingList:
        if isinstance(aThing, Bear) and aThing.isDead():
            self.delThing(aThing)

    def __str__(self):
        s = ''
    for y in range(self.__maxY - 1, -1, -1):
        for x in range(self.__maxX):
            if self.__grid[y][x]:
                s += str(self.__grid[y][x])
            else:
                s += '-'
        s += '\n'
    return s


class Thing:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__world = None
        self.__turtle = turtle.Turtle()
        self.__turtle.hideturtle()
        self.__turtle.speed(0)

    def setX(self, x):
        self.__x = x

    def getX(self):
        return self.__x

    def setY(self, y):
        self.__y = y

    def getY(self):
        return self.__y

    def setWorld(self, aWorld):
        self.__world = aWorld

    def getWorld(self):
        return self.__world

    def appear(self):
        self.__turtle.goto(self.__x, self.__y)
        self.__turtle.showturtle()

    def hide(self):
        self.__turtle.hideturtle()

    def move(self, newX, newY):
        self.hide()
        self.setX(newX)
        self.setY(newY)
        self.appear()
        self.getWorld().moveThing(self.getX(), self.getY(), newX, newY)

    def update(self):
        pass

    def __str__(self):
        return 'T'


class Plant(Thing):
    def __init__(self, x, y):
        Thing.__init__(self, x, y)

    def __str__(self):
        return 'B'


class Fish(Thing):
    def __init__(self, x, y, world):
        Thing.__init__(self, x, y)
        self.__world = world
        self.__turtle.shape("Fish.gif")

    def __str__(self):
        return 'F'

    def update(self):
        neighbors = self.__world.getNeighbors(self.getX(), self.getY())
        plants = [x for x in neighbors if isinstance(x, Plant)]
        if plants:
            plant = plants[0]
            self.move(plant.getX(), plant.getY())
            self.__world.delThing(plant)
        else:
            self.move(random.randrange(self.__world.getMaxX()),
                      random.randrange(self.__world.getMaxY()))


class Bear(Thing):
    def __init__(self, x, y, world):
        Thing.__init__(self, x, y)
        self.__world = world
        self.__turtle.shape("Bear.gif")
        self.__energy = 10  # Initialize energy level

    def __str__(self):
        return 'B'

    def update(self):
        neighbors = self.__world.getNeighbors(self.getX(), self.getY())
        plantNeighbors = [x for x in neighbors if isinstance(x, Plant)]
        if plantNeighbors:
            plant = plantNeighbors[0]
            self.move(plant.getX(), plant.getY())
            self.__world.delThing(plant)
            self.__energy += 5  # Increase energy level when eating
        else:
            fishNeighbors = [x for x in neighbors if isinstance(x, Fish)]
            if fishNeighbors:
                fish = fishNeighbors[0]
                self.move(fish.getX(), fish.getY())
                self.__world.delThing(fish)
                self.__energy += 5  # Increase energy level when eating
            else:
                self.move(random.randrange(self.__world.getMaxX()),
                          random.randrange(self.__world.getMaxY()))
                self.__energy -= 1  # Decrease energy level when moving or breeding

        # If energy level drops to 0, bear dies
        if self.__energy <= 0:
            self.die()

    def die(self):
        self.hide()
        self.__world.delThing(self)

    def isDead(self):
        return self.__turtle.isvisible() == False


def mainSimulation():
    # Create two lists to keep track of the number of fish and bears at each time unit
    numFishList = []
    numBearsList = []

    # Create the world and add 10 plants
    w = World(20, 20)
    w.draw()
    for i in range(10):
        Plant(random.randrange(0, w.getMaxX()),
              random.randrange(0, w.getMaxY())).setWorld(w)

    # Add 3 bears
    for i in range(3):
        Bear(random.randrange(0, w.getMaxX()),
             random.randrange(0, w.getMaxY()), w).setWorld(w)

    # Add 30 fish
    for i in range(30):
        Fish(random.randrange(0, w.getMaxX()),
             random.randrange(0, w.getMaxY()), w).setWorld(w)

    for i in range(20):
        numFishList.append(
            len([x for x in w.getThingList() if isinstance(x, Fish)]))
        numBearsList.append(
            len([x for x in w.getThingList() if isinstance(x, Bear)]))
        w.update()

    # Write the number of fish and bears at each time unit to a file
    with open('fish_bears.txt', 'w') as f:
        f.write('Time,Fish,Bears\n')
        for i in range(20):
            f.write(f'{i},{numFishList[i]},{numBearsList[i]}\n')


mainSimulation()
