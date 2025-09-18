# MBPP/448
### Completion
def cal_sum(n):
    if n < 0:
        return 0
    elif n == 0:
        return 3
    elif n == 1:
        return 3  # P(0)
    elif n == 2:
        return 3 + 0 + 2  # P(0) + P(1) + P(2)

    # Initialize the first three Perrin numbers
    perrin_numbers = [3, 0, 2]
    
    # Calculate Perrin numbers up to P(n)
    for i in range(3, n + 1):
        next_perrin = perrin_numbers[i - 2] + perrin_numbers[i - 3]
        perrin_numbers.append(next_perrin)

    # Return the sum of the first n Perrin numbers
    return sum(perrin_numbers[:n + 1])

# Test the function with the provided assertion
assert cal_sum(9) == 49
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert cal_sum(9) == 49
    assert cal_sum(10) == 66
    assert cal_sum(11) == 88
