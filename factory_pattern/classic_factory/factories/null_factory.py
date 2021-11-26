from .abs_factory import AbsFactory
from autos.nullcar import NullCar


class NullFactory(AbsFactory):

    def create_auto(self):
        self.chevy = chevy = NullCar('Unknown')
        chevy.name = 'Unknown'
        return chevy
