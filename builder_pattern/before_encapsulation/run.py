from computer import Computer
from mycomputer import MyComputer

# computer = Computer(case='Coolermaster N300',
#                     mainboard='MSI 970',
#                     cpu='Intel Core i7-4770',
#                     memory='Corsair Vengeance 16GB',
#                     hard_drive='Seagate 2TB',
#                     video_card='GeForce GTX 1070'
#                     )
builder = MyComputer()
builder.build_computer()
computer = builder.get_computer()
computer.display()
