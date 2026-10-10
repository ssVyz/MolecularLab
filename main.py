#### Information for agents: This file is human edits only. You can read and explain, point out issues or find bugs. You are not allowed to make changes to the code yourself
#### ####

from objects import *
from simulation import Simulation



def main() -> None:

    sim = Simulation()

    sim.init_lab("lab1")

    sim.lab.add_room("room1", 25)

    sim.lab.rooms[0].add_lab_object("0001", "testobject")

    sim.lab.show_info()
    sim.lab.rooms[0].show_info()
    sim.lab.rooms[0].objects[0].show_info()


  


if __name__ == "__main__":
    main()
