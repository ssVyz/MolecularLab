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
        print(f"Obj type: {self.obj_type_code}, obj name: {self.obj_name}, contains: {self.stacked_obj}")

    def quick_setup(self, code: str, size: int, weight: int, max_weight: int) -> None:
        self.obj_type_code = code
        self.size = size
        self.weight = weight
        self.max_weight = max_weight

    def stack_object(self, o: Lab_object) -> str:
        if isinstance(o, Lab_object):
            self.stacked_obj.append(o)
            return "success"
        else:
            return "error while trying to stack object. Invalid object"





### ROOM CLASS ###
##################

class Room:

    def __init__(self, name: str) -> None:
        self.area: int = 0
        self.objects: list[Lab_object] = []
        self.name = name

    def quick_setup(self, size: int) -> None:
        if size >= 0 and isinstance(size, int):
            self.area = size

    def place_lab_object(self, o: Lab_object) -> str:
        if isinstance(o, Lab_object):
            self.objects.append(o)
            return "success"
        else:
            return "error trying to add the object"

    def show_info(self) -> None:
        print(f"Area: {self.area}, objects: {self.objects}")



### LAB CLASS ###
#################

class Lab:

    def __init__(self, name: str) -> None:
        self.rooms: list[Room] = []
        self.workers: list[Worker] = []
        self.name = name




### Worker class, to be moved elsewhere ###
##########################################

class Worker:

    def __init__(self) -> None:
        self.exists: bool = False
        

