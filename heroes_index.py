import httpx
r = httpx.get("https://api.opendota.com/api/heroes")


heroes_by_id = {i['id']:i for i in r.json() }


Ranged = []
Melee = []

for i in r.json():
    if i["attack_type"] == "Melee":
        Melee.append(i)
    if i["attack_type"] == "Ranged":
        Ranged.append(i)

Agility_Melee = []
Universal_Melee = []
Strength_Melee = []

Intellect_Ranged = []
Agility_Ranged = []
Universal_Ranged = []
Strength_Ranged = []

for i in Ranged:
    if i['primary_attr'] == "agi":
        Agility_Ranged.append(i)
    elif i['primary_attr'] == "int":
        Intellect_Ranged.append(i)
    elif i['primary_attr'] == "all":
        Universal_Ranged.append(i)
    elif i['primary_attr'] == "str":
        Strength_Ranged.append(i)
for i in Melee:
    if i['primary_attr'] == "agi":
        Agility_Melee.append(i)
    elif i['primary_attr'] == "all":
        Universal_Melee.append(i)
    elif i['primary_attr'] == "str":
        Strength_Melee.append(i)