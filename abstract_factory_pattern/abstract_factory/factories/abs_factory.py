import abc

class AbsFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_economy():
        pass

    @abc.abstractmethod
    def create_sport():
        pass

    @abc.abstractmethod
    def create_luxury():
        pass
