import json


def get_firstname(full_name: str) -> str:
    if full_name is None:
        return "Not Found"
    first_name: str = full_name.split(" ")[0]
    return first_name


def get_lastname(full_name: str) -> str:
    if full_name is None:
        return "Not Found"
    
    names: str = full_name.split(" ")
    if len(names) < 2: return ""
    return names[-1]


if __name__ == "__main__":
    ...
