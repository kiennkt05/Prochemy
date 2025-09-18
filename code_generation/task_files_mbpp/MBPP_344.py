# MBPP/344
### Completion
def count_Odd_Squares(start, end):
    count = 0
    for i in range(start, end + 1):
        # Check if i is a perfect square
        if (i**0.5).is_integer():
            count += 1
    return count

# Test the function with the provided assertion
assert count_Odd_Squares(5, 100) == 8
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Odd_Squares(5,100) == 8
    assert count_Odd_Squares(8,65) == 6
    assert count_Odd_Squares(2,5) == 1
