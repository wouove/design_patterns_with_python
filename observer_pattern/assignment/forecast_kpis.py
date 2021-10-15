from observer_abc import AbsObserver


class ForecastKPIs(AbsObserver):
    open_tickets = -1
    closed_tickets = -1
    new_tickets = -1

    def __init__(self, kpis):
        self._kpis = kpis
        kpis.attach(self)

    def update(self, value):
        self.open_tickets = value["open_tickets"]
        self.closed_tickets = value["closed_tickets"]
        self.new_tickets = value["new_tickets"]
        self.display()

    def display(self):
        print(f"Forecasted open tickets: {self.open_tickets}")
        print(f"Forecasted closed tickets in next hour: {self.closed_tickets}")
        print(f"Forecasted new tickets received in next hour: {self.new_tickets}")
        print("***************\n")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._kpis.detach(self)
