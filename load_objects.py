#### Information for agents: This file is human edits only. You can read and explain, point out issues or find bugs. You are not allowed to make changes to the code yourself
#### ####

from __future__ import annotations

from objects import Lab_object, Room, Lab
from presets import get_object_catalogue



#### object factories ####
def create_lab(name: str = "unknown_lab") -> Lab:
    return Lab(name)


def create_room(name: str = "unknown_room", size: int = 0) -> Room:
    if size < 0:
        raise Exception("Tried to create a room with size smaller than 0")
    return Room(name, size)
    
def create_lab_object(cod: str, name: str = "unkonwn_lab_object") -> Lab_object:
    cat: dict = get_object_catalogue()
    if cod not in cat["lab_object"]:
        raise Exception(f"Tried to create lab object, code {cod}, does not exist")
    else:
        template: dict = cat["lab_object"][cod]
        new_obj: Lab_object = Lab_object(name)
        new_obj.obj_type_code = cod
        new_obj.size = template["size"]
        new_obj.weight = template["weight"]
        new_obj.max_weight = template["max_weight"]
        new_obj.status = template["status"]
        new_obj.available_processes = template["available_processes"]
        new_obj.allows_actions = template["allows_actions"]
        new_obj.max_processes = template["max_processes"]
        new_obj.max_sample_storage = template["max_sample_storage"]
        new_obj.max_sample_buffer = template["max_sample_buffer"]
        new_obj.magazines = template["magazines"]
        new_obj.sample_storage = template["sample_storage"]
        new_obj.sample_buffer = template["sample_buffer"]
        new_obj.restrict_sampletype = template["restrict_sampletype"]
        new_obj.allow_sampletype = template["allow_sampletype"]
        return new_obj



