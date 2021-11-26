from .abs_factory import AbsFactory
from design_patterns_with_python.abstract_factory_pattern.before.factories.ford import FordFiesta, FordMustang, \
    LincolnMKS


class FordFactory(AbsFactory):
    @staticmethod
    def create_economy():
        return FordFiesta()

    @staticmethod
    def create_sport():
        return FordMustang()

    @staticmethod
    def create_luxury():
        return LincolnMKS()
