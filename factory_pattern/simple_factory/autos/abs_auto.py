from abc import ABCMeta, abstractmethod


class AbsAuto:
    __metaclass__ = ABCMeta

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass