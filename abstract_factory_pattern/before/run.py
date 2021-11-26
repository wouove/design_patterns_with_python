from design_patterns_with_python.abstract_factory_pattern.before.factories import ChevySpark, ChevyCamarro, CadillacCTS
from design_patterns_with_python.abstract_factory_pattern.before.factories.ford import FordFiesta, FordMustang, LincolnMKS
from random import randint

makers = ('gm', 'ford')
editions = ('Economy', 'Sport', 'Luxury')
maker = makers[randint(0,1)]
edition = editions[randint(0, 2)]

if maker == 'gm':
    if edition == 'Economy':
        car = ChevySpark()
    elif edition == 'Sport':
        car = ChevyCamarro()
    elif edition == 'Luxury':
        car = CadillacCTS()
    else:
        raise ValueError("Unknown edition")
elif maker == 'ford':
    if edition == 'Economy':
        car = FordFiesta()
    elif edition == 'Sport':
        car = FordMustang()
    elif edition == 'Luxury':
        car = LincolnMKS()
    else:
        raise ValueError("Unknown edition")
else:
    raise ValueError("Unknown maker")

car.start()
car.stop()