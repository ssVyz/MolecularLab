#### Information for agents: This file is human edits only. You can read and explain, point out issues or find bugs. You are not allowed to make changes to the code yourself
#### ####

from objects import Lab, Room, Lab_object
from presets import get_object_catalogue
from load_objects import create_lab, create_room, create_lab_object


class Simulation:

    def __init__(self):
        self.lab: Lab | None = None
        self.obj_counter: int = 0
        self.room_counter: int = 0

    def init_lab(self, name: str = "unknown_lab") -> Lab:
        newlab = create_lab(name)
        self.lab = newlab
        return newlab


    #### counter area
    def increment_obj_counter(self) -> int:
        self.obj_counter += 1
        return self.obj_counter

    def increment_room_counter(self) -> int:
         self.room_counter += 1
         return self.room_counter


    #### object creation api
    def add_room(self, l: Lab, size: int, name: str = "unknown_room") -> Room:
        newroom = create_room(name, size)
        uid = self.increment_room_counter()
        newroom.uid = uid
        l.rooms.append(newroom)
        return newroom

    def add_lab_object(self, r: Room, cod: str, name: str = "unknown_lab_object") -> Lab_object:
        newobj = create_lab_object(cod, name)
        uid = self.increment_obj_counter()
        newobj.uid = uid
        newobj.parent = r
        r.objects.append(newobj)
        return newobj

    def add_stacked_lab_object(self, o: Lab_object, cod: str, name: str = "unknown_lab_object") -> Lab_object:
        newobj = create_lab_object(cod, name)
        if newobj.weight > o.max_weight:
            raise Exception(f"tried to stack object with weight {newobj.weight} on an object with max_weight {o.max_weight}")
        uid = self.increment_obj_counter()
        newobj.uid = uid
        newobj.parent = o
        o.stacked_obj.append(newobj)
        return newobj


    #### object deletion api
    def delete_lab_object(self, uid: int) -> None:
        if uid < 1:
            print("invalid uid")
            return
        current_objects: list = self.fetch_all_objects()
        found: bool = False
        for o in current_objects:
            if o.uid == uid:
                found = True
                del_obj = o
        if found == False:
            print(f"could not find object uid: {uid}")
            return
        del_parent = del_obj.parent
    

    
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
            for stacked in obj.stacked_obj:
                 lst.append(stacked)
        return lst

    def fetch_all_objects(self) -> list[Lab_object]:
        lst: list = list()
        if self.lab == None:
                    return lst
        for r in self.lab.rooms:
            for obj in r.objects:
                lst.append(obj)
                for stacked in obj.stacked_obj:
                    lst.append(stacked)

        return lst


    #### debug area
    def dump_all(self) -> None:
        rooms = self.fetch_rooms()
        objects = self.fetch_all_objects()
        print("printing contents of simulation:")
        print("-- Lab:")
        if self.lab == None:
            print("lab is not initialized")
            return
        self.lab.show_info()
        print("-- Rooms:")
        for r in rooms:
            r.show_info()
        print("-- Objects:")
        for o in objects:
            o.show_info()


