from interfaces.pokemon_interface import PokemonInterface


# Water weak against Water, Grass, Dragon
class Water(PokemonInterface):
    weak = ['WATER', 'GRASS', 'DRAGON']

    def validate_fighting_type(self, fighting_type):
        self.print_weak(fighting_type)
