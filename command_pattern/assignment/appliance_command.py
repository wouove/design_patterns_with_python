from command_abc import AbsCommand
from actions.appliance import Appliance


class ApplianceOnCommand(AbsCommand):
    def __init__(self, appliance):
        if not isinstance(appliance, Appliance):
            raise TypeError
        self.appliance = appliance

    def execute(self):
        self.appliance.on()

    def undo(self):
        self.appliance.off()


class ApplianceOffCommand(AbsCommand):
    def __init__(self, appliance):
        if not isinstance(appliance, Appliance):
            raise TypeError
        self.appliance = appliance

    def execute(self):
        self.appliance.off()

    def undo(self):
        self.appliance.on()