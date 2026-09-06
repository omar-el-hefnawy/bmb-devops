from app import sum_numbers, mult_numbers, sub_numbers

def test_add_numbers():
    assert sum_numbers(2, 3) == 5
    assert sum_numbers(-1, 1) == 0
    assert sum_numbers(0, 0) == 0

def test_mult_numbers():
    assert mult_numbers(2, 3) == 6
    assert mult_numbers(-1, 1) == -1
    assert mult_numbers(0, 0) == 0

def test_sub_numbers():
    assert sub_numbers(2, 3) == -1
    assert sub_numbers(-1, 1) == -2
    assert sub_numbers(0, 0) == 0