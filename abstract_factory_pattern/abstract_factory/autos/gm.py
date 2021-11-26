from abs_auto import AbsAuto


class ChevySpark(AbsAuto):
    def start(self):
        print("Chevy spark running")

    def stop(self):
        print("Chevy spark shutting down")


class ChevyCamarro(AbsAuto):
    def start(self):
        print("Chevy Camarro running")

    def stop(self):
        print("Chevy Camarro shutting down")


class CadillacCTS(AbsAuto):
    def start(self):
        print("Cadillac CTS running")

    def stop(self):
        print("Cadillac CTS shutting down")
