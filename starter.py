# Opening print statements
print("Welcome to the amazing world of Pokémon!")
print("Choose your starter Pokémon!\n")
print("""
The lizard Pokémon, \033[38;5;215m\033[1mCharmander!\033[0m
The seed Pokémon, \033[38;5;85m\033[1mBulbasaur!\033[0m
The tiny turtle Pokémon, \033[38;5;81m\033[1mSquirtle!\033[0m

""")
print("Which will you choose?")

# Some global variables
pokemon = []
starter_pokemon_names = ["charmander", "bulbasaur", "squirtle"]
pokemon_names = ["charmander", "bulbasaur", "squirtle", "pikachu"]

# For the secret pikachu unlock
___starter_py_secret = int(0)
___starter_py_secret_cap = 3


# Returns the first letter uppercase and the rest as lowercase.
def ___starter_py_capfirst(strig: str):
    return strig[0].upper() + strig[1:].lower()


# Code that continuously asks for a confirmation.
# Takes pokemon name as an input.
def ___starter_py_confirm(_pokename: str):
    pokename = ___starter_py_capfirst(_pokename)
    while (1):
        confirm = input("Are you sure about your choice? (%s) [y/n] "
                        % (pokename)).lower()
        if (confirm[0] == "y"):
            return True
        elif (confirm[0] == "n"):
            return False
        else:
            # If they didn't answer properly, re-ask for confirmation
            continue


# To be run when game first starts.
def GameLaunchFirstTime():
    global ___starter_py_secret, ___starter_py_secret_cap
    while (1):
        # Special case handling
        # If they already collected the secret, break
        got_secret = 0
        if (___starter_py_secret == ___starter_py_secret_cap):
            print("You have activated a secret event!")

            # Continuously ask for confirmation, with different print() values
            while (1):
                sp_confirm = input("Do you want to claim the alternate starter"
                                   " Pokémon? [y/n] ").lower()
                if (sp_confirm[0] == "y"):
                    # They really want the pikachu

                    print("Congratulations! You have received the secret \033["
                          "38;5;227m\033[1mPikachu!\033[0m")
                    pokemon.append("pikachu")
                    got_secret = 1
                    break
                elif (sp_confirm[0] == "n"):
                    # They are an idiot

                    print("You will not receive the alternate starter Pokémon."
                          )
                    break
                else:
                    # If they didn't answer properly, re-ask for confirmation
                    continue

        if (got_secret):
            break

        # Take input and convert into lowercase
        curr_name = input("Desired Pokémon name: ").lower()

        if (curr_name in starter_pokemon_names):
            confirm = ___starter_py_confirm(curr_name)
            if (confirm):
                # They want the pokemon they chose
                print("Congratulations! You have chosen %s!\n" %
                      (___starter_py_capfirst(curr_name)))
                pokemon.append(curr_name)
                ___starter_py_secret = 0
                break
            else:
                # They not confirmed it
                print("\n")
                ___starter_py_secret += 1
                continue
        else:
            print("That is not a valid Pokémon!\n")
            continue


# I wrapped it in a function, so i have to call it
# but you can use it anywhere else
GameLaunchFirstTime()
