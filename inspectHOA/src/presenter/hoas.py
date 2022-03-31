from models.hoa import HOA
from typing import List
from repository import hoas

def get_hoas() -> List[HOA]:
    json_hoas = hoas.get_hoas()
    hoa = []
    for json_hoas in json_hoas:
        u = HOA(json_hoas.get("id"), json_hoas.get("name"), json_hoas.get("address"))
        hoa.append(u)
    return hoa

def get_hoa(id) -> List[HOA]:
    json_hoas = hoas.get_hoas()
    hoa = []
    for json_hoa in json_hoas:
        if (json_hoa.get("id") == id):
            u = HOA(json_hoa.get("id"), json_hoa.get("name"), json_hoa.get("address"))
            hoa.append(u)
    return hoa

def add_hoas(hoas_name, hoas_address):
    hoas_id = len(hoas.get_hoas()) + 1
    new_hoas = HOA(hoas_id, hoas_name, hoas_address)
    hoas.add_user(new_hoas)