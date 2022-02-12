import json
import random as r

pokedex = json.load(open("pokemon.json"))

class Pokemon():
    def __init__(self, name, level):
        
        
