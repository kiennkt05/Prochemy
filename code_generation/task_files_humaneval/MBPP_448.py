# MBPP/448
### Completion
def cal_sum(n):
    # Base cases for the first three Perrin numbers
    if n < 0:
        return 0  # If n is negative, return 0 as there are no Perrin numbers
    elif n == 0:
        return 3  # P(0)
    elif n == 1:
        return 3  # P(0) + P(1) = 3 + 0
    elif n == 2:
        return 5  # P(0) + P(1) + P(2) = 3 + 0 + 2

    # Initialize the first three Perrin numbers
    p0, p1, p2 = 3, 0, 2
    total_sum = p0 + p1 + p2  # Start with the sum of the first three numbers

    # Calculate Perrin numbers from P(3) to P(n) and sum them
    for i in range(3, n + 1):
        p_next = p1 + p0  # P(n) = P(n-2) + P(n-3)
        total_sum += p_next  # Add the new Perrin number to the total sum
        # Update the previous Perrin numbers
        p0, p1 = p1, p2
        p2 = p_next

    return total_sum

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
