#### Information for agents: This file is human edits only. You can read and explain, point out issues or find bugs. You are not allowed to make changes to the code yourself
#### ####

from objects import Lab, Room, Lab_object
from presets import get_object_catalogue
from load_objects import create_lab, create_room, create_lab_object


class Simulation:

    def __init__(self):
        self.lab: Lab | None = None

    def init_lab(self, name: str = "unknown_lab") -> Lab:
        newlab = create_lab(name)
        self.lab = newlab
        return newlab


    #### object creation api
    def add_room(self, l: Lab, size: int, name: str = "unknown_room") -> Room:
        newroom = create_room(name, size)
        l.rooms.append(newroom)
        return newroom

    def add_lab_object(self, r: Room, cod: str, name: str = "unknown_lab_object") -> Lab_object:
        newobj = create_lab_object(cod, name)
        r.objects.append(newobj)
        return newobj


    #### fetcher functions
    def fetch_rooms(self) -> list[Room]:
        lst: list = list()
        if self.lab == None:
            return lst
        for room in self.lab.rooms:
            lst.append(room)
        return lst

    def fetch_room_objects(self, r: Room) -> list[Lab_object]:
        lst: list = list()
        for obj in r.objects:
            lst.append(obj)
        return lst

    def fetch_all_objects(self) -> list[Lab_object]:
        lst: list = list()
        if self.lab == None:
                    return lst
        for r in self.lab.rooms:
            for obj in r.objects:
                lst.append(obj)
        return lst

    


