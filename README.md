# py2-weak-pokemon
A python2 example of meta programming and self-registering subclasses (with lazy loading)

**Want to know which Pokemon types are weakest against a specific Pokemon type?**

In your software engineering efforts, you may come across a scenario which could benefit from plug-and-play classes.  This is a concise example of self-registering classes which can be added or removed easily without affecting the main functionality that `uses` them.
## Context
Pokemon is a game of fighting creatures that have a type hierarchy.  From what I understand, all Pokemon types are either effective, weak or neutral against other specific Pokemon types... which essentially ends up making it a very complicated version of _rock/paper/scissors_.

This project allows the developer to create new Pokemon classes which will increase the usefulness of the code's output.

This [link](https://www.eurogamer.net/articles/2018-12-21-pokemon-go-type-chart-effectiveness-weaknesses "Pokemon Type Chart") contains a chart documenting Pokemon types and which types they are strong or weak against.  This code attempts to provide a user with the **Weak Against** values quickly, given any Pokemon type.

## Implementation
The `find_weak_types_to_fight()` function, which is called from `main()`, accepts one dictionary with one `key` "type" and one string value of a Pokemon type

> Why did I choose a dictionary as the data type to pass into `find_weak_types_to_fight()`?
> Because a dictionary is a common data type passed in as a payload to a REST API, and that dictionary is also passed to each Pokemon Type class' _validate_fighting_type()_ methods, which can act on that payload as needed

Inside `find_weak_types_to_fight()` there is a call to `PokemonInterface.registry`, expecting it to be of a type **dictionary**.  But how can that be?  The code doesnt instantiate any Pokemon type classes, and it certainly doesnt instantiate an interface...

The answer is _Meta Programming_.  Unbenkownst to most developers, the import statements are doing more than anyone thinks.  Step through with a debugger and see what happens

When `PokemonInterface` is imported inside `weak_pokemon.py` it makes a call to its `__metaclass__` constructor.  Since there is no class attribute named _registry_, it creates one, assigning it the value `defaultdict(list)`.

This is used so the `registry` dict has a string key (Pokemon type) and a list value (classes of Pokemon types that are weak against it), because we will be pushing additional values as each Pokemon type class is evaluated.

> __One Annoyance__... Each Pokemon Type class has to be manually imported in `weak_pokemon.py`, which means you need a code change anytime a new class is added
```python
from pokemon_types.bug import Bug
from pokemon_types.dragon import Dragon
from pokemon_types.electric import Electric
from pokemon_types.flying import Flying
from pokemon_types.grass import Grass
from pokemon_types.ground import Ground
from pokemon_types.ice import Ice
from pokemon_types.rock import Rock
from pokemon_types.steel import Steel
from pokemon_types.water import Water
```

As each Pokemon type class is imported, since it implements the _PokemonInterface_ interface, the `__metaclass__` constructor is called... and this time the _registry_ class attribute exists, allowing values to be appended to the handler.

For each string in the Pokemon type's _weak_ class attribute (which is a list), the _registry_ dictionary receives another entry (if the key doesnt exist) or has a value appended (if the key exists).

Once all Pokemon type classes are imported then the `PokemonInterface.registry` dictionary is fully populated

## Lazy Importing

New Pokemon characters are periodically introduced into the game.  I have no idea if new Pokemon Types are introduced as well, but I'll assume they could be.

Since I'm all about the plug-and-play aspect, I want to be able to create a new class _as needed_ and add it to the _pokemon_types_ directory and **NOT** have to modify the _weak_pokemon.py_ file

This can be accomplished by the lazy importing of all files in that directory, by adding code to the traditionally empty *\_\_init__.py* file

```bash
from os.path import dirname, basename, isfile
import glob
modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [basename(f)[:-3] for f in modules if isfile(f) is True and not f.startswith('_')]`
```

Then the plethora of Pokemon Type class import statements in the  _weak_pokemon.py_ file can be replaced by this statement

```python
from pokemon_types import *
```

This solution was discovered by searching _python import all files in directory_ which led me to this [StackOverflow post](https://stackoverflow.com/questions/1057431/how-to-load-all-modules-in-a-folder).

New Pokemon Type classes can now be added to the _pokemon_types_ directory and be auto-magically imported without any changes to existing code :)

## Output
Given an input of: ``{'type': 'steel'}``

The output will be:
```
Finding weak Pokemon types to fight against type: STEEL...
Bug is weak fighting STEEL
Dragon is weak fighting STEEL
Flying is weak fighting STEEL
Grass is weak fighting STEEL
Ice is weak fighting STEEL
Rock is weak fighting STEEL
Steel is weak fighting STEEL
```

## Exercises
* Create the remaining Pokemon type classes from this [chart](https://www.eurogamer.net/articles/2018-12-21-pokemon-go-type-chart-effectiveness-weaknesses "Pokemon Type Chart")
* Add functionality to print which Pokemon types the Pokemon type in question is strong fighting against it.
* Convert this code into an API using [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/)

## References
[Pokemon Type Chart](https://www.eurogamer.net/articles/2018-12-21-pokemon-go-type-chart-effectiveness-weaknesses)

[A Primer On Python Metaclasses](https://jakevdp.github.io/blog/2012/12/01/a-primer-on-python-metaclasses/#Example-2:-Registering-Subclasses)

[Example Self Registration of Subclasses](https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Metaprogramming.html#example-self-registration-of-subclasses)

[Stack Overflow Question on Lazy Loading](https://stackoverflow.com/questions/1057431/how-to-load-all-modules-in-a-folder)