from .abs_factory import AbsFactory
from design_patterns_with_python.abstract_factory_pattern.before.factories.gm import ChevySpark, ChevyCamarro, CadillacCTS


class GMFactory(AbsFactory):
    @staticmethod
    def create_economy():
        return ChevySpark()

    @staticmethod
    def create_sport():
        return ChevyCamarro()

    @staticmethod
    def create_luxury():
        return CadillacCTS()
