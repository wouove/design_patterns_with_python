import abc


class AbsCommand:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self):
        pass

    @abc.abstractmethod
    def undo(self):
        pass
