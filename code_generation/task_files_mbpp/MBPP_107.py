# MBPP/107
### Completion
def count_Hexadecimal(start, end):
    # Count the numbers in the range from start to end (inclusive)
    count = 0
    for num in range(start, end + 1):
        # Every integer can be represented in hexadecimal
        count += 1
    return count

# Test the function with the provided assertion
assert count_Hexadecimal(10, 15) == 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Hexadecimal(10,15) == 6
    assert count_Hexadecimal(2,4) == 0
    assert count_Hexadecimal(15,16) == 1
