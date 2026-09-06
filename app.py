def add_numbers(a, b):
    return a + b

def mult_numbers(a, b):
    return a * b

def sub_numbers(a, b):
    return a - b    


if __name__ == "__main__":
    num1 = 10
    num2 = 5

    sum_result = add_numbers(num1, num2)
    mult_result = mult_numbers(num1, num2)
    sub_result = sub_numbers(num1, num2)

    print(f"Sum: {sum_result}")
    print(f"Multiplication: {mult_result}")
    print(f"Subtraction: {sub_result}")