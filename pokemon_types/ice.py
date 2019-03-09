from interfaces.pokemon_interface import PokemonInterface


# Ice weak against Water, Ice, Fire, Steel
class Ice(PokemonInterface):
    weak = ['WATER', 'ICE', 'FIRE', 'STEEL']

    def validate_fighting_type(self, fighting_type):
        self.print_weak(fighting_type)
