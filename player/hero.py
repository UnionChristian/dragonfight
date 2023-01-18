import json


# body of the constructor
# Opening JSON file
with open('./player/hero.json', 'r') as heroData:

    # Reading from json file
    hero_data = json.load(heroData)
