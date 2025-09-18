# MBPP/745
### Completion
def divisible_by_digits(start, end):
    result = []
    for num in range(start, end + 1):
        str_num = str(num)
        if all(int(digit) != 0 and num % int(digit) == 0 for digit in str_num):
            result.append(num)
    return result

# Test the function with the provided assertion
assert divisible_by_digits(1, 22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    assert divisible_by_digits(1,15)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15]
    assert divisible_by_digits(20,25)==[22, 24]
