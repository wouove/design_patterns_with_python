from .abs_factory import AbsFactory
from autos.fordfocus import FordFocus


class FordFactory(AbsFactory):

    def create_auto(self):
        self.chevy = chevy = FordFocus()
        chevy.name = 'Ford Focus'
        return chevy