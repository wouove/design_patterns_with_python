from abc import ABCMeta, abstractmethod


class AbstractStrategy():
    __metaclass__ = ABCMeta

    @abstractmethod
    def calculate(self, order):
        """ Calculate shipping costs """
