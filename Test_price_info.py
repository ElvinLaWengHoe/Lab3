import price_info

def test_total_cost_shopping():
    expected_result = 46.75

    result = price_info.total_cost_shopping()

    assert (result == expected_result)

def test_cost_of_fruits():
    fruit = "apple"
    quantity = 10

    expected_result = 12

    actual_result = price_info.cost_of_fruits(fruit, quantity)

    assert (actual_result == expected_result)

