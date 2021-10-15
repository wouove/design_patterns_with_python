from kpis import KPIs
from current_kpis import CurrentKPIs
from forecast_kpis import ForecastKPIs

if __name__ == '__main__':
    kpis = KPIs()
    current_kpis = CurrentKPIs(kpis)
    forecast_kpis = ForecastKPIs(kpis)
    kpis.set_kpis(25, 10, 5)
    kpis.set_kpis(100, 50, 30)
    kpis.set_kpis(50, 10, 20)

    print("\n***** Detaching the Current KPIs observer *****\n")
    kpis.detach(current_kpis)
    kpis.set_kpis(150, 110, 120)
