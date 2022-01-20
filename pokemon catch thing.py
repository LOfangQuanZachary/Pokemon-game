#pokeball is val 1
#great ball is val 2
#ultraball is val 3

import random

wildPokemonStatusCondition = False
wildPokemonHealth = 35
pokemonBall = 1

def pokemonCatchChance(wildPokemonStatusCondition, wildPokemonHealth, pokemonBall):
    catchChance = 100
    if wildPokemonStatusCondition == True:
        catchChance = catchChance + 10
    catchChance = catchChance + (pokemonBall*5)
    catchChance = catchChance - (wildPokemonHealth*1.1 + 5) - 10
    if catchChance < 0 :
        print("The pokemon broke free!")
    elif catchChance > 100 :
        print("The pokemon has been caught!")
    else :
        n = random.randint(0, 100)
        if n >= catchChance:
            print("The pokemon has broke free!")
        elif n < catchChance:
            print("the pokemon has been caught!")
    print(catchChance)
pokemonCatchChance(True, 80, 3)
