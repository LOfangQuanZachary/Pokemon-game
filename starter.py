# Opening
print("Welcome to the amazing world of Pokémon!")
print("Choose your starter Pokémon!\n")
print("""
The lizard Pokémon, \033[38;5;215m\033[1mCharmander!\033[0m
The seed Pokémon, \033[38;5;85m\033[1mBulbasaur!\033[0m
The tiny turtle Pokémon, \033[38;5;81m\033[1mSquirtle!\033[0m

""")
print("Which will you choose?")

# Must put at top level
pokemon = []
starter_pokemon_names = ["charmander", "bulbasaur", "squirtle"]
pokemon_names = ["charmander", "bulbasaur", "squirtle", "pikachu"]


___starter_py_secret = int(0)
___starter_py_secret_cap = 3

def ___starter_py_capfirst(strig : str):
    return strig[0].upper() + strig[1:].lower()

def ___starter_py_confirm(_pokename : str):
    pokename = ___starter_py_capfirst(_pokename)
    while (1):
        confirm = input("Are you sure about your choice? (%s) [y/n] " % (pokename)).lower()
        if (confirm[0] == "y"):
            return True
        elif (confirm[0] == "n"):
            return False
        else:
            continue

def GameLaunchFirstTime():
    global ___starter_py_secret, ___starter_py_secret_cap
    while (1):
        # Special case handling
        # i have 15 minutes
        # you see how slowly i code?
        # i make it gud quality but very slow
        got_secret = 0
        if (___starter_py_secret == ___starter_py_secret_cap):
            print("You have activated a secret event!")
            while (1):
                sp_confirm = input("Do you want to claim the alternate starter Pokémon? [y/n] ").lower()
                if (sp_confirm[0] == "y"):
                    print("Congratulations! You have received the secret \033[38;5;227m\033[1mPikachu!\033[0m")
                    pokemon.append("pikachu")
                    got_secret = 1
                    break
                elif (sp_confirm[0] == "n"):
                    print("You will not receive the alternate starter Pokémon.")
                    break
                else:
                    continue
       
        if (got_secret):
            break
        # my brain is dying, previously i could code
        # a html challenge in 30 minutes in primary 5

        

        # Take input and convert into lowercase
        curr_name = input("Desired Pokémon name: ").lower()
        
        if (curr_name in starter_pokemon_names):
            confirm = ___starter_py_confirm(curr_name)
            if (confirm):
                print("Congratulations! You have chosen %s!\n" % (pokename))
                pokemon.append(curr_name)
                ___starter_py_secret = 0
                break
            else:
                print("\n")
                ___starter_py_secret += 1
                continue
        else:
            print("That is not a valid Pokémon!\n")
            continue

GameLaunchFirstTime()
