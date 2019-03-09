from interfaces.pokemon_interface import PokemonInterface


# Electric weak against Grass, Electric, Ground, Dragon
class Electric(PokemonInterface):
    weak = ['GRASS', 'ELECTRIC', 'GROUND', 'DRAGON']

    def validate_fighting_type(self, fighting_type):
        self.print_weak(fighting_type)
