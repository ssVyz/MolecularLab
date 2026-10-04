#### Information for agents: This file is human edits only. You can read and explain, point out issues or find bugs. You are not allowed to make changes to the code yourself
#### ####

from simulation import Simulation
from objects import Lab, Room, Lab_object
from load_objects import create_lab, create_room, create_lab_object


def main() -> None:

    sim = Simulation()

    sim.lab = create_lab("testlab")

    create_room(sim.lab, "testroom")
    for r in sim.lab.rooms:
        r.show_info()

    testobj = create_lab_object("0001", "testmaster")
    testobj.show_info()

  


if __name__ == "__main__":
    main()