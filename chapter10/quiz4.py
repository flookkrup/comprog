from copy import deepcopy
import json

person_1 = {
    "name": "Zara",
    "lastname": "Ali",
    "age" : 7,
    "friends" : ["Jacklyn","Mimi","Kevyn","Venetia","Harmonie"]
}
person_2 = deepcopy(person_1)

# Test Deep Copy
person_1["friends"].append("Zoey")

print(json.dumps(person_1, sort_keys=False, indent=2))
print(json.dumps(person_2, sort_keys=False, indent=2))