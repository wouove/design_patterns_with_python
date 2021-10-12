from abstract_strategy import AbstractStrategy


class PostalStrategy(AbstractStrategy):
    def calculate(self, order):
        return 5.00
