from interfaces.pokemon_interface import PokemonInterface


# Rock weak against Fighting, Ground, Steel
class Rock(PokemonInterface):
    weak = ['FIGHTING', 'GROUND', 'STEEL']

    def validate_fighting_type(self, fighting_type):
        self.print_weak(fighting_type)
