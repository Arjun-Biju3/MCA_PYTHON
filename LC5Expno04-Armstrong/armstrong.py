def is_armstrong_number(num):
    order = len(str(num))
    sum_of_digits = sum(int(digit) ** order for digit in str(num))
    return num == sum_of_digits

def generate_armstrong_numbers(start, end):
    armstrong_numbers = [num for num in range(start, end + 1) if is_armstrong_number(num)]
    return armstrong_numbers
