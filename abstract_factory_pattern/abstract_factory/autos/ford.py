from abs_auto import AbsAuto


class FordFiesta(AbsAuto):
    def start(self):
        print("Ford fiesta running")

    def stop(self):
        print("Ford fiesta shutting down")


class FordMustang(AbsAuto):
    def start(self):
        print("Ford mustang running")

    def stop(self):
        print("Ford mustang shutting down")


class LincolnMKS(AbsAuto):
    def start(self):
        print("Lincoln MKS running")

    def stop(self):
        print("Lincoln MKS shutting down")
