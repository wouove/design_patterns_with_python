from shipping_cost import ShippingCost
from order import Order

from fedex_strategy import FedExStrategy
from ups_strategy import UPSStrategy
from postal_strategy import PostalStrategy

if __name__ == '__main__':
    # Test fedex shipping
    order = Order()
    strategy = FedExStrategy()
    cost_calculator = ShippingCost(strategy)
    cost = cost_calculator.shipping_cost(order)
    assert cost == 3.0

    # Test UPS shipping
    order = Order()
    strategy = UPSStrategy()
    cost_calculator = ShippingCost(strategy)
    cost = cost_calculator.shipping_cost(order)
    assert cost == 4.0

    # Test Postal shipping
    order = Order()
    strategy = PostalStrategy()
    cost_calculator = ShippingCost(strategy)
    cost = cost_calculator.shipping_cost(order)
    assert cost == 5.0

    print("Tests finished")
