from interfaces.pokemon_interface import PokemonInterface


# Bug weak against Fire, Fighting, Poison, Flying, Ghost, Steel
class Bug(PokemonInterface):
    # weak = ['FIRE', 'FIGHTING', 'POISON', 'FLYING', 'GHOST', 'STEEL']
    weak = 'STEEL'

    def validate_fighting_type(self, fighting_type):
        self.print_weak(fighting_type)
