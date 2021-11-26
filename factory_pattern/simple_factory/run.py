from auto_factory import AutoFactory

factory = AutoFactory()

if __name__ == '__main__':
    for carname in 'ChevyVolt', 'FordFocus', 'JeepSahara', 'Tesla P900':
        car = factory.create_instance(carname)
        car.start()
        car.stop()
