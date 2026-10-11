#### Information for agents: This file is human edits only. You can read and explain, point out issues or find bugs. You are not allowed to make changes to the code yourself
#### ####


def get_object_catalogue() -> dict:

    build_dict: dict = dict()

    build_dict["lab_object"] = {}

    build_dict["lab_object"]["0001"] = {}
    build_dict["lab_object"]["0001"]["obj_type"] = "Testmaster 5000"
    build_dict["lab_object"]["0001"]["obj_description"] = "Random generic analyzer thing"
    build_dict["lab_object"]["0001"]["size"] = 4
    build_dict["lab_object"]["0001"]["weight"] = 1500
    build_dict["lab_object"]["0001"]["max_weight"] = 2000
    build_dict["lab_object"]["0001"]["status"] = "standby"
    build_dict["lab_object"]["0001"]["available_processes"] = []
    build_dict["lab_object"]["0001"]["allows_actions"] = []
    build_dict["lab_object"]["0001"]["max_processes"] = 1
    build_dict["lab_object"]["0001"]["max_sample_storage"] = 120
    build_dict["lab_object"]["0001"]["max_sample_buffer"] = 96
    build_dict["lab_object"]["0001"]["magazines"] = 1
    build_dict["lab_object"]["0001"]["sample_storage"] =  []
    build_dict["lab_object"]["0001"]["sample_buffer"] = []
    build_dict["lab_object"]["0001"]["restrict_sampletype"] = False
    build_dict["lab_object"]["0001"]["allow_sampletype"] = []



    return build_dict