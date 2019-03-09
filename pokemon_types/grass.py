from interfaces.pokemon_interface import PokemonInterface


# Grass weak against Fire, Grass, Poison, Flying, Bug, Dragon, Steel
class Grass(PokemonInterface):
    weak = ['FIRE', 'GRASS', 'POISON', 'FLYING', 'BUG', 'DRAGON', 'STEEL']

    def validate_fighting_type(self, fighting_type):
        self.print_weak(fighting_type)
