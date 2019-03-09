from collections import defaultdict


class PokemonInterfaceMeta(type):
    def __init__(cls, name, bases, dct):
        if not hasattr(cls, 'registry'):
            # this is the base class.  Create an empty registry
            cls.registry = defaultdict(list)
        else:
            # this is a derived class.  Add cls weak to the registry
            if hasattr(cls, 'weak'):
                # The weak class attribute can be a list or a string
                if isinstance(cls.weak, list):
                    for handler in cls.weak:
                        if isinstance(handler, basestring):
                            cls.registry[handler].append(cls)
                else:
                    if isinstance(cls.weak, basestring):
                            cls.registry[cls.weak].append(cls)

        super(PokemonInterfaceMeta, cls).__init__(name, bases, dct)


class PokemonInterface:
    __metaclass__ = PokemonInterfaceMeta
    weak = None

    def validate_fighting_type(self, fighting_type):
        raise NotImplementedError

    def print_weak(self, fighting_type):
        print '{} is weak fighting {}'.format(self.__class__.__name__, fighting_type.get('type').upper())
