from pokemon_types.interfaces.pokemon_interface import PokemonInterface
from pokemon_types.bug import Bug
from pokemon_types.dragon import Dragon
from pokemon_types.electric import Electric
from pokemon_types.flying import Flying
from pokemon_types.grass import Grass
from pokemon_types.ground import Ground
from pokemon_types.ice import Ice
from pokemon_types.rock import Rock
from pokemon_types.steel import Steel
from pokemon_types.water import Water


# Not the best example of implementing interfaces, as all classes implement the validate_fighting_type
#  exactly the same... but it surely doesnt have to be that way
#
# This code implements self-registering subclasses (all the pokemon type classes)
#
# The code will inform the user which pokemon pokemon_types are weak against a provided pokemon type
#
# Step through the code with a debugger.  You'll see that...
# 1. PokemonInterface is processed first
# 2. PokemonInterfaceMeta is processed second.  Since it doesnt have the registry attribute,
#     a default one is created using defaultdict(list)
# 3. All pokemon type classes are processed next.  As each one is processed, a call is made to
#     the metaclass of the interface it implements (PokemonInterfaceMeta).  Since the registry
#     attribute now exists, the flow jumps down into the else condition
#     #-#-# THE MAGIC HAPPENS HERE IN STEP 3 #-#-#
# 4. The main function is called, which calls the route() function


def find_weak_types_to_fight(fighting_type):
    pokemon_type = fighting_type.get('type').upper()
    print 'Finding weak Pokemon types to fight against type: {}...'.format(pokemon_type)
    weak = PokemonInterface.registry.get(pokemon_type)
    # ^ Look at the value of PokemonInterface.registry after adding break point.
    # PokemonInterface.registry is a dict.  Given any type on the left, you'll see a list of type classes
    #  on the right that are weak against it
    #
    # HOW is PokemonInterface.registry is a dict???  The code doesnt instantiate any Pokemon types and it
    #  certainly didnt instantiate the interface!
    # The answer is in the README
    #
    # Remove all the pokemon type class imports above and look at the value of PokemonInterface.registry
    if weak:
        for self_registering_class in weak:
            self_registering_class().validate_fighting_type(fighting_type)  # construct class and run interface function
            # ^ This calls validate_fighting_type method for each pokemon type that is weak against it,
            #  which will print once per weak pokemon type


if __name__ == '__main__':
    # Change the type value to see which pokemon pokemon_types are weak against it
    find_weak_types_to_fight({'type': 'steel'})
