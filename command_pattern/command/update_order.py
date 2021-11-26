from command_abc import AbsCommand
from order_command_abc import AbsOrderCommand

class UpdateOrder(AbsCommand, AbsOrderCommand):
    name = "UpdateQuantity"
    description = "UpdateQuantity number"

    def __init__(self, args):
        self.newgty = args[1]

    def execute(self):
        oldqty = 5
        print("Database updated")
        print(f"Logging updated quantity from {oldqty} to {self.newgty}")