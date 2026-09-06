from app import add_numbers, mult_numbers, sub_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_mult_numbers():
    assert mult_numbers(2, 3) == 6
    assert mult_numbers(-1, 1) == -1
    assert mult_numbers(0, 0) == 0

def test_sub_numbers():
    assert sub_numbers(2, 3) == -1
    assert sub_numbers(-1, 1) == -2
    assert sub_numbers(0, 0) == 0