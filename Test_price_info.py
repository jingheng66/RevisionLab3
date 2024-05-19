import price_info

def test_total_cost_shipping():
    expected_cost = ((5 * 1.20) + (5 * 1.40) + (1 * 6.50) + (2 * 2.70) + (10 * 0.90) + (1 * 2.95) + (2 * 4.95))
    assert price_info.total_cost_shopping() == expected_cost

def test_cost_of_fruits():
    expected_cost_apple = 1.20 * 10
    assert price_info.cost_of_fruits("apple", 10) == expected_cost_apple