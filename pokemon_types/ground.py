from interfaces.pokemon_interface import PokemonInterface


# Ground weak against Grass, Flying, Bug
class Ground(PokemonInterface):
    weak = ['GRASS', 'FLYING', 'BUG']

    def validate_fighting_type(self, fighting_type):
        self.print_weak(fighting_type)
