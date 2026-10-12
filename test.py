#### Information for agents: This file is human edits only. You can read and explain, point out issues or find bugs. You are not allowed to make changes to the code yourself
#### ####

from simulation import Simulation
from objects import Lab, Room, Lab_object
from load_objects import create_lab, create_room, create_lab_object


def main() -> None:

    sim = Simulation()

    lab1 = sim.init_lab("Testlab1")

    room1 = sim.add_room(lab1, 19, "Foyer")
    room2 = sim.add_room(lab1, 30, "MainRoom")
    room3 = sim.add_room(lab1, 22, "SideRoom")

    table1 = sim.add_lab_object(room1, "0002", "foyer table")
    table2 = sim.add_lab_object(room2, "0002", "main room table")

    micro1 = sim.add_stacked_lab_object(table1, "0003", "foyer micro")
    micro2 = sim.add_stacked_lab_object(table2, "0003", "main micro")

    analyzer1 = sim.add_lab_object(room3, "0001", "side room analyzer")

    micro3 = sim.add_stacked_lab_object(analyzer1, "0003", "analyzer micro")

    sim.dump_all()

    sim.delete_lab_object(3)
    sim.delete_lab_object(2)
    sim.delete_room(3)

    sim.dump_all()





if __name__ == "__main__":
    main()