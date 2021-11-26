from .abs_factory import AbsFactory
from autos.checyvolt import ChevyVolt


class ChevyFactory(AbsFactory):

    def create_auto(self):
        self.chevy = chevy = ChevyVolt()
        chevy.name = 'Chevy Volt'
        return chevy
