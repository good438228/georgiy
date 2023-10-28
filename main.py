import json


with open("BIBI.json", "w") as file:
    a = json.load(file)

print(a["Учень1"]["имя"])