from interfaces.pokemon_interface import PokemonInterface


# Dragon weak against Ice, Steel
class Dragon(PokemonInterface):
    weak = ['ICE', 'STEEL']

    def validate_fighting_type(self, fighting_type):
        self.print_weak(fighting_type)
