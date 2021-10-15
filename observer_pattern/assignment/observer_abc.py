import abc

class AbsObserver:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def update(self, value):
        pass

    def __enter__(self):
        pass

    @abc.abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass