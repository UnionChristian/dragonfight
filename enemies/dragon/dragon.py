import json


# body of the constructor
# Opening JSON file
with open('./enemies/dragon/dragon.json', 'r') as dragonData:

    # Reading from json file
    dragon_data = json.load(dragonData)