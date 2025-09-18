# MBPP/398
### Completion
def sum_of_digits(numbers):
    """
    Computes the sum of digits of each number in the given list.

    Parameters:
    numbers (list of int): A list of integers.

    Returns:
    int: The total sum of all digits from all numbers in the list.
    """
    total_sum = 0  # Initialize total sum of digits

    for number in numbers:
        # Convert the number to string to iterate over each digit
        for digit in str(number):
            total_sum += int(digit)  # Convert digit back to int and add to total sum

    return total_sum

# Test case
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
