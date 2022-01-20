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
chosen_pokemon = ""
starter_pokemon_names = ["charmander", "bulbasaur", "squirtle"]
pokemon_names = ["charmander", "bulbasaur", "squirtle"]




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
    while (1):
        # Take input and convert into lowercase
        curr_name = input("Pokémon name: ").lower()
        
        if (curr_name in starter_pokemon_names):
            confirm = ___starter_py_confirm(curr_name)
            if (confirm):
                print("Congratulations! You have chosen %s!\n" % (pokename))
                break
            else:
                print("\n")
                continue
        else:
            print("That is not a valid pokémon!\n")
            continue

