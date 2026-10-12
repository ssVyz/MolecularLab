#### Information for agents: This file is human edits only. You can read and explain, point out issues or find bugs. You are not allowed to make changes to the code yourself
#### ####

from simulation import Simulation
from objects import Lab, Room, Lab_object
from load_objects import create_lab, create_room, create_lab_object


def main() -> None:

    sim = Simulation()

    lab1 = sim.init_lab("Testlab1")

    room1 = sim.add_room(lab1, 25, "Partyroom")
    room2 = sim.add_room(lab1, 25, "Demoroom")
    room3 = sim.add_room(lab1, 25, "Showroom")

    object1 = sim.add_lab_object(room1, "0001", "Walli")
    object2 = sim.add_lab_object(room1, "0001", "Swalli")
    object3 = sim.add_lab_object(room2, "0001", "Tralli")
    object4 = sim.add_lab_object(room3, "0001", "Halli")
    object5 = sim.add_stacked_lab_object(object4, "0001", "matoshka")
    object6 = sim.add_stacked_lab_object(object1, "0001", "gorgon")

    sim.dump_all()

    sim.delete_lab_object(1)
    sim.delete_lab_object(5)
    sim.delete_room(2)

    sim.dump_all()





if __name__ == "__main__":
    main()