

class Lab:

    def __init__(self) -> None:
        self.rooms: list[Room] = []
        self.workers: list[Worker] = []


class Room:

    def __init__(self) -> None:
        self.area: int = 0
        self.objects: list[Lab_object] = []


class Lab_object:

    def __init__(self) -> None:
        self.obj_type_code: str = ""
        self.size: int = 0
        self.weight: int = 0
        self.max_weight: int = 0
        self.contains: Lab_object | None = None

    def show_info(self) -> None:
        print(f"Obj type: {self.obj_type_code}, contains: {self.contains}")

    def quick_setup(self, code: str, size: int, weight: int, max_weight: int) -> None:
        self.obj_type_code = code
        self.size = size
        self.weight = weight
        self.max_weight = max_weight


class Worker:

    def __init__(self) -> None:
        self.exists: bool = False
        

