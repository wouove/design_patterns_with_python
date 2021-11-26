import abc


class AbsCommand:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self):
        pass
