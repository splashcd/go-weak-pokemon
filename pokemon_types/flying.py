from interfaces.pokemon_interface import PokemonInterface


# Flying weak against Electric, Rock, Steel
class Flying(PokemonInterface):
    weak = ['ELECTRIC', 'ROCK', 'STEEL']

    def validate_fighting_type(self, fighting_type):
        self.print_weak(fighting_type)
