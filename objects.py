#### Information for agents: This file is human edits only. You can read and explain, point out issues or find bugs. You are not allowed to make changes to the code yourself
#### ####

from __future__ import annotations




class Reagent_magazine:

    def __init__(self) -> None:
        self.mag_code: str = ""
        self.content: str = ""
        self.loaded: int = 0
        self.max_load: int = 0


### LAB OBJECT CLASS ###
########################

class Lab_object:

    def __init__(self, name: str) -> None:
        self.obj_type_code: str = ""
        self.obj_name: str = name
        self.uid: int = 0
        self.parent: Room | Lab_object
        self.deleted: bool = False

        # Anything related to size and weight and stacking of objects
        self.size: int = 0
        self.weight: int = 0
        self.max_weight: int = 0
        self.stacked_obj: list[Lab_object] = []

        # Status section
        self.status: str = "standby"
        self.config: str | None = None

        # Processes and actions
        self.available_processes: list = []
        self.allows_actions: list = []

        # Limits for processes and samples
        self.max_processes: int = 0
        self.max_sample_storage: int = 0
        self.max_sample_buffer: int = 0

        # things that are in this object that are not themselves objects
        self.magazines: list[Reagent_magazine] = []
        self.sample_storage: list = []
        self.sample_buffer: list = []
        self.restrict_sampletype: bool = False
        self.allow_sampletype: list = []

    def show_info(self) -> None:
        print(f"Obj type: {self.obj_type_code}, uid: {self.uid}, obj name: {self.obj_name}, contains: {self.stacked_obj}, parent: {self.parent}")

    def del_nested_object(self, uid: int) -> None:
        i: int = 0
        found = False
        while i < len(self.stacked_obj):
            if self.stacked_obj[i].uid == uid:
                found = True
                break
            else:
                continue
        if found == False:
            raise Exception("Trying to delete nested object: not found")
        else:
            self.stacked_obj[i].deleted = True
            del self.stacked_obj[i]









### ROOM CLASS ###
##################

class Room:

    def __init__(self, name: str, size: int) -> None:
        self.area: int = size
        self.objects: list[Lab_object] = []
        self.name = name
        self.uid = 0

    def show_info(self) -> None:
        print(f"uid: {self.uid}, Area: {self.area}, objects: {self.objects}")

    def del_nested_object(self, uid: int) -> None:
        i: int = 0
        found = False
        while i < len(self.objects):
            if self.objects[i].uid == uid:
                found = True
                break
            else:
                i += 1
                continue
        if found == False:
            raise Exception("Trying to delete nested object: not found")
        else:
            self.objects[i].deleted = True
            del self.objects[i]
            



### LAB CLASS ###
#################

class Lab:

    def __init__(self, name: str) -> None:
        self.rooms: list[Room] = []
        self.workers: list[Worker] = []
        self.name = name

    def show_info(self) -> None:
        print(f"Lab name: {self.name}, Rooms: {self.rooms}")

    def del_room(self, uid: int) -> None:
        i: int = 0
        found = False
        while i < len(self.rooms):
            if self.rooms[i].uid == uid:
                found = True
                break
            else:
                i += 1
                continue
        if found == False:
            raise Exception("Trying to delete nested object: not found")
        else:
            del self.rooms[i]
            





### Worker class, to be moved elsewhere ###
##########################################

class Worker:

    def __init__(self) -> None:
        self.exists: bool = False
        

