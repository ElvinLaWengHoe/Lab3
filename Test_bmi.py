import Lab2.bmi as bmi

def test_bmi_normal_weight():
    weight = 60
    height = 1.73
    expected_result= 0

    result = bmi.calculate_bmi(height, weight)
    assert(result == expected_result)

def test_bmi_over_weight():
    weight = 90
    height = 1.6
    expected_result= 1

    result = bmi.calculate_bmi(height, weight)
    assert(result == expected_result)

def test_bmi_under_weight():
    weight = 50
    height = 1.9
    expected_result= -1

    result = bmi.calculate_bmi(height, weight)
    assert(result == expected_result)