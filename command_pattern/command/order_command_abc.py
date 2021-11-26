import abc

class AbsOrderCommand:
    __metaclass__ = abc.ABCMeta

    @property
    @abc.abstractmethod
    def name(self):
        pass

    @property
    @abc.abstractmethod
    def description(self):
        pass