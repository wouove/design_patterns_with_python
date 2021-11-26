from director import Director
from mycomputer_builder import MyComputerBuilder
from budget_box_builder import BudgetBoxBuilder

computer_builder = Director(MyComputerBuilder())
computer_builder.build_computer()
my_computer = computer_builder.get_computer()
my_computer.display()

computer_builder = Director(BudgetBoxBuilder())
computer_builder.build_computer()
budget_computer = computer_builder.get_computer()
budget_computer.display()

