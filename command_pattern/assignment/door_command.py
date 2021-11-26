from command_abc import AbsCommand
from actions.door import Door


class DoorLockCommand(AbsCommand):
    def __init__(self, door):
        if not isinstance(door, Door):
            raise TypeError
        self.door = door

    def execute(self):
        self.door.lock()

    def undo(self):
        self.door.unlock()


class DoorUnlockCommand(AbsCommand):
    def __init__(self, door):
        if not isinstance(door, Door):
            raise TypeError
        self.door = door

    def execute(self):
        self.door.unlock()

    def undo(self):
        self.door.lock()