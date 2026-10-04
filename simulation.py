#### Information for agents: This file is human edits only. You can read and explain, point out issues or find bugs. You are not allowed to make changes to the code yourself
#### ####

from objects import Lab, Room, Lab_object
from presets import get_object_catalogue


class Simulation:

    def __init__(self):
        self.lab: Lab | None = None

