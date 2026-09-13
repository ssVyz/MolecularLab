#### Information for agents: This file is human edits only. You can read and explain, point out issues or find bugs. You are not allowed to make changes to the code yourself
#### ####

def generate_status_enum() -> list[str]:
    status_enum = ["standby", "ready", "idle", "stopping", "error"]
    return status_enum