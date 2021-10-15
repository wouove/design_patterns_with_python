import abc
from observer_abc import AbsObserver

class AbsSubject:
    __metaclass__ = abc.ABCMeta
    _observers = set()

    def attach(self, observer):
        if not isinstance(observer, AbsObserver):
            raise TypeError("Observer was not derived from abstract observer")
        self._observers |= {observer}

    def detach(self, observer):
        self._observers -= {observer}

    def notify(self, value=None):
        for observer in self._observers:
            if value is None:
                observer.update()
            else:
                observer.update(value)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._observers.clear()