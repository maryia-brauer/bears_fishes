# Bears and Fishes Ecosystem
This is simulated ecosystem where fish and bears move around, interact with their neighbors, and consume plants or each other based on certain rules. The simulation is run for 20 time units, and the number of fish and bears at each time unit is recorded.

1. The code begins by importing the turtle and random modules, which are used for graphical and random number generation purposes, respectively.

2. The World class represents the simulation world. It initializes the maximum X and Y coordinates, creates a grid to represent the world, and sets up the graphical display using the turtle module. It also defines methods to draw the world, add and remove things (bears, fish, plants), move things within the world, and access various properties of the world.

3. The Thing class is a base class for all the objects in the simulation. It initializes the coordinates, sets up the graphical turtle, and defines methods to manipulate the object's position, appearance, and movement.

4. The Plant, Fish, and Bear classes are subclasses of the Thing class, representing different types of objects in the simulation. They define additional attributes and behaviors specific to each type of object. For example, the Fish class has an update method that determines how a fish moves and interacts with its neighbors, while the Bear class has an additional energy attribute and methods for eating, dying, and checking if it's dead.

5. The mainSimulation function sets up the simulation by creating the world, adding initial objects (plants, fish, and bears), and running the simulation for a specified number of time units. It keeps track of the number of fish and bears at each time unit and writes the data to a file.
