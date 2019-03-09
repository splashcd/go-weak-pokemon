from interfaces.pokemon_interface import PokemonInterface


# Steel weak against Fire, Water, Steel
class Steel(PokemonInterface):
    weak = ['FIRE', 'WATER', 'STEEL']

    def validate_fighting_type(self, fighting_type):
        self.print_weak(fighting_type)
