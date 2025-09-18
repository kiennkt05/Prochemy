# MBPP/575
### Completion
def count_no(n, m, start, end):
    count = 0
    for number in range(start, end + 1):
        if number % m != 0:  # Check if the number is not a multiple of m
            count += 1
            if count == n:  # If we have found the nth number
                return number
    return None  # Return None if nth number is not found in the range

# Example usage
assert count_no(2, 3, 1, 10) == 5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_no(2,3,1,10) == 5
    assert count_no(3,6,4,20) == 11
    assert count_no(5,10,4,20) == 16
