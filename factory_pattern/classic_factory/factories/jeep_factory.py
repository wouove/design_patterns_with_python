from .abs_factory import AbsFactory
from autos.jeepsahara import JeepSahara


class JeepFactory(AbsFactory):

    def create_auto(self):
        self.chevy = chevy = JeepSahara()
        chevy.name = 'Jeep Sahara'
        return chevy
