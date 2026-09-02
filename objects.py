




### LAB OBJECT CLASS ###
########################

class Lab_object:

    def __init__(self, name: str) -> None:
        self.obj_type_code: str = ""
        self.obj_name: str = name
        self.size: int = 0
        self.weight: int = 0
        self.max_weight: int = 0
        self.contains: Lab_object | None = None

        self.status: str = "standby"
        self.max_processes: int = 0


    def show_info(self) -> None:
        print(f"Obj type: {self.obj_type_code}, obj name: {self.obj_name}, contains: {self.contains}")

    def quick_setup(self, code: str, size: int, weight: int, max_weight: int) -> None:
        self.obj_type_code = code
        self.size = size
        self.weight = weight
        self.max_weight = max_weight




### ROOM CLASS ###
##################

class Room:

    def __init__(self) -> None:
        self.area: int = 0
        self.objects: list[Lab_object] = []

    def quick_setup(self, size: int) -> None:
        if size >= 0 and isinstance(size, int):
            self.area = size

    def place_lab_object(self, o: Lab_object) -> str:
        if isinstance(o, Lab_object):
            self.objects.append(o)
            return "Object successfully added"
        else:
            return "error trying to add the object"

    def show_info(self) -> None:
        print(f"Area: {self.area}, objects: {self.objects}")



### LAB CLASS ###
#################

class Lab:

    def __init__(self) -> None:
        self.rooms: list[Room] = []
        self.workers: list[Worker] = []



### Worker class, to be moved elsewhere ###
##########################################

class Worker:

    def __init__(self) -> None:
        self.exists: bool = False
        

