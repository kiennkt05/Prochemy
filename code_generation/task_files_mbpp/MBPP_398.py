# MBPP/398
### Completion
def sum_of_digits(numbers):
    total_sum = 0
    for number in numbers:
        total_sum += sum(int(digit) for digit in str(number))
    return total_sum

# Test the function with the provided assertion
assert sum_of_digits([10, 2, 56]) == 14
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_of_digits([10,2,56])==14
    assert sum_of_digits([[10,20,4,5,'b',70,'a']])==19
    assert sum_of_digits([10,20,-4,5,-70])==19
