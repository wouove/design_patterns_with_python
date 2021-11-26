import abc


class AbsAuto(metaclass=abc.ABCMeta):
    def start(self):
        pass

    def stop(self):
        pass
